#import stuff
#make sure you are in enviernemnt:
#workon cv
import imutils  #convience functions
import argparse
import cv2      # embed OpenCV 4
from getHand import getFingerCount

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "Path to image")
args = vars(ap.parse_args())

#load image
image = cv2.imread(args["image"])
image = imutils.resize(image, height=600)
getFingerCount(image)
