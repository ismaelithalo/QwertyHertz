import speech_recognition as sr
r = sr.Recognizer()

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)

    print("\n\nRepita pausadamente o que quer, você tem 3 segundos ...")

    data = r.record(source, duration=3)
    text = r.recognize_google(data,show_all=True,language='pt')
    #print(text)

#with open('../json/text.txt', 'w') as file:
with open('src/json/text.txt', 'w') as file:
    file.write("{}".format(text))


