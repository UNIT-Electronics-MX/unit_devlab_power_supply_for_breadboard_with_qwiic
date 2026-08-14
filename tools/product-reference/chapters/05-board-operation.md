## **5 Board Operation**

### **5.1 Initial Power-Up** {.section-page}

1. With USB-C disconnected, set both breadboard-rail selectors to `OFF`.
2. Insert the module in the intended breadboard position and inspect that each
   header aligns with the intended power rail.
3. Connect a compatible USB-C PD source and cable.
4. Confirm the negotiated VUSB profile before connecting a load.
5. Set each rail independently to `VUSB`, `3V3`, or leave it `OFF`.
6. Verify voltage and polarity with a meter before connecting sensitive or
   high-current circuitry.

### **5.2 Standalone PD Selection** {.section-page}

The onboard DIP switch configures the HUSB238 request when no external I²C
controller overrides it. Use only profiles supported by the connected source.
An unavailable request must not be assumed to result in the selected voltage;
measure VUSB before use.

### **5.3 I²C Monitoring with Arduino** {.section-page}

When the optional HUSB238-to-Qwiic connections are enabled, an external
3.3 V microcontroller can access the controller through I²C. The released
example uses an ESP32-compatible controller with SDA on GPIO6, SCL on GPIO7,
and the default HUSB238 address `0x08`.

Install the `Adafruit_HUSB238` library and use the supplied example:

`software/examples/cpp_examples/husb238_detection_only/husb238_detection_only.ino`

The example initializes I²C, detects the HUSB238, and reports the PD profiles
advertised by the attached source. It is a detection example; it does not
validate the connected load or replace a voltage measurement.

### **5.4 Operational Precautions** {.section-page}

- Do not change rail jumpers while the module is powered.
- Keep the VUSB rail isolated from 3.3 V-only devices and I²C signals.
- Use a cable and PD source rated for the requested voltage and expected load.
- The maximum usable output current is installation-dependent; respect source,
  cable, regulator, thermal, breadboard, and connected-device limits.
- For a 3.3 V load, prefer a 9 V or higher PD input profile as documented in
  the electrical notes.
