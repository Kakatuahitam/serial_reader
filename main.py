import serial

print("app launched")

with serial.Serial('/dev/ttyACM1') as ser:
    line = ser.readline()
    print(line.decode('utf-8'))

print("good bye")
