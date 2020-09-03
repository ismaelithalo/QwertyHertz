with open('src/json/text.json') as file:
    text = file.read()

text = text.replace("\'", "\"")
text = text.replace("True", "true")

with open('src/json/command.json', 'w') as t_json:
    t_json.write(text)
#print("{}".format(texto))