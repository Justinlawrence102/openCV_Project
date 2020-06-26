#import stuff
#make sure you are in enviernemnt:
#workon cv
from imutils.video import WebcamVideoStream
from imutils.video import FPS
from getHand import getFingerCount
from PIL import Image
from PIL import ImageTk

import tkinter as tk #used for GUI
import threading
import imutils  #convience functions
import argparse
import cv2      # embed OpenCV 4

class Rock_Paper_Sissors_App:

	def __init__(self, vs):
		self.vs = vs
		self.thread = None
		self.window = tk.Tk()

		#init window
		startButton = tk.Button(text="Start", width=25, height=5, fg="green")
		startButton.bind("<Button-1>", self.did_press_start)
		startButton.pack()

		image = Image.open('ball.png')
		image = image.resize((600, 600))
		image = ImageTk.PhotoImage(image)

		self.imageView = tk.Label(image=image)
		self.imageView.image = image
		self.imageView.pack(side="left", padx=10, pady=10)

		#prepare threading
		self.thread = threading.Thread(target=self.getVideo, args=())
		self.thread.start()


	def getVideo(self):
		while(True):
			frame = self.vs.read()
			frame = imutils.resize(frame, height = 300)	#600
			cv2.rectangle(frame,(50,50),(210,210),(0,255,0),0)	#(100,100),(420,420)

			image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
			image = Image.fromarray(image)
			image = ImageTk.PhotoImage(image)
			self.imageView.configure(image=image)
			self.imageView.image = image

	def did_press_start(self, event):
		counter = 0
		while counter < 100:
			frame = self.vs.read()
			getFingerCount(frame, False)
			counter += 1


