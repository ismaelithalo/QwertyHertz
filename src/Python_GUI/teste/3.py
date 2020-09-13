import tkinter as tk
from test import *
from tkinter import *
import os

root = tk.Tk()

canvas = tk.Canvas(root, height=400, width =550, bg ="#202020") 
canvas.pack()

#frame = tk.Frame(root, bg="white");
#frame.place(relwidth=0.8, relheight = 0.8, relx=0.1, rely=0.1)

topFrame = tk.Frame(root, bg="#202020")
topFrame.place(relwidth=1, relheight = 0.75)

bottomFrame = tk.Frame(root, bg="#202020")
bottomFrame.place(rely=0.75, relwidth=1, relheight = 0.25)


launch = tk.Button(bottomFrame, text="Launch", bg="white", fg="#202020", font="noah 10 bold", padx=20, command=test)
launch.place(in_=bottomFrame, rely=0.5, relx=0.5, anchor=CENTER)

root.mainloop()
