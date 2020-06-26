#import stuff
#make sure you are in enviernemnt:
#workon cv
from live_detect_fingers import Rock_Paper_Sissors_App
from imutils.video import VideoStream
import argparse


ap = argparse.ArgumentParser()
ap.add_argument("-n", "--num-frames", type=int, default=100, help="num frames for test")
ap.add_argument("-d", "--display", type=int, default=-1, help="should frames be displayed?")
args = vars(ap.parse_args())

vs = VideoStream(src=0).start() #used for multithreading

app = Rock_Paper_Sissors_App(vs)
app.window.title('Rock Paper Scissors')
app.window.mainloop()


