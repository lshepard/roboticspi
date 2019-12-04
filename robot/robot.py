from adafruit_motorkit import MotorKit
from picamera import PiCamera
from io import BytesIO
from PIL import Image
import numpy as np
from time import sleep

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

def current_green(camera_stream):
    """Get the current average green value"""
    with camera_stream.condition:
        camera_stream.condition.wait()
        frame = camera_stream.frame

        # capture directly, not from stream
        #        frame = np.empty((RESOLUTION_y,RESOLUTION_x,3),dtype=np.uint8)
        #        camera.capture(frame,'rgb')
        
        return green(frame)
    
def green(x):
    """Take the average value of the green channel minus the red channel"""
    
    return np.mean(np.mean(x[:,:,1].astype(int) - x[:,:,0].astype(int), axis=1))

class StreamingOutput(object):
    def __init__(self):
        self.frame = None
        self.buffer = io.BytesIO()
        self.condition = Condition()

    def write(self, buf):
        if buf.startswith(b'\xff\xd8'):
            # New frame, copy the existing buffer's content and notify all
            # clients it's available
            self.buffer.truncate()
            with self.condition:
                self.frame = self.buffer.getvalue()
                self.condition.notify_all()
            self.buffer.seek(0)
        return self.buffer.write(buf)


def monitor_green():

    direction = .5
    with setup_camera() as camera:
        camera_stream = StreamingOutput()
        camera.start_recording(camera_stream, format="mjpeg")
        
        try:
            while(True):
                g = current_green(camera_stream)
                print(g)
                if g > THRESHOLD:
                    straight(0)
                    sleep(1)
                    direction *= -1
                    
                    straight(direction)
        finally:
            camera.stop_recording()
