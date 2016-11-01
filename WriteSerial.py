#!/usr/bin/env python
from serial import serial

ser = serial.Serial(
    port='/dev/ttyAMA0',
    baudrate=19200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_NONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)
ser.open()

ser.write("Hello World from Raspberry Pi".encode())

ser.close()