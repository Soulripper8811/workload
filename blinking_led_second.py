import time
import RPi.GPIO as GP

GP.setmode(GP.BOARD)
GP.setup(7,GP.OUT)
GP.setup(13,GP.OUT)
GP.setup(15,GP.OUT)
GP.setup(11,GP.OUT)



while True:
    GP.output(7,GP.LOW)
    time.sleep(1)
    GP.output(11,GP.HIGH)
    time.sleep(1)
    GP.output(13,GP.LOW)
    time.sleep(1)
    GP.output(15,GP.HIGH)
    time.sleep(1)

print("Led is blinking")
GP.cleanup()