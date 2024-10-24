import time
import RPi.GPIO as GP
import time
import serial

def Read_Card():
    ser=serial.Serial("/dev/ttyUSB0")
    ser.baudrate=9600
    data=ser.read(12)
    ser.close()
    return data


try:
    while True:
        id=Read_Card()
        print(id)
        if id=="":
            print("access granted")
            time.sleep(2)
        else:
            print("access denied")
            time.sleep(2)
finally:
    GP.cleanup()