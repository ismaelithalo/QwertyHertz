import json
import pyautogui
import time
import subprocess

with open('src/json/command.json', 'r') as input_file:
    data = json.load(input_file)
#print(data)

inst = data['alternative'][0]['transcript']

time.sleep(1)
print("\nO comando dito foi: {}".format(inst))

coman_1 = "alternar"
coman_2 = "fechar"
coman_3 = "Abrir terminal"
coman_4 = "desligar"

if inst == coman_1: 
	pyautogui.hotkey('alt','tab')
	time.sleep(2)
	pyautogui.hotkey('alt','esc')

elif inst == coman_2: 
        pyautogui.hotkey('alt','tab')
        time.sleep(2)
        pyautogui.hotkey('alt','f4')

elif inst == coman_3: 
        pyautogui.hotkey('alt','tab')
        time.sleep(2)
        pyautogui.hotkey('ctrl','alt','t')
elif inst == coman_4: 
        pyautogui.hotkey('alt','tab')
        time.sleep(2)
        subprocess.run(["shutdown", "now"])
else:
        print("Comando nao listado ...")
