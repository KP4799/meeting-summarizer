from googletrans import Translator

translator = Translator()

def translate_text(filedata):
    #file = open("file.txt")
    #filedata = file.readlines()

    with open('text.txt', 'a') as file:
        file.write((filedata))
    print("Transcripted Text Saved")

def translate_summary(filedata):

    with open('summary.txt','a') as file:
        file.write((filedata))
    
    print("Original Summary Saved")

    output = translator.translate(filedata,dest="hi")
    with open('summary_hindi.txt','a') as file:
        file.write((output.text))

    output = translator.translate(filedata,dest="gu")
    with open('summary_gujarati.txt','a') as file:
        file.write((output.text))

    print("Translated Summary Saved")