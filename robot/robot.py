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

current_key = None

def onkey(event):
    """Write the currently pressed key to global var for interpretation in the event loop"""
    if event.event_type == "up":
        current_key = None
    elif event.event_type == "down":
        current_key = event.name

        

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

def stop():
    straight(0)
    
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
        
    print(f"frame found {frame[:100]}")

        # capture directly, not from stream
        #        
        #        camera.capture(frame,'rgb')
        
    return green(frame)
    
def green(x):
    """Take the average value of the green channel minus the red channel"""
    
    return np.mean(np.mean(x[:,:,1].astype(int) - x[:,:,0].astype(int), axis=1))

def monitor_green():

    direction = .5
    with setup_camera() as camera:
        try: 
#            raw = PiRGBArray(camera, size=(RESOLUTION_x,RESOLUTION_y))
            camera.start_preview()
            frame = np.empty((RESOLUTION_y,RESOLUTION_x,3),dtype=np.uint8)
            for frame in camera.capture_continuous(frame, format="rgb", use_video_port=True):

                # This is the main event loop. We have a new green frame each time.
                
                g = green(frame)

                if current_key is not None:
                    # If there's a key pressed, then that overrides

                    if current_key == "up":
                        straight(1)
                    elif current_key == "down":
                        straight(-1)
                    elif current_key == "right":
                        turn_right(1)
                    elif current_key == "left":
                        turn_right(-1)
                    elif current_key == "space":
                        straight(0)
                    

                else:
                    # maybe handle the color?

                    #if g < THRESHOLD:
                    #    straight(direction)
                    #else:
                    #    stop()
                    #    return
                    
        finally:
            camera.stop_recording()
