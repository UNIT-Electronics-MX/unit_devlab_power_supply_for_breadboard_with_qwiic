## **3 Functional Overview**

The module receives power from a USB-C PD source, negotiates a compatible
fixed profile through the HUSB238 controller, and distributes that negotiated
VUSB rail to the screw terminal and selectable breadboard headers. In parallel,
the TPS54302 converts VUSB to a regulated 3.3 V rail for logic and Qwiic
peripherals.

### **3.1 Power Distribution Architecture** {.section-page}

![Board topology](hardware/resources/unit_topology_v_1_0_0_ue0113_devlab_power_supply_for_breadboard_with_qwiic.png){width=6.9in}

The left and right breadboard rails have independent selectors. Each selector
can route VUSB, disconnect the rail, or route 3.3 V. This makes it possible to
use a higher PD voltage for one rail while retaining 3.3 V logic on the other.

| Selection | Function |
|---|---|
| `VUSB` | Routes the negotiated USB-C PD voltage to the rail |
| `OFF` | Disconnects the rail output |
| `3V3` | Routes the regulated 3.3 V rail to the rail |

### **3.2 USB-C Power Delivery** {.section-page}

The HUSB238 performs USB-C PD-sink negotiation with a compatible source. The
available profiles are determined by the charger and cable; selecting a
profile does not create a voltage that the source did not advertise. The
released datasheet describes 5 V, 9 V, 12 V, 15 V, and 20 V as the standard
profiles, and also mentions 18 V where that profile is offered by the source.

Use the onboard DIP switch for standalone configuration. When HUSB238 I²C
access is enabled, a host controller can monitor the connection and apply
dynamic selection; I²C configuration has priority over the DIP-switch setting.

### **3.3 Qwiic Expansion** {.section-page}

The Qwiic-compatible JST 1.0 mm connectors expose a shared 3.3 V I²C bus:
SDA, SCL, 3.3 V, and ground. Optional solder jumpers connect the HUSB238 to
that bus for monitoring and control. Leave those jumpers open when the
controller must remain isolated from the external Qwiic network.

The I²C bus is a 3.3 V logic domain. Do not apply VUSB to SDA, SCL, or the
Qwiic power pin.

### **3.4 Breadboard Integration** {.section-page}

The mechanical layout aligns with common 54 mm and 64 mm breadboard rail
formats. The two sides permit independent power assignment for cases such as:

| Left rail | Right rail | Typical use |
|---|---|---|
| 3.3 V | 3.3 V | Logic and sensor prototype |
| VUSB | 3.3 V | Mixed power and logic system |
| 12 V | 3.3 V | Motor driver with microcontroller |
| OFF | VUSB | Single high-voltage rail test |

The `12 V` example assumes that the source provides and the module has
selected that VUSB profile.
