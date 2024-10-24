import sys
import time
import datetime
import tm1637
import RPi.GPIO as GP


display=tm1637.tm1637(23,24,tm1637.BRIGHT_TYPICAL)
display.Clear()
display.SetBrightnes(1)

while True:
    now=datetime.datetime.now()
    hour=now.hour
    miutes=now.minute
    second=now.second
    currentTime=[int(hour/10),hour%10,int(minute/10),minute%10]
    display.Show(currentTime)
    display.ShowDoublepoint(second%2)
    time.sleep(1)