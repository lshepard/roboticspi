from adafruit_motorkit import MotorKit
from picamera import PiCamera
from io import BytesIO
from PIL import Image
import numpy as np
from time import sleep
from picamera.streams import PiCameraCircularIO
from picamera.array import PiRGBArray

kit = MotorKit()

def straight(speed):
    kit.motor1.throttle = speed
    kit.motor2.throttle = speed
    kit.motor3.throttle = speed
    kit.motor4.throttle = speed
    
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
#            camera.start_recording()
            frame = np.empty((RESOLUTION_y,RESOLUTION_x,3),dtype=np.uint8)
            for frame in camera.capture_continuous(frame, format="rgb"):#, use_video_port=True):
                g = green(frame)
                raw.truncate(0)
                print(g)
                if g > THRESHOLD:
                    straight(0)
                    sleep(1)
                    direction *= -1
                    
                    straight(direction)
        finally:
            camera.stop_recording()
