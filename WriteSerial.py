#!/usr/bin/env python
import serial

ser = serial.Serial(
    port='/dev/serial0',
    baudrate=19200,
    parity=serial.PARITY_NONE,
    timeout=1
)

ser.write("Hello World from Raspberry Pi".encode())

ser.close()