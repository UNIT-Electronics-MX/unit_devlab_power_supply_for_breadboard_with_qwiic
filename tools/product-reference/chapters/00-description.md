## **Description**

The DevLab Power Supply for Breadboard with Qwiic is a USB Type-C-powered
power-distribution module for breadboard-based electronic prototyping. It acts
as a USB Power Delivery (PD) sink, negotiates a profile from a compatible
source, and routes the negotiated VUSB rail to selectable breadboard outputs.
An onboard TPS54302 buck regulator supplies a separate 3.3 V rail.

![Power Supply for Breadboard with Qwiic top view](hardware/resources/unit_top_v_1_0_0_ue0113_devlab_power_supply_for_breadboard_with_qwiic.png){width=5.8in}

### **Applications**

- Breadboard power distribution and mixed-voltage prototyping
- USB-C PD source and cable evaluation
- Embedded-system, sensor, and peripheral development
- Laboratory education, validation, and early hardware testing

### **Hardware Features**

- USB Type-C PD input with HUSB238 PD-sink controller
- Selectable VUSB profiles supported by the attached PD source
- TPS54302-based 3.3 V output rail
- Independent left and right breadboard-rail selection
- Screw-terminal and header outputs for VUSB, 3.3 V, and ground
- Qwiic-compatible I²C connectors for 3.3 V peripherals
- DIP-switch PD configuration and optional HUSB238 I²C access

The module is mechanically intended for common 54 mm and 64 mm breadboard
rail formats. Output voltage and available current depend on the negotiated PD
profile, source, cable, thermal conditions, and external load.
