## **1 The Board**

The Power Supply for Breadboard with Qwiic provides a compact power entry and
distribution point for solderless breadboards. A USB-C PD source supplies the
module. The selected VUSB rail and the regulated 3.3 V rail can be assigned to
the two breadboard sides independently, which supports both single-voltage and
mixed-voltage prototypes.

### **1.1 Board Identification** {.section-page}

| Item | Value |
|---|---|
| Product | Power Supply for Breadboard with Qwiic |
| Manufacturer part number | UE0113 |
| Product family | UNIT Electronics DevLab |
| Product type | USB-C PD breadboard power-distribution module |
| Hardware revision | V1.0 |
| Product Reference | Version 1.0.0 |
| PD controller | HUSB238 |
| 3.3 V regulator | TPS54302 |

### **1.2 Included and Recommended Items** {.section-page}

The released V1.0 datasheet lists the following accessory items: 16 single-row
male headers, one Qwiic 4-pin JST 1.0 mm harness, and two jumper caps.

For safe operation, use a USB-C charger that supports the needed PD profile, a
USB-C cable rated for the expected voltage and current, and a breadboard with
the appropriate rail spacing. Verify the source profile before connecting a
load.

### **1.3 Main Assemblies** {.section-page}

| RefDes | Component or connector | Function |
|---|---|---|
| J1 | USB Type-C connector | PD power input |
| IC1 | HUSB238 | PD negotiation controller |
| SW1 | DIP switch | PD voltage-profile selection |
| U1 | TPS54302 | 3.3 V buck regulator |
| L1 | Power LED | Power indication |
| J6 | Screw terminal | VUSB output access |
| JP7 | Pin header | 3.3 V output access |
| JP3 / JP4 | Selector headers | Left and right rail-voltage selection |
| JP1 / JP2 | Left headers | Breadboard power connection |
| JP5 / JP6 | Right headers | Breadboard power connection |

### **1.4 Board Views** {.section-page}

![Top view](hardware/resources/unit_top_v_1_0_0_ue0113_devlab_power_supply_for_breadboard_with_qwiic.png){width=5.8in}

![Bottom view](hardware/resources/unit_btm_v_1_0_0_ue0113_devlab_power_supply_for_breadboard_with_qwiic.png){width=5.8in}

### **1.5 Handling** {.section-page}

Disconnect USB-C power before moving rail-selection jumpers, inserting the
board into a breadboard, or changing wiring. Keep high-voltage VUSB wiring
away from the 3.3 V logic rail and confirm polarity before connecting a load.
