#!/usr/bin/env python
import serial

ser = serial.Serial(
    port='/dev/serial0',
    baudrate=19200,
    parity=serial.PARITY_NONE,
    timeout=1
)

ser.write("Hello World from Raspberry Pi".encode())

for i in enumerate(range(256), start=21):
    ser.write(bytes(i)

ser.close()