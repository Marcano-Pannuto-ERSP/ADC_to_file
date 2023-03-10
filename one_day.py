import serial
import time
import sys

def format_output(s):
    s = s.replace("'", "")
    s = s.replace("b", "")
    s = s.replace("\\r\\n", "\n")
    return s

def one_day():
    ser = serial.Serial('/dev/ttyUSB0', 115200)  # open serial port Linux
    #ser = serial.Serial('COM6', 115200) # open serial port Windows
    initialTime = time.monotonic()
    currentTime = time.monotonic()
    finalTime = currentTime + 86400 # one day
    fileName = sys.argv[1]
    f = open(fileName, "x")
    
    while(currentTime < finalTime):
        x = ser.read_until(expected=b"\r\n")
        s = format_output(str(x))
        currentTime = time.monotonic()
        f.write(s + "time elapsed = " + str(currentTime - initialTime) + "\n")
    f.close()
    ser.close()

one_day()
