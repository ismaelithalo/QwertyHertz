#pilha basica de execuçao provisria antes dos mdoulos principais
#reconhecimento da voz e exportaçao do json com o dito
exec(open("./src/script/voice_rec.py").read())
#tratamento do json
exec(open("./src/script/data_fix.py").read())
#filtro de comandos
exec(open("./src/script/command_selector.py").read())