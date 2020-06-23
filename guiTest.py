#import stuff
#make sure you are in enviernemnt:
#workon cv
import tkinter as tk
import imutils  #convience functions
import argparse
counter = 0

window = tk.Tk()
greeting = tk.Label(
    text = "Hello World",
    foreground = "red", #text color
    background = "gray" #background color
)
greeting.pack()
entry = tk.Entry(fg="yellow", bg="gray", width=50)
entry.insert(0, "Python")
entry.pack()

button = tk.Button(
    text="Click me!",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
)
button.pack()
def handle_click(event):
    entryVal = entry.get()
    print("Entry is "+entryVal)
    global counter
    counter += 1
    greeting["text"] = "Hello World "+str(counter)
# Bind button event to handle_click()
button.bind("<Button-1>", handle_click)

frame1 = tk.Frame(master=window, height=100, bg="red") #this uses the hight and fills the width to the size of the window
frame1.pack(fill=tk.X)

frame2 = tk.Frame(master=window, height=50, bg="green")
frame2.pack(fill=tk.X)

frame3 = tk.Frame(master=window, height=80, width = 80, bg="black")
frame3.pack(side=tk.LEFT)

#for i in range(3):
#    window.columnconfigure(i, weight=1, minsize=75)
#    window.rowconfigure(i, weight=1, minsize=50)
#
#    for j in range(0, 3):
#        frame = tk.Frame(
#            master=window,
#            relief=tk.RAISED,
#            borderwidth=1
#        )
#        frame.grid(row=i, column=j, padx=5, pady=5)
#
#        label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
#        label.pack(padx=5, pady=5)
        
#label2 = tk.Label(text="Bottom Right")
#label2.grid(row=1, column=0, sticky="sw")
window.mainloop()
