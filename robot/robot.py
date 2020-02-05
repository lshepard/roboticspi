from adafruit_motorkit import MotorKit
from picamera import PiCamera
from io import BytesIO
from PIL import Image
import numpy as np
from time import sleep
from picamera.streams import PiCameraCircularIO
from picamera.array import PiRGBArray
import keyboard

kit = MotorKit()

class Key():
    def __init__(self):
        self.key = None
        
    def set(self, k):
        self.key = k
    
current_key = Key()

def onkey(event):
    """Write the currently pressed key to global var for interpretation in the event loop"""
    if event.event_type == "up":
        current_key.set(None)
    elif event.event_type == "down":
        current_key.set(event.name)

keyboard.hook(onkey)        
        


def motors(right, left):
    kit.motor1.throttle = right
    kit.motor3.throttle = right
    
    kit.motor2.throttle = left
    kit.motor4.throttle = left
    
def straight(speed):
    kit.motor1.throttle = speed
    kit.motor2.throttle = speed
    kit.motor3.throttle = speed
    kit.motor4.throttle = speed

def turn_right(speed):
    """Determines motor speed based on the input."""

    kit.motor1.throttle = speed 
    kit.motor3.throttle = speed 
    kit.motor1.throttle = -1 * speed
    kit.motor3.throttle = -1 * speed

def setup_camera():
    camera = PiCamera()
    camera.framerate = 24
    camera.resolution = (RESOLUTION_x,RESOLUTION_y)
    return camera
    sleep(2)

RESOLUTION_x = 320
RESOLUTION_y = 240
THRESHOLD = 5

def current_green(camera, stream):
    """Get the current average green value"""
    frame = b''
    while len(frame) == 0:
        #frameinfo = next(iter(stream.frames), None)
        frame = stream.getvalue()
        print("waiting")
        camera.wait_recording(.1)
        eval_keyboard()
        
    print(f"frame found {frame[:100]}")

        # capture directly, not from stream
        #        
        #        camera.capture(frame,'rgb')
        
    return green(frame)
    
def green(x):
    """Take the average value of the green channel minus the red channel"""
    
    return np.mean(np.mean(x[:,:,1].astype(int) - x[:,:,0].astype(int), axis=1))


def keyboard_loop():
    speed = 0.0
    direction = 0.5
    
    while True:
        eval_keyboard()
        
def eval_keyboard():
        k = current_key.key
        if k is None:
            return False
            #print("none")
        else:
            # If there's a key pressed, then that overrides
            if k == "up":
                motors(1,1)
            elif k == "down":
                motors(-1,-1)
            elif k == "right":
                motors(-1,1)
            elif k == "left":
                motors(1,-1)
            elif k == "space":
                motors(0,0)
            elif k == "g":
                monitor_green()
            return True
        # now go
            
            
if __name__ == "__main__":
    # start the keyboard loop at the top
    keyboard_loop()
