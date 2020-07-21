import tkinter as tk             
from PIL import Image
from PIL import ImageTk
from imutils.video import VideoStream
from getHand import getFingerCount
from playerClass import Player

import threading
import imutils  #convience functions
import cv2      # embed OpenCV 4
from enum import Enum
import random
from collections import Counter

#import Tkinter as tk     # python 2
#import tkFont as tkfont  # python 2

class gameView(tk.Frame):
    
    def __init__(self, parent, controller, vs, gameLength):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.vs = vs
        self.gameLength = gameLength
        compName = tk.StringVar()
        compRound1 = tk.StringVar()
        compRound2 = tk.StringVar()
        compRound3 = tk.StringVar()
        compRound4 = tk.StringVar()
        compRound5 = tk.StringVar()
        playerName = tk.StringVar()
        playerRound1 = tk.StringVar()
        playerRound2 = tk.StringVar()
        playerRound3 = tk.StringVar()
        playerRound4 = tk.StringVar()
        playerRound5 = tk.StringVar()
        game1Title = tk.StringVar()
        game2Title = tk.StringVar()
        game3Title = tk.StringVar()
        game4Title = tk.StringVar()
        game5Title = tk.StringVar()
        compName.set("Computer")
        compRound1.set("0")
        compRound2.set("0")
        compRound3.set("0")
        compRound4.set("0")
        compRound5.set("0")
        playerName.set("Player 1")
        playerRound1.set("0")
        playerRound2.set("0")
        playerRound3.set("0")
        playerRound4.set("0")
        playerRound5.set("0")
        game1Title.set("Game 1")
        game2Title.set("Game 2")
        game3Title.set("Game 3")
        game4Title.set("Game 4")
        game5Title.set("Game 5")

        comp = Player("Computer", [compName, compRound1, compRound2, compRound3, compRound4, compRound5])
        player = Player("Player 1", [playerName, playerRound1, playerRound2, playerRound3, playerRound4, playerRound5])

        title = tk.Label(self, text = "ROCK Paper Scissors", fg= "#800D02")
        title.config(font=("Arial Black", 44))
        title.pack()

        curScores = tk.Label(self, text="Scores:")
        curScores.pack()
      
        scoreCardFrame = tk.Frame(self, height = 100, width = 700)
        playerLabel = tk.Label(scoreCardFrame, text="Player 1")
        computerLabel = tk.Label(scoreCardFrame, text="Computer")
        numGames = 3
        if gameLength == "Best 3 of 5":
            numGames = 5
        titles = Player("titles", ["", game1Title, game2Title, game3Title, game4Title, game5Title])
        for r in range(3):
            for c in range(numGames+1):
                rowInfo = Player("", [])
                if r == 0:
                    rowInfo = titles
                if r == 1:
                    rowInfo = comp
                if r == 2:
                    rowInfo = player
                Label = tk.Label(scoreCardFrame, textvariable=rowInfo.scores[c])
                Label.grid(row=r, column=c)

        # game1Label = tk.Label(scoreCardFrame, text="Game 1")
        # game2Label = tk.Label(scoreCardFrame, text="Game 2")
        # game3Label = tk.Label(scoreCardFrame, text="Game 3")
        # game1Label.grid(row=0, column=1)
        # game2Label.grid(row=0, column=2)
        # game3Label.grid(row=0, column=3)
        # playerLabel.grid(row=1)
        # computerLabel.grid(row=2)

        scoreCardFrame.pack()

        image = Image.open('ball.png')
        image = image.resize((600, 600))
        image = ImageTk.PhotoImage(image)
        self.imageView = tk.Label(self, height = 350, width = 250, bg ="#9CAAFF", image = image)
        self.imageView.pack(side="left", padx=10, pady=10)



        emojes = tk.Label(self, text = "")
        emojes.config(font=("Arial Black", 70))
        emojes.pack()

        goButton = tk.Button(self, text = 'Start Round', fg='green', bg='red', width=30, height=6)
        goButton.pack()

        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        tempButton = tk.Button(self, text="add point for computer")
        def incrementComputer(event):
             compRound2.set("1")
        tempButton.bind("<Button-1>", incrementComputer)
        tempButton.pack()

        button.pack()
        # self.thread = threading.Thread(target=self.getVideo, args=())
        # self.thread.start()

        def startRound(event):
            showRock()
            self.after(1000, showPaper)
            self.after(2000, showScissors)
            self.after(3000, showGo)
            self.after(3100, detectHand)

        def showRock():
            emojes["text"] = "✊"
        def showPaper():
            emojes["text"] = "✋"
        def showScissors():
            emojes["text"] = "✌️"
        def showGo():
            emojes["text"] = "Go!"

        def detectHand():
            counter = 0
            usersAnswers = []
            while counter < 500:
                frame = self.vs.read()
                tempUserAnswer = getFingerCount(frame, False)
                print(tempUserAnswer)
                usersAnswers.append(tempUserAnswer)
                counter += 1
            #sort list by most common
            result = [item for items, c in Counter(usersAnswers).most_common() 
                                      for item in [items] * c] 
            usersAnswer = result[0]
            computerAnser = pickRandom()
            print("User says " + str(usersAnswer))
            print("Computer says " + str(computerAnser))

        def pickRandom():
            compAnswer = random.randint(1,3)
            if compAnswer == 1:
                showRock()
                return(1)
            elif compAnswer == 2:
                showPaper()
                return(2)
            else:
                showScissors()
                return(3)

        goButton.bind("<Button-1>", startRound)
        
    def getVideo(self):
        while(True):
            frame = self.vs.read()
            frame = imutils.resize(frame, height = 300) #600
            cv2.rectangle(frame,(50,50),(210,210),(0,255,0),0)  #(100,100),(420,420)
            #frameCropped = frame[0:0, 150:150]
            frameCropped = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frameCropped = Image.fromarray(frameCropped)
            frameCropped = ImageTk.PhotoImage(frameCropped)
            self.imageView.configure(image=frameCropped)
            self.imageView.image = frameCropped