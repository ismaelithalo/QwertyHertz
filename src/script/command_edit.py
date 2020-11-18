import pyautogui
import json
import speech_recognition as sr
import sys

r = sr.Recognizer()                                                                                 #Define r como a variável que guarda o core da lib de recordação

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