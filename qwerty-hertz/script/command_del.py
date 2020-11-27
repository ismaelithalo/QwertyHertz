import pyautogui
import json
import speech_recognition as sr
import sys

r = sr.Recognizer()                                                                                 #Define r como a variável que guarda o core da lib de recordação

with sr.Microphone() as source:                                                                     #Função que usa a lib de recordação e guarda a resposta em uma variável
    r.adjust_for_ambient_noise(source)
    print("\n\nRepita pausadamente o comando que queira apagar, você tem 3 segundos ...")
    data = r.record(source, duration=3)
    text = r.recognize_google(data,show_all=True,language='pt')

if len(text) == 0:                                                                                  #Verifica se a recordação está vazia
    sys.exit()

with open('script/comm_edit.txt', 'w') as file:                                                    #Salva a gravação em um arquivo
    file.write("{}".format(text))
    
with open('script/comm_edit.txt') as file:                                                         #Lê esse arquivo
    text = file.read()

text = text.replace("\'", "\"")                                                                     #Substitui os elementos de um fake json por um json completo
text = text.replace("True", "true")

with open('script/edit_command.json', 'w') as t_json:                                              #Grava o json em um arquivo
    t_json.write(text)

with open('script/edit_command.json', 'r') as input_file:                                          #Abre o arquivo do json e o coloca em uma variável
    data = json.load(input_file)

comm = data['alternative'][0]['transcript']                                                         #Seleciona o primeiro elemento do json pois é o maior precisão

flag_1 = True
flag_2 = False

with open('script/command_atalho_list.txt','r') as file:
    lines = file.readlines()
    
with open('script/command_atalho_list.txt') as file:    
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
    with open('script/command_atalho_list.txt','w') as file:
        novo = "\n".join(mantem)
        file.write(novo)
if(flag_1):            
    print("Comando nao listado ... Reinicie o processo de delecao")
    sys.exit()