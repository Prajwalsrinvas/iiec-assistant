import os

import pyttsx3
import speech_recognition as sr

user_name = input("What is your name?: ")
pyttsx3.speak(f"Hello {user_name},!")
pyttsx3.speak("I am IIEC-assistant")
pyttsx3.speak("I can help you open software programs!")

software_dict = {("word", "ms word", "microsoft word"): "winword",
                 ("notepad", "editor", "text editor"): "notepad",
                 ("chrome", "browser"): "chrome",
                 ("calc", "calculator"): "calc",
                 ("vlc", "videolan"): "vlc",
                 ("player", "media player", "windows media player"): "wmplayer"
                 }

r = sr.Recognizer()


def voice_input():
    while (True):
        try:
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2, duration=0.2)
                audio2 = r.listen(source2)
                MyText = r.recognize_google(audio2)
                MyText = MyText.lower()
                return MyText

        except sr.RequestError as e:
            print("Please connect to the internet!{0}".format(e))

        except sr.UnknownValueError:
            print("waiting...")


def add_new_software():
    commonly_used_words = tuple(input(
        "\nEnter commonly used names for the software seperated by commas\nFor example notepad can be referred to as notepad,editor,text editor etc:\n").split(
        ','))
    software_name = input("\nEnter the name of the .exe file (Make sure it is included in the path!):\n")
    software_dict[commonly_used_words] = software_name


def checker():
    flag = ''
    for word in user_input:
        for software in software_dict:
            if word in software:
                flag = 'found'
                command = software_dict[software]
                print(f"opening {command}")
                os.system(command)
                break
    if flag != "found":
        choice = input("If you are sure it is installed,type yes, otherwise type no:\n")
        if choice == 'yes':
            add_new_software()


while True:
    print("Which software do you want to open? [say exit to quit]: ")
    user_input = voice_input().lower().split()
    if 'exit' in user_input:
        print(f"byee {user_name}")
        pyttsx3.speak(f"byee {user_name}")
        break
    else:
        checker()
