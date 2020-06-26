#import stuff
#make sure you are in enviernemnt:
#workon cv

import imutils  #convience functions
import argparse
import numpy as np
import cv2      # embed OpenCV 4

def getFingerCount(image, showImage):
    kernel = np.ones((3,3), np.uint8)
    #load image
    image = imutils.resize(image, height=600)
    roi = image[100:420, 100:420]

  #  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
   # gray = cv2.GaussianBlur(gray, (15, 15), 0)
    hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

   #define skin tones
    lower_skin = np.array([0, 20, 70], dtype=np.uint8)
    upper_skin = np.array([20, 255, 255], dtype=np.uint8)
    #extract skin color
    mask = cv2.inRange(hsv, lower_skin, upper_skin) 

    #blur and expand to remove small imprefections
    #mask = cv2.dilate(mask, kernel, iterations=3) this made it inconsitent 
    mask = cv2.GaussianBlur(mask, (5, 5,), 100)
   # cv2.imshow("image", mask)
    #cv2.waitKey(0)

    #edged = cv2.Canny(gray, 50, 150)
    #thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)[1]


    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    handCnt = None

    if cnts:    #makes sure that cnts isnt empty...this happens on the first frame of the video for some reason
        handCnt = max(cnts, key=cv2.contourArea) #get the largest contour from the image
        approx = cv2.approxPolyDP(handCnt, 0.003 * cv2.arcLength(handCnt, True), True) # 0.002 works well
        #this reduses the polygons to make it shorter lines
        sortedPnts = sorted(approx, key =cv2.contourArea, reverse=False)

        numPnts = 0
        prevHeight = 600
        prevWidth = 600 #this is used to add dots to the iamge
        onTheRise = False

        for c in sortedPnts:
            cHeight = c[0][1]
            if onTheRise and cHeight > prevHeight+10:
              onTheRise = False
              numPnts += 1
              tempTuple = (prevWidth, prevHeight)
              cv2.circle(image, tempTuple, 8, (0, 0, 255), -1)

            if cHeight < prevHeight-30:
                #this means that the previous point was lower (bc 0 is at the top and 600 is at the bottom)
              onTheRise = True

            prevHeight = cHeight
            prevWidth = c[0][0]
            #print(c[0][1])

        #print("This many points: "+str(numPnts))
        if numPnts == 0 or numPnts == 1:
            print("ROCK")
        elif numPnts == 2:
            print("SISSORS")
        elif numPnts == 3 or numPnts == 4 or numPnts == 5 or numPnts ==6: 
            print("PAPER")

    #draw on the the shape to put these coordinates!
        cv2.drawContours(image, [approx], -1, (0, 255, 255), 2)
        if showImage:
            cv2.imshow("image", image)
            key = cv2.waitKey(1) & 0xFF
            #cv2.waitKey(0)


