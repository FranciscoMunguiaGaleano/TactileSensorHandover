# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 17:48:29 2023

@author: Francisco
"""
import cv2
import numpy as np
import threading
import sys
from constants import *

class UsbCamera():
    def __init__(self):
        self.run_threads=True
        self.rgb_image=np.zeros((300, 320, 3), dtype = np.uint8)
        self.camera = threading.Thread(target=self.init_camera_stream)
        self.camera.start()
    def init_camera_stream(self):
        print("Streaming user view")
        x, y, w, h = X_OFFSET, Y_OFFSET, WIDTH_SCREEN, HEIGHT_SCREEN
        cap = cv2.VideoCapture(USER_VIEW_CAM_ID)
        if not cap.isOpened():
            #rospy.logerr("Cannot open camera")
            print("Cannot open camera")
            sys.exit(0)
        try:
            while self.run_threads:
                ret, color_image = cap.read()
                color_image_rgb=np.asanyarray(color_image)[x:x+w, y:y+h]
                self.rgb_image=color_image_rgb   
                #cv2.imshow('User view',self.rgb_image)

        finally:
            # Stop streaming
            cv2.destroyAllWindows()
        return