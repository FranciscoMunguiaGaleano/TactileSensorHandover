# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 18:08:53 2023

@author: Francisco
"""

import cv2
import math
from PIL import ImageTk, Image 


SENSIBILITY_ALPHA=0.01
SENSIBILITY_BETA=15


ARDUINO_PORT='COM7'
GRIPPER_PORT='COM4'
MIN_PREASSURE=0.0
MAX_PREASSURE=1.2
MAX_GRIPPER=5
MIN_GRIPPER=255

SENSOR_CAM_ID=1
USER_VIEW_CAM_ID=0

X_OFFSET=85
Y_OFFSET=140
WIDTH_SCREEN=300
HEIGHT_SCREEN=320
WIDHT_PLOT=300
HEIGHT_PLOT=640
QUEUE_LENGHT=500

POINT_TIME = 50

RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
BLUE_GREEN=(255, 0, 255)
YELLOW=(255,255,0)

MIN_AREA=50





OPTIONS = [
"Experiment_1",
"Experiment_2",
"Experiment_3",
"Experiment_4",
"Experiment_5",
"Experiment_6",
"Experiment_7",
"Experiment_8",
"Experiment_9",
"Experiment_10",
]

OPTIONS_OBJECTS = [
"Paper",
"Fabrics",
"Cup",
"Dough",
"Strawberry",
"Raspberry",
"USB_cable",
"Prism",
]

OPENING_OBJECTS = {
'Paper':230,
'Fabrics':220,
'Cup':120,
'Dough':150,
'Strawberry':160,
'Raspberry':180,
'USB_cable':230,
'Prism':200,
}



OPTIONS_PARAMETERS=['S1_P1','S1_P2','S1_P3','S2_P1','S2_P2','S2_P3','S3_P1','S3_P2','S3_P3']

EXPERIMENTAL_SETUPS={'S1_P1':[0.01,0.8],
                     'S1_P2':[0.01,1.0],
                     'S1_P3':[0.01,1.3],
                     'S2_P1':[0.005,0.8],
                     'S2_P2':[0.005,1.0],
                     'S2_P3':[0.005,1.3],
                     'S3_P1':[0.001,0.8],
                     'S3_P2':[0.001,1.0],
                     'S3_P3':[0.001,1.3]}

EXPERIMENTAL_SETUPS_NUM=[[0.0,0.0],
                     [0.01,0.8],
                     [0.01,1.0],
                     [0.01,1.3],
                     [0.005,0.8],
                     [0.005,1.0],
                     [0.005,1.3],
                     [0.001,0.8],
                     [0.001,1.0],
                     [0.001,1.3]]

e1=[2, 4, 6, 8, 5, 3, 1, 7, 9]
e2=[8, 4, 5, 9, 6, 3, 1, 7, 2]
e3=[2, 3, 6, 5, 9, 1, 7, 8, 4]
e4=[6, 2, 4, 9, 1, 8, 7, 3, 5]
e5=[7, 3, 2, 9, 6, 5, 4, 1, 8]
e6=[4, 5, 3, 7, 8, 2, 6, 9, 1]
e7=[5, 6, 2, 7, 3, 8, 4, 1, 9]
e8=[7, 9, 3, 8, 4, 5, 6, 2, 1]
e9=[7, 5, 8, 4, 1, 2, 6, 9, 3]
e10=[4, 3, 8, 6, 2, 7, 9, 1, 5]

experiment_dict={'Experiment_1':[[2, 4, 6, 8, 5, 3, 1, 7, 9],[['Raspberry', 'USB_cable', 'Dough', 'Cup', 'Paper', 'Strawberry', 'Fabrics', 'Prism'],
['Dough', 'Raspberry', 'USB_cable', 'Prism', 'Strawberry', 'Fabrics', 'Paper', 'Cup'],
['USB_cable', 'Cup', 'Paper', 'Raspberry', 'Dough', 'Strawberry', 'Prism', 'Fabrics'],
['Prism', 'Paper', 'Cup', 'USB_cable', 'Raspberry', 'Dough', 'Fabrics', 'Strawberry'],
['Paper', 'Fabrics', 'USB_cable', 'Dough', 'Raspberry', 'Cup', 'Prism', 'Strawberry'],
['Strawberry', 'Raspberry', 'Fabrics', 'Dough', 'USB_cable', 'Paper', 'Prism', 'Cup'],
['Raspberry', 'USB_cable', 'Prism', 'Cup', 'Fabrics', 'Paper', 'Dough', 'Strawberry'],
['Raspberry', 'Paper', 'Strawberry', 'Prism', 'USB_cable', 'Fabrics', 'Cup', 'Dough'],
['Prism', 'Raspberry', 'Cup', 'Fabrics', 'Strawberry', 'Paper', 'USB_cable', 'Dough']]],
'Experiment_2':[[8, 4, 5, 9, 6, 3, 1, 7, 2],[['Paper', 'Cup', 'Strawberry', 'Dough', 'Prism', 'Raspberry', 'USB_cable', 'Fabrics'],
['Raspberry', 'Paper', 'Strawberry', 'Cup', 'Prism', 'USB_cable', 'Dough', 'Fabrics'],
['Fabrics', 'USB_cable', 'Cup', 'Paper', 'Raspberry', 'Prism', 'Strawberry', 'Dough'],
['Fabrics', 'Raspberry', 'Prism', 'Dough', 'Strawberry', 'Paper', 'Cup', 'USB_cable'],
['Raspberry', 'Paper', 'Fabrics', 'Prism', 'USB_cable', 'Strawberry', 'Dough', 'Cup'],
['Fabrics', 'Cup', 'Dough', 'Strawberry', 'Raspberry', 'Paper', 'USB_cable', 'Prism'],
['Prism', 'Fabrics', 'Raspberry', 'Paper', 'Cup', 'Dough', 'Strawberry', 'USB_cable'],
['Fabrics', 'Dough', 'Prism', 'Raspberry', 'Cup', 'Paper', 'Strawberry', 'USB_cable'],
['Strawberry', 'Cup', 'Prism', 'Raspberry', 'Paper', 'USB_cable', 'Fabrics', 'Dough']]],
'Experiment_3':[[2, 3, 6, 5, 9, 1, 7, 8, 4],[['Paper', 'Cup', 'Prism', 'Dough', 'Raspberry', 'USB_cable', 'Strawberry', 'Fabrics'],
['Prism', 'Paper', 'Strawberry', 'Raspberry', 'USB_cable', 'Dough', 'Fabrics', 'Cup'],
['Fabrics', 'USB_cable', 'Strawberry', 'Paper', 'Prism', 'Cup', 'Dough', 'Raspberry'],
['Strawberry', 'Fabrics', 'USB_cable', 'Dough', 'Cup', 'Paper', 'Raspberry', 'Prism'],
['Strawberry', 'Dough', 'Prism', 'Paper', 'Fabrics', 'Cup', 'Raspberry', 'USB_cable'],
['Fabrics', 'USB_cable', 'Cup', 'Strawberry', 'Prism', 'Paper', 'Dough', 'Raspberry'],
['Dough', 'USB_cable', 'Paper', 'Prism', 'Cup', 'Fabrics', 'Strawberry', 'Raspberry'],
['Dough', 'Raspberry', 'Strawberry', 'Cup', 'Fabrics', 'USB_cable', 'Prism', 'Paper'],
['Cup', 'USB_cable', 'Strawberry', 'Raspberry', 'Prism', 'Dough', 'Paper', 'Fabrics']]],
'Experiment_4':[[6, 2, 4, 9, 1, 8, 7, 3, 5],[['Raspberry', 'USB_cable', 'Prism', 'Fabrics', 'Strawberry', 'Cup', 'Paper', 'Dough'],
['Cup', 'Prism', 'Fabrics', 'USB_cable', 'Raspberry', 'Strawberry', 'Paper', 'Dough'],
['Strawberry', 'Prism', 'Cup', 'USB_cable', 'Fabrics', 'Paper', 'Dough', 'Raspberry'],
['Paper', 'Strawberry', 'Fabrics', 'Dough', 'Cup', 'USB_cable', 'Raspberry', 'Prism'],
['Strawberry', 'Prism', 'Raspberry', 'USB_cable', 'Cup', 'Dough', 'Fabrics', 'Paper'],
['Fabrics', 'Paper', 'Cup', 'USB_cable', 'Raspberry', 'Strawberry', 'Dough', 'Prism'],
['USB_cable', 'Dough', 'Cup', 'Fabrics', 'Raspberry', 'Strawberry', 'Prism', 'Paper'],
['Dough', 'Strawberry', 'Cup', 'Paper', 'USB_cable', 'Prism', 'Raspberry', 'Fabrics'],
['Dough', 'USB_cable', 'Cup', 'Prism', 'Raspberry', 'Paper', 'Strawberry', 'Fabrics']]],
'Experiment_5':[[7, 3, 2, 9, 6, 5, 4, 1, 8],[['USB_cable', 'Prism', 'Raspberry', 'Dough', 'Paper', 'Fabrics', 'Strawberry', 'Cup'],
['USB_cable', 'Paper', 'Prism', 'Strawberry', 'Dough', 'Cup', 'Raspberry', 'Fabrics'],
['Strawberry', 'Dough', 'USB_cable', 'Paper', 'Cup', 'Fabrics', 'Prism', 'Raspberry'],
['Cup', 'Raspberry', 'USB_cable', 'Paper', 'Fabrics', 'Strawberry', 'Dough', 'Prism'],
['Paper', 'USB_cable', 'Dough', 'Fabrics', 'Prism', 'Strawberry', 'Cup', 'Raspberry'],
['Fabrics', 'Paper', 'Dough', 'Raspberry', 'Cup', 'Prism', 'Strawberry', 'USB_cable'],
['Paper', 'USB_cable', 'Raspberry', 'Cup', 'Prism', 'Dough', 'Strawberry', 'Fabrics'],
['Strawberry', 'Paper', 'Dough', 'USB_cable', 'Raspberry', 'Cup', 'Prism', 'Fabrics'],
['Fabrics', 'USB_cable', 'Paper', 'Strawberry', 'Raspberry', 'Prism', 'Cup', 'Dough']]],
'Experiment_6':[[4, 5, 3, 7, 8, 2, 6, 9, 1],[['Strawberry', 'Paper', 'Cup', 'Prism', 'USB_cable', 'Raspberry', 'Fabrics', 'Dough'],
['Dough', 'Paper', 'Strawberry', 'Raspberry', 'Fabrics', 'USB_cable', 'Prism', 'Cup'],
['Paper', 'Strawberry', 'Cup', 'Raspberry', 'Fabrics', 'USB_cable', 'Prism', 'Dough'],
['Raspberry', 'Dough', 'Cup', 'Paper', 'USB_cable', 'Fabrics', 'Strawberry', 'Prism'],
['Raspberry', 'Prism', 'USB_cable', 'Cup', 'Strawberry', 'Fabrics', 'Paper', 'Dough'],
['Raspberry', 'Dough', 'Paper', 'Cup', 'USB_cable', 'Fabrics', 'Strawberry', 'Prism'],
['Cup', 'Dough', 'USB_cable', 'Raspberry', 'Prism', 'Fabrics', 'Strawberry', 'Paper'],
['Prism', 'USB_cable', 'Raspberry', 'Cup', 'Fabrics', 'Strawberry', 'Dough', 'Paper'],
['Fabrics', 'Cup', 'Prism', 'Paper', 'Strawberry', 'USB_cable', 'Raspberry', 'Dough']]],
'Experiment_7':[[5, 6, 2, 7, 3, 8, 4, 1, 9],[['Fabrics', 'Dough', 'Paper', 'Cup', 'Prism', 'Strawberry', 'Raspberry', 'USB_cable'],
['Fabrics', 'Prism', 'Paper', 'Dough', 'USB_cable', 'Cup', 'Raspberry', 'Strawberry'],
['Dough', 'USB_cable', 'Prism', 'Strawberry', 'Fabrics', 'Cup', 'Raspberry', 'Paper'],
['Raspberry', 'Fabrics', 'Strawberry', 'Dough', 'Prism', 'Paper', 'Cup', 'USB_cable'],
['Dough', 'Fabrics', 'Paper', 'Cup', 'Raspberry', 'Strawberry', 'Prism', 'USB_cable'],
['Prism', 'Paper', 'Fabrics', 'Dough', 'Raspberry', 'USB_cable', 'Cup', 'Strawberry'],
['Cup', 'Strawberry', 'Dough', 'Raspberry', 'Paper', 'Prism', 'Fabrics', 'USB_cable'],
['Dough', 'Prism', 'Strawberry', 'Paper', 'Cup', 'USB_cable', 'Raspberry', 'Fabrics'],
['Dough', 'USB_cable', 'Raspberry', 'Strawberry', 'Paper', 'Fabrics', 'Prism', 'Cup']]],
'Experiment_8':[[7, 9, 3, 8, 4, 5, 6, 2, 1],[['Cup', 'Raspberry', 'Dough', 'Prism', 'Strawberry', 'Paper', 'USB_cable', 'Fabrics'],
['Prism', 'Strawberry', 'Paper', 'Cup', 'Raspberry', 'Dough', 'USB_cable', 'Fabrics'],
['Paper', 'Strawberry', 'Dough', 'Raspberry', 'USB_cable', 'Prism', 'Fabrics', 'Cup'],
['Cup', 'Paper', 'Raspberry', 'Strawberry', 'Prism', 'Dough', 'Fabrics', 'USB_cable'],
['Dough', 'Cup', 'Raspberry', 'Strawberry', 'Fabrics', 'USB_cable', 'Prism', 'Paper'],
['USB_cable', 'Dough', 'Cup', 'Prism', 'Raspberry', 'Strawberry', 'Paper', 'Fabrics'],
['Strawberry', 'Fabrics', 'Prism', 'Paper', 'Dough', 'USB_cable', 'Raspberry', 'Cup'],
['Paper', 'Raspberry', 'Cup', 'Strawberry', 'Dough', 'USB_cable', 'Prism', 'Fabrics'],
['Paper', 'Cup', 'Strawberry', 'Prism', 'USB_cable', 'Fabrics', 'Dough', 'Raspberry']]],
'Experiment_9':[[7, 5, 8, 4, 1, 2, 6, 9, 3],[['Prism', 'Cup', 'Dough', 'Raspberry', 'Paper', 'Strawberry', 'Fabrics', 'USB_cable'],
['USB_cable', 'Raspberry', 'Dough', 'Prism', 'Paper', 'Cup', 'Strawberry', 'Fabrics'],
['Prism', 'Paper', 'Fabrics', 'Strawberry', 'USB_cable', 'Raspberry', 'Cup', 'Dough'],
['Cup', 'Raspberry', 'Fabrics', 'Paper', 'Prism', 'Dough', 'USB_cable', 'Strawberry'],
['Strawberry', 'Fabrics', 'Prism', 'Cup', 'Raspberry', 'USB_cable', 'Paper', 'Dough'],
['Strawberry', 'USB_cable', 'Dough', 'Prism', 'Paper', 'Cup', 'Raspberry', 'Fabrics'],
['Paper', 'Cup', 'Fabrics', 'Dough', 'Strawberry', 'Raspberry', 'USB_cable', 'Prism'],
['Cup', 'Strawberry', 'USB_cable', 'Dough', 'Prism', 'Paper', 'Fabrics', 'Raspberry'],
['Prism', 'Strawberry', 'USB_cable', 'Paper', 'Fabrics', 'Raspberry', 'Dough', 'Cup']]],
'Experiment_10':[[4, 3, 8, 6, 2, 7, 9, 1, 5],[['Dough', 'Fabrics', 'Paper', 'USB_cable', 'Prism', 'Strawberry', 'Raspberry', 'Cup'],
['Raspberry', 'Fabrics', 'Dough', 'Paper', 'Cup', 'USB_cable', 'Prism', 'Strawberry'],
['Dough', 'Paper', 'Cup', 'Strawberry', 'Fabrics', 'USB_cable', 'Raspberry', 'Prism'],
['Paper', 'Strawberry', 'USB_cable', 'Dough', 'Prism', 'Raspberry', 'Fabrics', 'Cup'],
['Paper', 'Strawberry', 'Dough', 'Fabrics', 'Prism', 'Cup', 'Raspberry', 'USB_cable'],
['Dough', 'Cup', 'Prism', 'Fabrics', 'Strawberry', 'USB_cable', 'Raspberry', 'Paper'],
['Paper', 'Cup', 'Fabrics', 'Strawberry', 'Raspberry', 'USB_cable', 'Prism', 'Dough'],
['Strawberry', 'Fabrics', 'Raspberry', 'Prism', 'Paper', 'Dough', 'Cup', 'USB_cable'],
['Raspberry', 'Dough', 'USB_cable', 'Strawberry', 'Fabrics', 'Cup', 'Paper', 'Prism']]]}

def tagger_init(img):
    center_init=[]
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    (thresh,gray) = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    types=""
    objective={}
    try:
        for c in cnts:
            area = cv2.contourArea(c)
            if area<MIN_AREA:
                #print(area)
                continue
            w=max([xmax[0][0] for xmax in c])-min([xmax[0][0] for xmax in c])
            l=max([xmax[0][1] for xmax in c])-min([xmax[0][1] for xmax in c])
            types=""
            M = cv2.moments(c)
            try:
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])
                center_init.append([cX,cY])
            except Exception as e:
                #print(e)
                pass
    except Exception as e:
        pass
        #print(e)
    return img,center_init

def tagger(img, center_initial):
    magnitude=0.0
    try:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        (thresh,gray) = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
        thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
        cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if len(cnts) == 2 else cnts[1]
        types=""
        objective={}
        #cv2.imshow('Dot Tracking',img)
        for c in cnts:
            area = cv2.contourArea(c)
            if area<MIN_AREA:
                #print(area)
                continue
            w=max([xmax[0][0] for xmax in c])-min([xmax[0][0] for xmax in c])
            l=max([xmax[0][1] for xmax in c])-min([xmax[0][1] for xmax in c])
            M = cv2.moments(c)
            try:
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])
                cv2.circle(img, (cX,cY), 2, RED, -1)
                cv2.line(img, (center_initial[0][0],center_initial[0][1]), (cX, cY), RED, 1)
                magnitude=math.sqrt((center_initial[0][0]-cX)**2+(center_initial[0][1]-cY)**2)
            except Exception as e:
                pass
                #print(e)
    except Exception as e:
        pass
        #print(e)
    return img,magnitude

def list_cameras():
    index = 0
    arr = []
    while True:
        cap = cv2.VideoCapture(index)
        if not cap.read()[0]:
            break
        else:
            arr.append(index)
        cap.release()
        index += 1
    return arr

def resize(img,scale):
    scale_percent = scale 
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    return cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

def object_list(exp,index):
    objects_list=experiment_dict[exp][1][index]
    return objects_list

def parameters_list(exp):
    params_list=[]
    for i in experiment_dict[exp][0]:
        params_list.append(OPTIONS_PARAMETERS[i-1])
    return params_list


#print(parameters_list('Experiment_1'))
#print(object_list('Experiment_1',0))