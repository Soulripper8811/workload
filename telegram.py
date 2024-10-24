sudo apt-get update
sudo apt-get upgrade
sudo reboot
sudo apt-get install python-pip3
sudo pip3 install telepot
sudo reboot



import time
import datetime
import RPi.GPIO as GP
import telepot
import sys


GP.setmode(GP.BOARD)
GP.setwarning(False)
GP.setup(3,GP.OUT)

def on(pin):
    GP.output(pin,GP.HIGH)
    return
def off(pin):
    GP.output(pin,GP.LOW)
    return


def handle(msg):
    chat_id=msg["chat"]["id"]
    command=msg["text"]

    print('Got command: %s',command)
    if command=="/on":
        bot.sendMessage(chat_id,on(3))
    if command==="/of":
        bot.sendMessage(chat_id,off(3))


bot=telepot.Bot("token jo ho ga")
bot.message_loop(handle)
print("i am listing")

while True:
    try:
        time.sleep(1)
    except KeyboardInterrupt:
        print("program is interuppedted")
        GP.cleanup()
        exit()

