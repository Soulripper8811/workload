# sudo reboot
# sudo apt-get install python-picamera
# sudo apt-get install python3-picamera
# sudo pip install picamera




import time
import picamera

camera=picamera.PiCamera()
camera.resolution=(1024,768)
camera.start_preview()
time.sleep(2)
camera.capture("path/images%s.jpg")
camera.stop_preview()
camera.close()