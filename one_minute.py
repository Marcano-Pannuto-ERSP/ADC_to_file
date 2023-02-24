import serial
import time
import sys

def format_output(s):
    s = s.replace("'", "")
    s = s.replace("b", "")
    s = s.replace("\\r\\n", "\n")
    return s

def one_minute():
    ser = serial.Serial('/dev/ttyUSB0', 115200)  # open serial port
    currentTime = time.monotonic()
    finalTime = currentTime + 60		# one minute
    fileName = sys.argv[1]
    f = open(fileName, "x")
    
    while(currentTime < finalTime):
        x = ser.read_until(expected=b"\r\n")
        print(x)
        s = format_output(str(x))
        print(s)
        f.write(s)
        currentTime = time.monotonic()
    f.close()
    ser.close()

one_minute()
