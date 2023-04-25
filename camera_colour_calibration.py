












# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 10:39:49 2023

@author: Francisco
"""

import cv2
import sys
import numpy as np
import pyrealsense2 as rs


def nothing(x):
    pass

#image = cv2.imread('1.jpg')

# Create a window
cv2.namedWindow('image')

# create trackbars for color change
cv2.createTrackbar('HMin','image',0,179,nothing) # Hue is from 0-179 for Opencv
cv2.createTrackbar('SMin','image',0,255,nothing)
cv2.createTrackbar('VMin','image',0,255,nothing)
cv2.createTrackbar('HMax','image',0,179,nothing)
cv2.createTrackbar('SMax','image',0,255,nothing)
cv2.createTrackbar('VMax','image',0,255,nothing)

# Set default value for MAX HSV trackbars.
cv2.setTrackbarPos('HMax', 'image', 179)
cv2.setTrackbarPos('SMax', 'image', 255)
cv2.setTrackbarPos('VMax', 'image', 255)

# Initialize to check if HSV min/max value changes
hMin = sMin = vMin = hMax = sMax = vMax = 0
phMin = psMin = pvMin = phMax = psMax = pvMax = 0

#output = image
wait_time = 33


found_rgb = False

x, y, w, h = 85, 140, 300, 320
x, y, w, h = 0, 0, 300, 320
cap = cv2.VideoCapture(0)
time=0
if not cap.isOpened():
    rospy.logerr("Cannot open camera")
    exit()
ret, color_image = cap.read()
color_image_rgb=np.asanyarray(color_image)[x:x+w, y:y+h]
color_image= cv2.bitwise_not(color_image_rgb)

try:
    while True:

        # Wait for a coherent pair of frames: depth and color
        
        #color_image = np.asanyarray(color_frame.get_data())[x:x+w, y:y+h]
        
        hsv = cv2.cvtColor(color_image, cv2.COLOR_BGR2HSV)
        lower = np.array([0,0,122])
        upper = np.array([179,255,255])
        mask = cv2.inRange(hsv, lower, upper)
        color_image = cv2.bitwise_and(color_image, color_image, mask = mask)

        # Apply colormap on depth image (image must be converted to 8-bit per pixel first)
        #depth_colormap = cv2.applyColorMap(cv2.convertScaleAbs(depth_image, alpha=0.03), cv2.COLORMAP_JET)

       # depth_colormap_dim = depth_colormap.shape
        #color_colormap_dim = color_image.shape

        
        # get current positions of all trackbars
        hMin = cv2.getTrackbarPos('HMin','image')
        sMin = cv2.getTrackbarPos('SMin','image')
        vMin = cv2.getTrackbarPos('VMin','image')

        hMax = cv2.getTrackbarPos('HMax','image')
        sMax = cv2.getTrackbarPos('SMax','image')
        vMax = cv2.getTrackbarPos('VMax','image')

        # Set minimum and max HSV values to display
        lower = np.array([hMin, sMin, vMin])
        upper = np.array([hMax, sMax, vMax])

        # Create HSV Image and threshold into a range.
        hsv = cv2.cvtColor(color_image, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, lower, upper)
        output = cv2.bitwise_and(color_image,color_image, mask= mask)

        # Print if there is a change in HSV value
        if( (phMin != hMin) | (psMin != sMin) | (pvMin != vMin) | (phMax != hMax) | (psMax != sMax) | (pvMax != vMax) ):
            print("(hMin = %d , sMin = %d, vMin = %d), (hMax = %d , sMax = %d, vMax = %d)" % (hMin , sMin , vMin, hMax, sMax , vMax))
            phMin = hMin
            psMin = sMin
            pvMin = vMin
            phMax = hMax
            psMax = sMax
            pvMax = vMax

        # Display output image
        #output=color_image
        cv2.imshow('image',output)

        # Wait longer to prevent freeze for videos.
        if cv2.waitKey(wait_time) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()
        
        # If depth and color resolutions are different, resize color image to match depth image for display
        #if depth_colormap_dim != color_colormap_dim:
        #    resized_color_image = cv2.resize(color_image, dsize=(depth_colormap_dim[1], depth_colormap_dim[0]), interpolation=cv2.INTER_AREA)
        #    images = np.hstack((resized_color_image, depth_colormap))
        #else:
        #    images = np.hstack((color_image, depth_colormap))#

        # Show images
        #cv2.namedWindow('RealSense', cv2.WINDOW_AUTOSIZE)
        #cv2.imshow('RealSense', images)
        #cv2.waitKey(1)

finally:

    # Stop streaming
    cv2.destroyAllWindows()
    #pipeline.stop()
