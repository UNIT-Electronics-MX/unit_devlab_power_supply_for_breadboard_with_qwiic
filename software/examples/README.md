# Software examples

Each C++ sketch has its own directory whose name matches its main `.ino` file.
See the [software guide](../README.md) for dependencies, connection details,
configuration, and usage instructions.

```text
examples/
└── cpp_examples/
    └── husb238_detection_only/
        └── husb238_detection_only.ino
```

## C++: HUSB238 detection

The [`husb238_detection_only`](cpp_examples/husb238_detection_only/husb238_detection_only.ino)
sketch detects the module and prints the USB-C PD voltage profiles offered by
the attached source.

The example defaults to SDA pin `6` and SCL pin `7`. Change
`HUSB238_I2C_SDA` and `HUSB238_I2C_SCL` when using another controller.
