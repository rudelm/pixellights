import serial

ser = serial.Serial('/dev/ttyACM0', 19200)
ser.open()

ser.write("Hello World from Raspberry Pi".encode())

ser.close()