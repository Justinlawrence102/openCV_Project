import tkinter as tk             
from PIL import Image
from PIL import ImageTk
from imutils.video import VideoStream
from roundOfGame import gameView
import threading
import imutils  #convience functions
import cv2      # embed OpenCV 4
from collections import Counter

#import Tkinter as tk     # python 2
#import tkFont as tkfont  # python 2

class Rock_Paper_Sissors_App(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        vs = VideoStream(src=0).start() #used for multithreading
        gameLength = tk.StringVar()

        self.frames = {}
        for F in (StartPage, settingsView, gameView):
            page_name = F.__name__
            frame = F(parent=container, controller=self, vs = vs, gameLength = gameLength)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller, vs, gameLength):
        #self.window = tk.Tk()
        tk.Frame.__init__(self,parent)
        self.controller = controller
        self.vs = vs
        self.gameLength = gameLength


        title = tk.Label(self, text = "ROCK Paper Scissors", fg= "#800D02")
        title.config(font=("Arial Black", 44))
        title.pack()

        settingsButton = tk.Button(self, text="Settings", bg = "red", command=lambda: controller.show_frame("settingsView"))
        settingsButton.pack()

        image = Image.open('ball.png')
        image = image.resize((600, 600))
        image = ImageTk.PhotoImage(image)
        self.imageView = tk.Label(self, height = 400, width = 250, bg ="#9CAAFF", image = image)
        self.imageView.pack(side="left", padx=10, pady=10)

        # frame2 = tk.Frame(master=self.window, width=250, bg="yellow")
        # frame2.pack(fill=tk.Y, side="left")
        emojes = tk.Label(self, text = "✊✋✌️")
        emojes.config(font=("Arial Black", 70))
        emojes.pack()

        rulesTitle = tk.Label(self, text = "Rules", anchor="e", justify="left")
        rulesTitle.config(font=("Arial Black", 26))
        rulesTitle.pack()

        print(gameLength.get())
        rules = tk.Label(self, text = "Theses are the rules, you can play \nbest 2  of 3 or 3 of 5. Rock beats \nscissors, scissors beats paper, and \npaper beats rock.", width=40, justify="left")
        rules.config(font=("Arial", 15))
        rules.pack()

        curGame = tk.Label(self, textvariable=gameLength)
        curGame.config(font=("Arial", 25))
        gameLength.set("Best 2 of 3")
        curGame.pack()

        blankSpace = tk.Label(self, height = 6, width = 20, bg ="white")
        blankSpace.pack()

        startButton = tk.Label(self, text="Start", width=25, height=3, bg='red', fg='white')
        startButton.bind("<Button-1>", self.did_press_start)
        startButton.pack()

    def did_press_start(self, event):
        self.controller.show_frame("gameView")


class settingsView(tk.Frame):

    def __init__(self, parent, controller, vs, gameLength):
        self.thread = None
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.gameLength = gameLength

        title = tk.Label(self, text="Settings")
        title.pack(side="top", fill="x", pady=10)
        var1 = tk.StringVar()
        ThreeOutOf5Check = tk.Checkbutton(self, text="Best 3 out of 5", variable=gameLength, onvalue="Best 3 of 5", offvalue="Best 2 of 3")
        ThreeOutOf5Check.pack()

        button = tk.Button(self, text="Save",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

        print("its one!" + str(var1))

if __name__ == "__main__":
    app = Rock_Paper_Sissors_App()
    app.mainloop()
