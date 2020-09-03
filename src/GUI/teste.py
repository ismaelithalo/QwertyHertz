import tkinter as tk 
import sys
import subprocess

class PrintLogger(): # create file like object
    def __init__(self, textbox): # pass reference to text widget
        self.textbox = textbox # keep ref

    def write(self, text):
        self.textbox.insert(tk.END, text) # write text to textbox
            # could also scroll to end of textbox here to make sure always visible

    def flush(self): # needed for file like object
        pass

if __name__ == '__main__':
    def w_title():
        print('Olá, bem vindo(a) ao QwertyHertz!')
        #window.after(1000, consol_write)

window = tk.Tk()
window.title("QwertyHertz")

label = tk.Label(
    	text="QwertyHertz!",
    	fg="black",  # Set the text color to white
    	bg="white",  # Set the background color to black
	    height=5,
	    width=80
)
label.pack()

t = tk.Text(
    	#text="",
    	fg="white",  # Set the text color to white
    	bg="black",  # Set the background color to black
	    height=20,
	    width=80
)
t.pack()


pl = PrintLogger(t)
sys.stdout = pl

window.after(1000, w_title)
#window.after(2000, W_test)
window.mainloop()
