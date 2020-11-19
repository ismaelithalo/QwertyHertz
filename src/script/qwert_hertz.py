import speech_recognition as sr
import sys
import json
import pyautogui
import time
import subprocess

r = sr.Recognizer()

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)

    print("\n\nRepita pausadamente o que quer, você tem 3 segundos ...")

    data = r.record(source, duration=3)
    text = r.recognize_google(data,show_all=True,language='pt')
    #print(text)

if len(text) == 0:
    sys.exit()

#with open('../json/text.txt', 'w') as file:
with open('src/json/text.txt', 'w') as file:
    file.write("{}".format(text))

with open('src/json/text.txt') as file:
    text = file.read()

text = text.replace("\'", "\"")
text = text.replace("True", "true")

with open('src/json/command.json', 'w') as t_json:
    t_json.write(text)

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
                with sr.Microphone() as source:                                                                     #Função que usa a lib de recordação e guarda a resposta em uma variável
                    r.adjust_for_ambient_noise(source)
                    print("\n\nRepita pausadamente o comando que queira cadastrar, você tem 3 segundos ...")
                    data = r.record(source, duration=3)
                    text = r.recognize_google(data,show_all=True,language='pt')

                if len(text) == 0:                                                                                  #Verifica se a recordação está vazia
                    sys.exit()

                with open('src/json/comm_rec.txt', 'w') as file:                                                    #Salva a gravação em um arquivo
                    file.write("{}".format(text))

                with open('src/json/comm_rec.txt') as file:                                                         #Lê esse arquivo
                    text = file.read()

                text = text.replace("\'", "\"")                                                                     #Substitui os elementos de um fake json por um json completo
                text = text.replace("True", "true")

                with open('src/json/cad_command.json', 'w') as t_json:                                              #Grava o json em um arquivo
                    t_json.write(text)

                with open('src/json/cad_command.json', 'r') as input_file:                                          #Abre o arquivo do json e o coloca em uma variável
                    data = json.load(input_file)

                comm = data['alternative'][0]['transcript']                                                         #Seleciona o primeiro elemento do json pois é o maior precisão

                print("\nDigite quantas teclas possui seu atalho de teclado")
                n = input()                                                                                         #Recebe o numero de teclas
                n = int(n)                                                                                          #Transforma a string recebida em inteiro
                teclas = []                                                                                         #Inicializa um array
                teclas.append(comm)                                                                                 #Coloca o comando gravado nesse array
                teclas.append(str(n))                                                                                 #Coloca o comando gravado nesse array

                for x in range(n):
                    print("\nDigite a tecla numero {}.".format(x+1))
                    print("(Ex. 'ctrl','del','fn','win','alt','shift','space','b','5','enter'.)")
                    teclas.append(input())                                                                          #Recebe a tecla e insere no array
                    
                print("Conferindo. As seguintes informações serão cadastradas, está tudo certo? s/n\n{}".format(teclas))

                if (input() == 's'):                                                                                #Confirma com o usuário se as instruções recebidas estão corretas
                    comando = '\n'+";".join(teclas)                                                                 #Pega todos os elementos do array e os coloca em uma string separada pelo elemento ;
                    
                    with open('src/json/command_atalho_list.txt', 'a') as file:                                            #Abre o arquivo de comandos no modo de adicionar                                      
                        file.write(comando)                                                                         #Insere essa string no arquivo
                else:
                    print("Ok. Reinicie o processo de gravação.")
                    sys.exit() 
                    
        elif (inst == 'editar comando'):
                with sr.Microphone() as source:                                                                     #Função que usa a lib de recordação e guarda a resposta em uma variável
                    r.adjust_for_ambient_noise(source)
                    print("\n\nRepita pausadamente o comando que queira editar, você tem 3 segundos ...")
                    data = r.record(source, duration=3)
                    text = r.recognize_google(data,show_all=True,language='pt')

                if len(text) == 0:                                                                                  #Verifica se a recordação está vazia
                    sys.exit()

                with open('src/json/comm_edit.txt', 'w') as file:                                                    #Salva a gravação em um arquivo
                    file.write("{}".format(text))
                    
                with open('src/json/comm_edit.txt') as file:                                                         #Lê esse arquivo
                    text = file.read()

                text = text.replace("\'", "\"")                                                                     #Substitui os elementos de um fake json por um json completo
                text = text.replace("True", "true")

                with open('src/json/edit_command.json', 'w') as t_json:                                              #Grava o json em um arquivo
                    t_json.write(text)

                with open('src/json/edit_command.json', 'r') as input_file:                                          #Abre o arquivo do json e o coloca em uma variável
                    data = json.load(input_file)

                comm = data['alternative'][0]['transcript']                                                         #Seleciona o primeiro elemento do json pois é o maior precisão

                flag_1 = True
                flag_2 = False

                with open('src/json/command_atalho_list.txt','r') as file:
                    lines = file.readlines()
                    
                with open('src/json/command_atalho_list.txt') as file:    
                    comandos = file.read().split('\n')
                    mantem = []
                    for x in range(len(comandos)):
                        mantem.append(comandos[x])
                        comman = comandos[x].split(';')
                        if (comm == comman[0]):
                            flag_1 = False
                            flag_2 = True
                            mantem.remove(comandos[x])
                            print("Comando encontrado, iniciando edicao.")
                            
                            with sr.Microphone() as source:                                                                     #Função que usa a lib de recordação e guarda a resposta em uma variável
                                r.adjust_for_ambient_noise(source)
                                print("\n\nRepita pausadamente o nome novo do comando, você tem 3 segundos ...")
                                data = r.record(source, duration=3)
                                text = r.recognize_google(data,show_all=True,language='pt')

                            if len(text) == 0:                                                                                  #Verifica se a recordação está vazia
                                sys.exit()

                            with open('src/json/comm_rec.txt', 'w') as file:                                                    #Salva a gravação em um arquivo
                                file.write("{}".format(text))

                            with open('src/json/comm_rec.txt') as file:                                                         #Lê esse arquivo
                                text = file.read()

                            text = text.replace("\'", "\"")                                                                     #Substitui os elementos de um fake json por um json completo
                            text = text.replace("True", "true")

                            with open('src/json/cad_command.json', 'w') as t_json:                                              #Grava o json em um arquivo
                                t_json.write(text)

                            with open('src/json/cad_command.json', 'r') as input_file:                                          #Abre o arquivo do json e o coloca em uma variável
                                data = json.load(input_file)

                            new = data['alternative'][0]['transcript']                                                         #Seleciona o primeiro elemento do json pois é o maior precisão

                            print("\nDigite quantas teclas possui seu atalho de teclado")
                            n = input()                                                                                         #Recebe o numero de teclas
                            n = int(n)                                                                                          #Transforma a string recebida em inteiro
                            teclas = []                                                                                         #Inicializa um array
                            teclas.append(new)                                                                                 #Coloca o comando gravado nesse array
                            teclas.append(str(n))                                                                                 #Coloca o comando gravado nesse array

                            for x in range(n):
                                print("\nDigite a tecla numero {}.".format(x+1))
                                print("(Ex. 'ctrl','del','fn','win','alt','shift','space','b','5','enter'.)")
                                teclas.append(input())                                                                          #Recebe a tecla e insere no array
                                
                            print("Conferindo. As seguintes informações serão cadastradas, está tudo certo? s/n\n{}".format(teclas))

                            if (input() == 's'):                                                                                #Confirma com o usuário se as instruções recebidas estão corretas
                                comando = ";".join(teclas)                                                                 #Pega todos os elementos do array e os coloca em uma string separada pelo elemento ;
                                mantem.append(comando)                                                                         #Insere essa string no arquivo
                            else:
                                print("Ok. Reinicie o processo de gravação.")
                                flag_2 = False
                                sys.exit()
                    file.close()
                if(flag_2):
                    with open('src/json/command_atalho_list.txt','w') as file:
                        novo = "\n".join(mantem)
                        file.write(novo)
                if(flag_1):            
                    print("Comando nao listado ... Reinicie o processo de ediçao")
                    sys.exit()    
                
        elif (inst == 'listar comandos'):
                with open('src/json/command_atalho_list.txt') as file: 
                        print("\nComandos disponíveis:")   
                        comandos = file.read().split('\n')
                        for x in range(len(comandos)):
                                comman = comandos[x].split(';')
                                print("\n{}".format(comman[0]))
                        print("\n")
        elif (inst == 'listar comandos e atalhos'):
                with open('src/json/command_atalho_list.txt') as file: 
                    print("\nComandos disponíveis:")   
                    comandos = file.read().split('\n')
                    for x in range(len(comandos)):
                            comman = comandos[x].split(';')
                            print("\n")
                            for i in range(len(comman)):
                                if(i > 0):
                                    if (i == 1):
                                        print("Numero de teclas: {}".format(comman[i]))
                                    else:
                                        print("{}: {}".format((i-1),comman[i]))
                                else:
                                    print("Comando: {}".format(comman[i]))
                                    print("\nAtalhos:")
                    print("\n")
        elif (inst == 'apagar comando'):
                with sr.Microphone() as source:                                                                     #Função que usa a lib de recordação e guarda a resposta em uma variável
                    r.adjust_for_ambient_noise(source)
                    print("\n\nRepita pausadamente o comando que queira editar, você tem 3 segundos ...")
                    data = r.record(source, duration=3)
                    text = r.recognize_google(data,show_all=True,language='pt')

                if len(text) == 0:                                                                                  #Verifica se a recordação está vazia
                    sys.exit()

                with open('src/json/comm_edit.txt', 'w') as file:                                                    #Salva a gravação em um arquivo
                    file.write("{}".format(text))
                    
                with open('src/json/comm_edit.txt') as file:                                                         #Lê esse arquivo
                    text = file.read()

                text = text.replace("\'", "\"")                                                                     #Substitui os elementos de um fake json por um json completo
                text = text.replace("True", "true")

                with open('src/json/edit_command.json', 'w') as t_json:                                              #Grava o json em um arquivo
                    t_json.write(text)

                with open('src/json/edit_command.json', 'r') as input_file:                                          #Abre o arquivo do json e o coloca em uma variável
                    data = json.load(input_file)

                comm = data['alternative'][0]['transcript']                                                         #Seleciona o primeiro elemento do json pois é o maior precisão

                flag_1 = True
                flag_2 = False

                with open('src/json/command_atalho_list.txt','r') as file:
                    lines = file.readlines()
                    
                with open('src/json/command_atalho_list.txt') as file:    
                    comandos = file.read().split('\n')
                    mantem = []
                    for x in range(len(comandos)):
                        mantem.append(comandos[x])
                        comman = comandos[x].split(';')
                        if (comm == comman[0]):
                            flag_1 = False
                            flag_2 = True
                            
                            print("Comando encontrado, iniciando delecao.")
                            print("\nConferindo. O seguinte comando sera apagado, está tudo certo? s/n\n{}".format(comman[0]))              #Confirma com o usuário se as instruções recebidas estão corretas
                            
                            if (input() == 's'):                                                                                
                                mantem.remove(comandos[x])
                                print("\nComando apagado com sucesso.")
                            else:
                                print("Ok. Finalizando o processo.")
                                flag_2 = False
                                sys.exit()
                    file.close()
                if(flag_2):
                    with open('src/json/command_atalho_list.txt','w') as file:
                        novo = "\n".join(mantem)
                        file.write(novo)
                if(flag_1):            
                    print("Comando nao listado ... Reinicie o processo de delecao")
                    sys.exit()
        else:
                print("Comando nao listado ...")