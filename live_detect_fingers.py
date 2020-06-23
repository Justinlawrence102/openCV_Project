#import stuff
#make sure you are in enviernemnt:
#workon cv
from imutils.video import WebcamVideoStream
from imutils.video import FPS
from getHand import getFingerCount

import imutils  #convience functions
import argparse
import cv2      # embed OpenCV 4


ap = argparse.ArgumentParser()
ap.add_argument("-n", "--num-frames", type=int, default=100, help="num frames for test")
ap.add_argument("-d", "--display", type=int, default=-1, help="should frames be displayed?")
args = vars(ap.parse_args())

vs = WebcamVideoStream(src=0).start()   #used for multithreading
fps = FPS().start()


while fps._numFrames < args["num_frames"]:
    frame = vs.read()                   #usef for multithreading
    image = imutils.resize(frame, height=600)
    #defines the region of interest
    roi = image[100:420, 100:420]
    cv2.rectangle(image,(100,100),(420,420),(0,255,0),0)   
    getFingerCount(image)
    fps.update()

fps.stop()
vs.stop()                #used for multithreading
cv2.destroyAllWindows()



