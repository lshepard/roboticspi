###
# Sample code for activating and annotating basic camera
# From https://projects.raspberrypi.org/en/projects/getting-started-with-picamera/8
#
###

from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
camera.annotate_text = "The Machine That Eats A City"
sleep(5)
camera.capture("/home/pi/Desktop/image.jpg")
camera.stop_preview()

