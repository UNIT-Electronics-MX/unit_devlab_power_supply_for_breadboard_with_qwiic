# Hardware

<div align="center">
<a href="./unit_schematic_v_1_0_0_ue0113_devlab_power_supply_for_breadboard_with_qwiic.pdf"><img src="resources/Schematics_icon.jpg?raw=false" width="200px"><br/>Schematic</a>
</div>

## Key Technical Specifications

<div align="center">

| **Parameter** |           **Description**            | **Min** | **Typ** | **Max** | **Unit** |
|:-------------:|:------------------------------------:|:-------:|:-------:|:-------:|:--------:|
|      Vin      | Input voltage to power on the module |    5    |    -    |   20    |    V     |
|      Vih      |   High-level input voltage for I2C   |   1.4   |    -    |   5.5   |    V     |
|      Vil      |   Low-level input voltage for I2C    |    -    |    -    |   0.4   |    V     |
|      Icc      |            Supply Current            |    -    |   3.1   |    -    |    mA    |
|     I3v3      |   3V3 Power Supply Output Current    |    -    |    -    |    2    |    A     |
 

</div>

* **Note:** Output voltages and currents may vary with the characteristics of the power supply

## Pinout

<div align="center">
    <a href="#"><img src="resources/unit_pinout_v_0_0_1_ue0094_icp10111_barometric_pressure_sensor_en.jpg" width="500px"><br/>Pinout</a>
    <br/>
    <br/>
    <br/>
    

| Pin Label | Function    | Notes                             |
|-----------|-------------|-----------------------------------|
| VCC       | Power Supply| 3.3V or 5V                       |
| GND       | Ground      | Common ground for all components  |

</div>

## Dimensions

<div align="center">
<a href="./resources/unit_dimension_v_1_0_0_ue0113_devlab_power_supply_for_breadboard_with_qwiic.png"><img src="./resources/unit_dimension_v_1_0_0_ue0113_devlab_power_supply_for_breadboard_with_qwiic.png" width="500px"><br/> Dimensions</a>
</div>

## Topology

<div align="center">
<a href="./resources/unit_topology_v_1_0_0_ue0113_devlab_power_supply_for_breadboard_with_qwiic.png"><img src="./resources/unit_topology_v_1_0_0_ue0113_devlab_power_supply_for_breadboard_with_qwiic.png" width="500px"><br/> Topology</a>
<br/>
<br/>
<br/>

| Ref.    | Description                                        |
|---------|----------------------------------------------------|
| J1      | USB Type-C Connector                               |
| L1      | Power On LED                                       |
| IC1     | HUSB238                                            |
| SW1     | Dip Switch for voltage selector                    |
| U1      | TPS54302 3.3V Regulator                            |
| J6      | Screw Terminal Block output for VUSB               |
| JP7     | Pin Header for 3V3 power supply                    |
| JP3     | Output voltage selector for the left side headers  |
| JP4     | Output voltage selector for the right side headers |
| JP1-JP2 | Left side output voltage headers for breadboard    |
| JP5-JP6 | Right side output voltage headers for breadboard   |

</div>

## Pin & Connector Layout
| Pin   | Voltage Level | Function                                                  |
|-------|---------------|-----------------------------------------------------------|
| VCC   | 3.3 V – 5.5 V | Provides power to the on-board regulator and sensor core. |
| GND   | 0 V           | Common reference for power and signals.                   |
| SDA   | 1.8 V to VCC  | Serial data line for I²C communications.                  |
| SCL   | 1.8 V to VCC  | Serial clock line for I²C communications.                 |

> **Note:** The module also includes a Qwiic/STEMMA QT connector carrying the same four signals (VCC, GND, SDA, SCL) for effortless daisy-chaining.

# References

- <a href="./resources/unit_datasheet_v_1_0_0_ue0113_husb238.pdf">HUSB238 Datasheet </a>
- <a href="./resources/unit_datasheet_v_1_0_0_ue0113_tps54302.pdf">TPS54302 Datasheet </a>
