import serial
import time
import sys

def one_minute():
    ser = serial.Serial('/dev/ttyUSB0', 115200)  # open serial port
    currentTime = time.monotonic()
    finalTime = currentTime + 60
    fileName = sys.argv[1]
    f = open(fileName, "x")
    while(currentTime < finalTime):
        x = ser.read_until(expected=b"\r\n")
        f.write(x)
    f.close()
    ser.close()