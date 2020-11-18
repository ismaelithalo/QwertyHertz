import json
import pyautogui
import time
import subprocess

with open('src/json/command.json', 'r') as input_file:
    data = json.load(input_file)
#print(data)

inst = data['alternative'][0]['transcript']

# time.sleep(1)
print("\nO comando dito foi: {}".format(inst))
   
# elif inst == coman_4: 
#         pyautogui.hotkey('alt','tab')
#         time.sleep(2)
#         subprocess.run(["shutdown", "now"])

flag = True

with open('src/json/command_atalho_list.txt') as file:
    comandos = file.read().split('\n')
    for x in range(len(comandos)):
        comman = comandos[x].split(';')
        if (inst == comman[0]):
                flag = False
                if (comman[1] == '1'):
                        pyautogui.hotkey(comman[2])
                elif (comman[1] == '2'):        
                        pyautogui.hotkey(comman[2],comman[3])
                elif (comman[1] == '3'):        
                        pyautogui.hotkey(comman[2],comman[3],comman[4])
                elif (comman[1] == '4'):        
                        pyautogui.hotkey(comman[2],comman[3],comman[4],comman[5])
                elif (comman[1] == '5'):        
                        pyautogui.hotkey(comman[2],comman[3],comman[4],comman[5],comman[6])
if(flag):            
        if (inst == 'cadastrar comando'):
                exec(open("src/script/command_reg.py").read())
        elif (inst == 'editar comando'):
                exec(open("src/script/command_edit.py").read())
        elif (inst == 'listar comandos'):
                with open('src/json/command_atalho_list.txt') as file: 
                        print("\nComandos disponíveis:")   
                        comandos = file.read().split('\n')
                        for x in range(len(comandos)):
                                comman = comandos[x].split(';')
                                print("\n{}".format(comman[0]))
                        print("\n")
        elif (inst == 'listar comandos e atalhos'):
                exec(open("src/script/command_list.py").read())
        elif (inst == 'apagar comando'):
                exec(open("src/script/command_del.py").read())
        else:
                print("Comando nao listado ...")
