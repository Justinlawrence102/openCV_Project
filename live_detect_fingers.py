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
		title = tk.Label(text = "ROCK Paper Scissors", fg= "#800D02")
		title.config(font=("Arial Black", 44))
		title.pack()

		image = Image.open('ball.png')
		image = image.resize((600, 600))
		image = ImageTk.PhotoImage(image)
		self.imageView = tk.Label(height = 400, width = 250, bg ="#9CAAFF", image = image)
		self.imageView.pack(side="left", padx=10, pady=10)

		# frame2 = tk.Frame(master=self.window, width=250, bg="yellow")
		# frame2.pack(fill=tk.Y, side="left")
		emojes = tk.Label(text = "✋✊✌️")
		emojes.config(font=("Arial Black", 70))
		emojes.pack()

		rulesTitle = tk.Label(text = "Rules", anchor="e", justify="left")
		rulesTitle.config(font=("Arial Black", 26))
		rulesTitle.pack()

		rules = tk.Label(text = "Theses are the rules, you can play \nbest of 5 or best of 3. Rock beats \nscissors, scissors beats paper, and \npaper beats rock.", width=40, justify="left")
		rules.config(font=("Arial", 15))
		rules.pack()

		blankSpace = tk.Label(height = 6, width = 20, bg ="white")
		blankSpace.pack()

		startButton = tk.Label(self.window, text="Start", width=25, height=3, bg='red', fg='white')
		startButton.bind("<Button-1>", self.did_press_start)
		startButton.pack()






		#prepare threading
		self.thread = threading.Thread(target=self.getVideo, args=())
		self.thread.start()


	def getVideo(self):
		while(True):
			frame = self.vs.read()
			frame = imutils.resize(frame, height = 300)	#600
			cv2.rectangle(frame,(50,50),(210,210),(0,255,0),0)	#(100,100),(420,420)
			#frameCropped = frame[0:0, 150:150]
			frameCropped = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
			frameCropped = Image.fromarray(frameCropped)
			frameCropped = ImageTk.PhotoImage(frameCropped)
			self.imageView.configure(image=frameCropped)
			self.imageView.image = frameCropped

	def did_press_start(self, event):
		counter = 0
		while counter < 100:
			frame = self.vs.read()
			getFingerCount(frame, False)
			counter += 1


