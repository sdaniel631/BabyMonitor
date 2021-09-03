import cv2
from imutils.video import VideoStream
import imutils
import time
import numpy as np

class VideoCamera(object):
    # initialise the camera
    def __init__(self):
        self.vs = VideoStream(src=0).start()
        time.sleep(2.0)

    def __del__(self):
        self.vs.stop()

    # get a frame from the camera
    def get_frame(self):
        frame = self.vs.read()
        ret, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()