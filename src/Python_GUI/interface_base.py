import tkinter as tk 

window = tk.Tk()
window.title("QwertyHertz")

label = tk.Label(
    	text="Olá, bem vindo(a) ao QwertyHertz!",
    	fg="white",  # Set the text color to white
    	bg="black",  # Set the background color to black
	height=20,
	width=80
)
label.pack()

btn = tk.Button(text="Clique aqui!")
btn.pack()



window.mainloop()
