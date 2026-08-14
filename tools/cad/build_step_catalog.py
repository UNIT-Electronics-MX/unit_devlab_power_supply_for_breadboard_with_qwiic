#!/usr/bin/env python3
"""Generate web-ready GLB and SVG files from STEP models.

The generated files are written to a staging directory. The caller is
responsible for publishing that directory next to the STEP source, preserving
the repository's ``hardware/mechanics`` layout.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import quote


STEP_EXTENSIONS = {".step", ".stp"}


def public_url(base_url: str, path: Path) -> str:
    """Return a Pages URL for an asset relative to the mechanics directory."""
    return f"{base_url.rstrip('/')}/{quote(path.as_posix(), safe='/-_.~')}"


def read_step_shapes(source: Path):
    """Read every free shape in a STEP file, retaining its assembly structure."""
    from OCP.STEPCAFControl import STEPCAFControl_Reader
    from OCP.TCollection import TCollection_ExtendedString
    from OCP.TDF import TDF_LabelSequence
    from OCP.TDocStd import TDocStd_Document
    from OCP.XCAFDoc import XCAFDoc_DocumentTool, XCAFDoc_ShapeTool

    document = TDocStd_Document(TCollection_ExtendedString("ue-component-assets"))
    reader = STEPCAFControl_Reader()
    reader.SetColorMode(True)
    if not reader.ReadFile(str(source)) or not reader.Transfer(document):
        raise ValueError("OpenCascade could not read the STEP file")

    shape_tool = XCAFDoc_DocumentTool.ShapeTool_s(document.Main())
    labels = TDF_LabelSequence()
    shape_tool.GetFreeShapes(labels)
    if not labels.Length():
        raise ValueError("The STEP file contains no free shapes")

    return [XCAFDoc_ShapeTool.GetShape_s(labels.Value(index)) for index in range(1, labels.Length() + 1)]


def make_compound(shapes):
    """Convert OpenCascade shapes to one CadQuery compound."""
    import cadquery as cq

    return cq.Compound.makeCompound([cq.Shape.cast(shape) for shape in shapes])


def export_glb(shapes, target: Path, linear_tolerance: float, angular_tolerance: float) -> None:
    """Tessellate a STEP assembly into a GLB model."""
    import cadquery as cq
    import trimesh
    from OCP.TopAbs import TopAbs_SOLID
    from OCP.TopExp import TopExp_Explorer

    scene = trimesh.Scene()
    with tempfile.TemporaryDirectory(prefix="ue-step-glb-") as temporary:
        temporary_path = Path(temporary)
        part_number = 0
        for shape in shapes:
            solids = TopExp_Explorer(shape, TopAbs_SOLID)
            while solids.More():
                mesh_path = temporary_path / f"part-{part_number}.stl"
                cq.exporters.export(
                    cq.Shape.cast(solids.Current()),
                    str(mesh_path),
                    tolerance=linear_tolerance,
                    angularTolerance=angular_tolerance,
                )
                mesh = trimesh.load_mesh(mesh_path, force="mesh")
                if not mesh.is_empty:
                    mesh.visual.material = trimesh.visual.material.PBRMaterial(
                        baseColorFactor=(179, 184, 199, 255),
                        metallicFactor=0.0,
                        roughnessFactor=0.72,
                    )
                    scene.add_geometry(mesh, geom_name=f"part-{part_number}")
                part_number += 1
                solids.Next()

    if not scene.geometry:
        raise ValueError("The STEP file produced no convertible solids")
    target.parent.mkdir(parents=True, exist_ok=True)
    scene.export(target, file_type="glb")


def export_svg(shapes, target: Path) -> None:
    """Create an isometric vector preview of the STEP assembly."""
    import cadquery as cq

    compound = make_compound(shapes)
    target.parent.mkdir(parents=True, exist_ok=True)
    cq.exporters.export(
        compound,
        str(target),
        exportType="SVG",
        opt={
            "projectionDir": (1, -1, 1),
            "showAxes": False,
            "strokeColor": (36, 45, 57),
            "hiddenColor": (145, 153, 165),
        },
    )


def output_name(source: Path, extension: str) -> Path:
    """Keep generated assets beside the source model with the same basename."""
    return Path(f"{source.stem}{extension}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True, help="directory containing STEP files")
    parser.add_argument("--output", type=Path, required=True, help="empty staging directory for generated assets")
    parser.add_argument("--public-base-url", required=True, help="Pages URL for the mechanics directory")
    parser.add_argument("--linear-tolerance", type=float, default=0.05, help="GLB linear tolerance in mm")
    parser.add_argument("--angular-tolerance", type=float, default=0.10, help="GLB angular tolerance in radians")
    arguments = parser.parse_args()

    source_root = arguments.input.resolve()
    output = arguments.output.resolve()
    if not source_root.is_dir():
        parser.error(f"input directory does not exist: {source_root}")
    if output == source_root:
        parser.error("output must be a separate staging directory")
    if arguments.linear_tolerance <= 0 or arguments.angular_tolerance <= 0:
        parser.error("tolerances must be greater than zero")

    if output.exists():
        shutil.rmtree(output)
    output.mkdir(parents=True)

    step_files = sorted(path for path in source_root.rglob("*") if path.suffix.lower() in STEP_EXTENSIONS)
    output_stems = [source.relative_to(source_root).stem for source in step_files]
    if len(set(output_stems)) != len(output_stems):
        parser.error("STEP filenames must be unique when publishing flat mechanics assets")

    components = []
    failures = 0
    for source in step_files:
        relative_source = source.relative_to(source_root)
        glb_path = output_name(relative_source, ".glb")
        svg_path = output_name(relative_source, ".svg")
        component = {
            "id": hashlib.sha256(relative_source.as_posix().encode()).hexdigest()[:10],
            "source_step": {
                "path": relative_source.as_posix(),
                "url": public_url(arguments.public_base_url, relative_source),
            },
            "model_glb": {"path": glb_path.as_posix(), "url": public_url(arguments.public_base_url, glb_path)},
            "preview_svg": {"path": svg_path.as_posix(), "url": public_url(arguments.public_base_url, svg_path)},
        }
        try:
            shapes = read_step_shapes(source)
            export_glb(shapes, output / glb_path, arguments.linear_tolerance, arguments.angular_tolerance)
            export_svg(shapes, output / svg_path)
            print(f"Generated GLB and SVG: {relative_source}")
        except Exception as error:
            failures += 1
            component["error"] = str(error)
            print(f"Could not convert {relative_source}: {error}")
        components.append(component)

    manifest = {
        "schema_version": 1,
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "public_base_url": arguments.public_base_url.rstrip("/"),
        "components": components,
    }
    (output / "catalog.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Generated catalog for {len(components)} STEP file(s): {output / 'catalog.json'}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
