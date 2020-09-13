import tkinter as tk
from test import *
from tkinter import *
import os

class Redirect():

    def __init__(self, widget):
        self.widget = widget

    def write(self, text):
        self.widget.insert('end', text)

    # some widget may need it
    #def flush(self):
    #    pass

text = tk.Text(root)
text.pack()

# keep original stdout
old_stdout = sys.stdout    

# assing Redirect with widget Text 
sys.stdout = Redirect(text)

root.mainloop()

# assign back original stdout (if you need it)
sys.stdout = old_stdout
