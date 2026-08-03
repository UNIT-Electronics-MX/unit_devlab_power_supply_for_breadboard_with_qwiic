/**
 * HUSB238 USB-C PD source detection C++ example.
 *
 * Detects the HUSB238 over I2C and prints the voltage profiles offered by
 * the connected USB-C PD source.
 */

#include <Wire.h>
#include <Adafruit_HUSB238.h>

// Change these values to match the I2C pins on the controller connected to
// the module. The defaults are suitable for UNIT Electronics RP2040 boards.
#ifndef HUSB238_I2C_SDA
#define HUSB238_I2C_SDA 6
#endif

#ifndef HUSB238_I2C_SCL
#define HUSB238_I2C_SCL 7
#endif

Adafruit_HUSB238 husb238;
bool husb238Ready = false;

void printDetectedVoltages() {
  bool anyVoltage = false;

  Serial.println("Available USB-C PD voltages:");

  if (husb238.isVoltageDetected(PD_SRC_5V)) {
    Serial.println("- 5 V");
    anyVoltage = true;
  }
  if (husb238.isVoltageDetected(PD_SRC_9V)) {
    Serial.println("- 9 V");
    anyVoltage = true;
  }
  if (husb238.isVoltageDetected(PD_SRC_12V)) {
    Serial.println("- 12 V");
    anyVoltage = true;
  }
  if (husb238.isVoltageDetected(PD_SRC_15V)) {
    Serial.println("- 15 V");
    anyVoltage = true;
  }
  if (husb238.isVoltageDetected(PD_SRC_18V)) {
    Serial.println("- 18 V");
    anyVoltage = true;
  }
  if (husb238.isVoltageDetected(PD_SRC_20V)) {
    Serial.println("- 20 V");
    anyVoltage = true;
  }

  if (!anyVoltage) {
    Serial.println("- No USB-C PD profile detected");
  }
}

void setup() {
  Serial.begin(115200);
  delay(1000);

  Wire.begin(HUSB238_I2C_SDA, HUSB238_I2C_SCL);
  delay(100);

  Serial.println("Initializing HUSB238...");
  husb238Ready = husb238.begin(HUSB238_I2CADDR_DEFAULT, &Wire);

  if (husb238Ready) {
    Serial.println("HUSB238 detected.");
  } else {
    Serial.println("HUSB238 not found. Check the I2C connection and pins.");
  }
}

void loop() {
  if (!husb238Ready) {
    delay(1000);
    return;
  }

  printDetectedVoltages();
  Serial.println();
  delay(1000);
}
