## **9 Appendix**

### **9.1 Source Migration** {.section-page}

This editable product reference is migrated from the released PDF:

`hardware/unit_datasheet_v_1_0_0_ue0113_Power_Supply_for_Breadboard_with_Qwiic.pdf`

The original PDF is retained as a released historical artifact. The Markdown
chapters under `tools/product-reference/chapters/` are the source for future
generated PDF and DOCX editions.

### **9.2 Documentation Scope** {.section-page}

The module's negotiated VUSB output depends on the USB-C PD source and cable.
The listed component ratings do not independently establish all module-level
limits. Before high-voltage or high-current use, verify the selected profile,
measure the output, and account for all connected hardware.

The released V1.0 datasheet mentions an 18 V PD profile in descriptive text,
while its ratings tables enumerate 5 V, 9 V, 12 V, 15 V, and 20 V. This
reference treats 18 V as source-dependent rather than as a guaranteed standard
profile.

### **9.3 Document Control** {.section-page}

| Item | Value |
|---|---|
| Product reference version | 1.0.0 |
| Hardware revision | V1.0 |
| Manufacturer part number | UE0113 |
| Released datasheet date | 2026-06-30 |
| Editable source | `tools/product-reference/` |
