import tkinter as tk 
import sys

class PrintLogger(): # create file like object
    def __init__(self, textbox): # pass reference to text widget
        self.textbox = textbox # keep ref

    def write(self, text):
        self.textbox.insert(tk.END, text) # write text to textbox
            # could also scroll to end of textbox here to make sure always visible

    def flush(self): # needed for file like object
        pass

if __name__ == '__main__':
    def consol_write_t():
        print('i did something')
    def consol_write_y():
        print('Teste de log')
        #window.after(1000, consol_write)

window = tk.Tk()
window.title("QwertyHertz")

label = tk.Label(
    	text="Olá, bem vindo(a) ao QwertyHertz!",
    	fg="white",  # Set the text color to white
    	bg="black",  # Set the background color to black
	    height=5,
	    width=80
)
label.pack()

t = tk.Text(
    	#text="Olá, bem vindo(a) ao QwertyHertz!",
    	fg="white",  # Set the text color to white
    	bg="black",  # Set the background color to black
	    height=20,
	    width=80
)
t.pack()


pl = PrintLogger(t)
sys.stdout = pl

window.after(1000, consol_write_t)
window.after(2000, consol_write_y)
window.mainloop()
