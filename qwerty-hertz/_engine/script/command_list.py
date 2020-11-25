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