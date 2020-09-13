import tkinter as tk
import sys
import subprocess
import threading 

# --- functions ---

def run():
    threading.Thread(target=test).start()

def test():
    print("Hello World")

    p = subprocess.Popen("ping -c 4 stackoverflow.com".split(), stdout=subprocess.PIPE, bufsize=1, text=True)
    while p.poll() is None:
        msg = p.stdout.readline().strip() # read a line from the process output
        if msg:
            print(msg)

    print("Finished")

# --- classes ---

class Redirect():

    def __init__(self, widget):
        self.widget = widget

    def write(self, text):
        self.widget.insert('end', text)

    #def flush(self):
    #    pass

# --- main ---    

root = tk.Tk()

text = tk.Text(root)
text.pack()

button = tk.Button(root, text='TEST', command=run)
button.pack()

old_stdout = sys.stdout    
sys.stdout = Redirect(text)

root.mainloop()

sys.stdout = old_stdout
