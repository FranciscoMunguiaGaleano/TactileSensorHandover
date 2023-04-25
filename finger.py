# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 10:43:15 2023

@author: Francisco
"""
import cv2
import sys
import numpy as np
import io
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import threading
from constants import *
import time as t


def get_img_from_fig(fig, dpi=180):
    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=dpi)
    buf.seek(0)
    img_arr = np.frombuffer(buf.getvalue(), dtype=np.uint8)
    buf.close()
    img = cv2.imdecode(img_arr, 1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    return img

class Finger():
    def __init__(self,gripper):
        #rospy.init_node('finger_sensor_node', anonymous=True)
        self.avg_time=0.0
        self.frames=0
        self.run_threads=True
        self.sensibility_alpha=SENSIBILITY_ALPHA
        self.sensibility_beta=SENSIBILITY_BETA
        self.center_initial=[]
        self.dot_tracking_img=np.zeros((WIDTH_SCREEN, HEIGHT_SCREEN, 3), dtype = np.uint8)
        self.rgb_image=np.zeros((WIDTH_SCREEN, HEIGHT_SCREEN, 3), dtype = np.uint8)
        self.plot_image=np.zeros((WIDHT_PLOT, HEIGHT_PLOT, 3), dtype = np.uint8)
        self.plot_image_large=None
        self.gripper=gripper
        self.gripper_open=False
        self.ready_to_handover=False
        self.magnitudes=[]
        self.gripper_states=[]
        self.gripper_state=0
        self.plotting=True
        self.ready_to_grasp=False
        self.start=False
        self.fig = Figure(figsize=(5, 4), dpi=100)
        self.camera = threading.Thread(target=self.init_camera_stream)
        self.camera.start()
        self.plotter = threading.Thread(target=self.plot)
        self.plotter.start()
        #self.image_finger_pub_1 = rospy.Publisher("/tactile_sensor_image_1", Image, queue_size=10)
        #self.image_finger_pub_2 = rospy.Publisher("/tactile_sensor_image_2", Image, queue_size=10)
        #self.br=CvBridge()
    def init_camera_stream(self):
        x, y, w, h = X_OFFSET, Y_OFFSET, WIDTH_SCREEN, HEIGHT_SCREEN
        cap = cv2.VideoCapture(SENSOR_CAM_ID)
        time=0
        self.magnitudes=[]
        magnitude=0.0
        change_counter=0
        if not cap.isOpened():
            print("Cannot open camera")
            sys.exit(0)
        try:
            #n=0
            while self.run_threads:
                #n+=1
                start = t.time()
                ret, color_image = cap.read()
                color_image_rgb=np.asanyarray(color_image)[x:x+w, y:y+h]
                self.rgb_image=color_image_rgb
                color_image= cv2.bitwise_not(color_image_rgb)
                gray = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)
                (thresh,gray) = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
                hsv = cv2.cvtColor(color_image, cv2.COLOR_BGR2HSV)
                lower = np.array([0,0,122])
                lower = np.array([0,0,155])
                upper = np.array([185,255,255])
                mask = cv2.inRange(hsv, lower, upper)
                hsv = cv2.cvtColor(color_image, cv2.COLOR_BGR2HSV)
                hMin = 0
                sMin = 0
                vMin = 190
                hMax = 179
                sMax =255
                vMax = 255
                lower = np.array([hMin, sMin, vMin])
                upper = np.array([hMax, sMax, vMax])
                mask = cv2.inRange(hsv, lower, upper)
                self.dot_tracking_img = cv2.bitwise_and(color_image,color_image, mask= mask)
                cv2.circle(self.dot_tracking_img, (int(w/2), int(h/2)), 240, (0,0,0), 200)
                magnitude_new=0.0
                if self.start:
                    if time<POINT_TIME:
                        self.ready_to_handover=False
                        self.ready_to_grasp=False
                        output,self.center_initial=tagger_init(self.dot_tracking_img)
                        time+=1
                    else:
                        self.ready_to_handover=True
                        self.ready_to_grasp=True
                        output,magnitude_new=tagger(self.dot_tracking_img,self.center_initial)
                else:
                    time=0
                    self.ready_to_grasp=False
                    magnitude=0.0
                    magnitude_new=0.0
                dev=abs(magnitude_new-magnitude)
                if dev<2.0:
                    dev=0.0
                    change_counter+=1
                    if change_counter==50:
                        if self.gripper_open:
                            self.gripper_state=2
                        else:
                            self.gripper_state=0
                        change_counter=0
                else:
                    self.gripper_state=1
                magnitude=magnitude_new
                if len(self.magnitudes)>QUEUE_LENGHT:
                    self.magnitudes.pop(0)
                    self.gripper_states.pop(0)
                self.magnitudes.append(dev)
                if len(self.magnitudes)>self.sensibility_beta:
                    #print(sum(self.magnitudes[-self.sensibility_beta:])/len(self.magnitudes))
                    if (sum(self.magnitudes[-self.sensibility_beta:])/len(self.magnitudes))>self.sensibility_alpha:
                        #self.gripper_state=2
                        if not self.gripper_open:
                            print("Open gripper")
                            self.gripper.move(10)
                        self.gripper_open=True
                        self.ready_to_grasp=False
                        self.ready_to_handover=False
                        
                self.gripper_states.append(self.gripper_state)
                end = t.time()
                self.avg_time=round((end-start)*1000.0,3)
        finally:
            self.plotting=False
        return
    def plot(self):
        while self.plotting:
            fig = plt.figure()
            fig.set_figwidth(17)
            ax = fig.add_subplot(111)
            ax.plot(self.magnitudes)
            ax.set_title("Tactile sensor dot traking")
            ax.set_ylim(bottom=-0.1)
            img=get_img_from_fig(fig)
            scale_percent = 30 
            width = int(img.shape[1] * scale_percent / 100)
            height = int(img.shape[0] * scale_percent / 100)
            dim = (width, height)
            self.plot_image_large=img.copy()
            image= cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
            for index in range(0,len(self.gripper_states)):
                x_i=int(145+index*1.29 - 2)
                y_i=int(35-2)
                x_f=int(145+index*1.29 + 2)
                y_f=int(35 +2)
                if self.gripper_states[index]==0:
                    cv2.rectangle(image, (x_i,y_i), (x_f,y_f), RED, -1)
                elif self.gripper_states[index]==1:
                    cv2.rectangle(image, (x_i,y_i), (x_f,y_f), YELLOW, -1)
                elif self.gripper_states[index]==2:
                    cv2.rectangle(image, (x_i,y_i), (x_f,y_f), GREEN, -1)
            image = cv2.putText(image, str(self.avg_time)+" ms", (5, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 2, cv2.LINE_AA)
            self.plot_image=image
            del fig
            del img
            del ax
        return