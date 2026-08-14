# Product Reference build

The Power Supply for Breadboard with Qwiic (UE0113) Product Reference source
is maintained in Markdown under `chapters/`. Document metadata and chapter
order are defined in `book.yml`. Version 1.0.0 migrates the released V1.0
datasheet into editable source, using the board schematic, pinout, topology,
and component datasheets as supporting references.

## Local validation build

Requirements:

- Pandoc
- WeasyPrint

Run from the repository root and direct validation output outside the
repository:

```bash
./tools/product-reference/build.sh /tmp/ue0113-product-reference
```

The build produces:

```text
unit_product_reference_v_1_0_0_ue0113_power_supply_for_breadboard_with_qwiic.md
unit_product_reference_v_1_0_0_ue0113_power_supply_for_breadboard_with_qwiic.docx
unit_product_reference_v_1_0_0_ue0113_power_supply_for_breadboard_with_qwiic.html
unit_product_reference_v_1_0_0_ue0113_power_supply_for_breadboard_with_qwiic.pdf
```

GitHub Actions publishes the PDF and DOCX under `docs/hardware/`. Do not edit
generated documents or `docs/` manually.

The Markdown chapters are the editable source of truth for the generated
reference. The released V1.0 PDF remains available in `hardware/` as the
historical release. Board values and mappings must come from board-level
documentation; do not infer complete module limits from an individual
component datasheet. Chapter 9 records source scope and version control.
