import speech_recognition as sr
#import time

r = sr.Recognizer()

def listen():
    x = 1
    while x == 1:
        try:
            with sr.Microphone() as source:
                print("Speak")
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
                text = r.recognize_google(audio)

                #time.sleep(5)

                print(f"Recognized text : {text}")

                # text = text + "\n"
                ##### (ISKO CHECK KARNA BAADME) #####

                

                #with open('file.txt', 'a') as file:
                #    file.write(text)

                if text == 'banana':
                    print("recording stopped")
                    #global x
                    x = 0
                    #return '\n'
                    #exit(0)

                return text

        except:
            print("Try Again")
            text = '\n'
            return text
            #continue

listen()

