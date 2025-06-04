import pyttsx3
import speech_recognition as sr
# from googletrans import Translator
import eel
import time
import pyautogui
import os
# translator = Translator()
@eel.expose
def neuvela():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    engine.setProperty('rate',150)
    engine.say("Hello")
    engine .runAndWait()
    engine.say("I am Nebula")
    engine.runAndWait()
@eel.expose
def speak():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    engine.setProperty('rate',150)
    engine.say("How can I assist you today")
    engine.runAndWait()

def speakFunction(text):
    text = str(text)
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    engine.setProperty('rate',174)
    eel.DisplayMessage(text)
    engine.say(text)
    eel.receiverText(text)
    engine.runAndWait()

def TakeCommand():
    tr = sr.Recognizer()
    with sr.Microphone() as source:
        print("--Listening--")
        eel.DisplayMessage("listening--")
        tr.pause_threshold = 1
        tr.adjust_for_ambient_noise(source)
        audio = tr.listen(source, 10, 5)
    try:
        print("--Recognizing--")
        eel.DisplayMessage("--recognising--")
        query = tr.recognize_google(audio, language='en')
        print(f"user said : {query}")
        eel.DisplayMessage(query)
#        time.sleep(2)
#        speakFunction(query)
#         eel.DisplayMessage(query)
#         time.sleep(2)
#         return query
    except Exception as e:
        return ""
    return query.lower()
@eel.expose
def allcommand(message=1):
    if message == 1:
        query = TakeCommand()
        print(query)
        eel.senderText(query)
    else:
        query = message
        eel.senderText(query)
    try:
        if "open" in query:
            pyautogui.hotkey('win', 'm')
            from engine.feature import OpenCommand
            OpenCommand(query)
        elif "on youtube" in query:
            pyautogui.hotkey('win', 'm')
            from engine.feature import PlayYoutube
            PlayYoutube(query)
        elif "type" in query:
            pyautogui.hotkey('win', 'm')
            from engine.feature import write
            write(query)
        elif "terminate" in query:
            speakFunction("Terminating")
            pyautogui.hotkey('ctrl', 'alt', 'M')
        elif "shutdown" in query:
            speakFunction("do you really want to shut down it")
            preferance = TakeCommand()
            if "yes" or "sure" in preferance:
                speakFunction("At what Time you want to shutdown")
                sec = TakeCommand()
                from engine.feature import shutingdown
                shutingdown(sec)
            elif "no" in preferance:
                speakFunction("OK")
            else:
                speakFunction("Invalid")
        elif "abort" in query:
            speakFunction("Aborting shut down")
            os.system("shutdown /a")
        elif "volume" in query:
            from engine.feature import volume_control
            volume_control(query)
        elif "on spotify" in query:
            pyautogui.hotkey('win', 'm')
            speakFunction("Whoch mode you want to choose either mobile or laptop")
            preferance = TakeCommand()
            print(preferance)
            if "mobile" in preferance:
                from engine.feature import spotify
                spotify(query)
            elif "laptop" in preferance:
                from engine.feature import potify
                potify(query)
        elif "send message" in query or "phone call" in query or "video call" in query:
            pyautogui.hotkey('win', 'm')
            from engine.feature import findContact, whatsApp, makeCall, sendMessage
            contact_no, name = findContact(query)
            if(contact_no != 0):
                speakFunction("Which mode you want to use whatsapp or mobile")
                preferance = TakeCommand()
                print(preferance)

                if "mobile" in preferance:
                    if "send message" in query or "send sms" in query: 
                        speakFunction("what message to send")
                        message = TakeCommand()
                        sendMessage(message, contact_no, name)
                    elif "phone call" in query:
                        makeCall(name, contact_no)
                    else:
                        speakFunction("please try again")
                elif "whatsapp" in preferance:
                    message = ""
                    if "send message" in query:
                        message = 'message'
                        speakFunction("what message to send")
                        query = TakeCommand()
                                    
                elif "phone call" in query:
                    message = 'call'
                else:
                    message = 'video call'
                                        
                whatsApp(contact_no, query, message, name)
        elif "close" in query:
            speakFunction("closing now")
            pyautogui.hotkey('alt', 'fn', 'f4')
        elif "shutdown" in query:
            speakFunction("shutting down now")
            os.system("shutdown /s /f /t 0")
        elif "restart" in query:
            speakFunction("restarting now")
            os.system("shutdown /r /f /t 0")
        elif "lock" in query:
            speakFunction("locking now")
            os.system("shutdown /l")
        elif "advanced boot option" in query:
            os.system("shutdown /r /o /f /t 0")
        else:
            pyautogui.hotkey('win', 'm')
            from engine.feature import chatBot
            chatBot(query)
        allcommand()
    except:
        print("ERROR")
    eel.Showhood()