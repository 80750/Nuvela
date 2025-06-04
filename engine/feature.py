import os
import re
import struct
import subprocess
import time
from pipes import quote
from hugchat import hugchat
from playsound import playsound
import pvporcupine
import eel
import pyaudio
import pyautogui
import pywhatkit as kit
import webbrowser
import sqlite3
from engine.command import speakFunction
from engine.config import ASSISTANT_NAME
from engine.config import APISTOKEN
from engine.helper import extract_yt_term, remove_words, replace_text_query
from engine.helper import extract_sp_term
import requests
import speech_recognition
from pvrecorder import PvRecorder

con = sqlite3.connect("jarvis.db")
cursor_obj = con.cursor()
import json 
import spotipy
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume  

username = '3144yhzaepzsolxc7ypqsttnlpiu'
clientID = 'fb6d0c039840459fae0cad7dd5e473de'
clientSecret = '234d8e7f403e410493a7396c9474fd73'
redirect_uri = 'http://google.com/callback/'
oauth_object = spotipy.SpotifyOAuth(clientID, clientSecret, redirect_uri) 
token_dict = oauth_object.get_access_token() 
token = token_dict['access_token'] 
spotifyObject = spotipy.Spotify(auth=token) 
user_name = spotifyObject.current_user()
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

def potify(pot):
    music = extract_sp_term(pot)
    results = spotifyObject.search(music, 1, 0, "track")
    music_dict = results['tracks']
    music_item = music_dict['items']
    song = music_item[0]['external_urls']['spotify']
    webbrowser.open(song)
    speakFunction("playing "+music+" on spotify") 
@eel.expose
#play opening sound
def playAssistantSound():
    music_dir = 'C:\\Users\\mayan\\OneDrive\\Documents\\jarvis\\assets\\start_sound.mp3'
    playsound(music_dir)
def OpenCommand(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("open", "")
    query.lower()
    app_name = query.strip()
    if app_name != "":
        try:
            cursor_obj.execute('SELECT path FROM sys_command WHERE name IN (?)', (app_name,))
            results = cursor_obj.fetchall()
            if len(results) != 0:
                speakFunction("Opening "+query)
                os.startfile(results[0][0])
            elif len(results) == 0:
                cursor_obj.execute('SELECT path FROM web_command WHERE name IN (?)', (app_name,))
                results = cursor_obj.fetchall()
                if len(results) != 0:
                    speakFunction("Openning "+query)
                    webbrowser.open(results[0][0])
                else:
                    speakFunction("Opening "+query)
                    try:
                        os.system('start '+query)
                    except:
                        speakFunction("not found")
        except:
            speakFunction("SomeThing Went Wrong")
def PlayYoutube(query):
    search_term = extract_yt_term(query)
    speakFunction("Playing "+search_term+" on youtube")
    kit.playonyt(search_term)
# def hotword():
#     porcupine = pvporcupine.create(APISTOKEN, keywords=["jarvis"])
#     recorder = PvRecorder(device_index=-1, frame_length=porcupine.frame_length)
#     try:
#        recorder.start()
#        while True:
#            keyword_index = porcupine.process(recorder.read())
#            if keyword_index >= 0:
#                print(f"Detected")
#     except KeyboardInterrupt:
#         stream.stop_stream()
#         stream.close()
#         p.terminate()
def findContact(query):
    words_to_remove = [ASSISTANT_NAME, 'make', 'a', 'to', 'phone', 'call', 'send', 'message', 'wahtsapp', 'video']
    query = remove_words(query, words_to_remove)
    try:
        query = query.strip().lower()
        cursor_obj.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", ('%' + query + '%', query + '%'))
        results = cursor_obj.fetchall()
        print(results[0][0])
        mobile_number_str = str(results[0][0])
        if not mobile_number_str.startswith('+91'):
            mobile_number_str = '+91' + mobile_number_str
        return mobile_number_str, query
    except:
        speakFunction('not exist in contacts')
        return 0, 0
def whatsApp(mobile_no, message, flag, name):
    if flag == 'message':
        target_tab = 21
        jarvis_message = "message send successfully to "+name
    elif flag == 'call':
        target_tab = 15
        message = ''
        jarvis_message = "calling to "+name
    else:
        target_tab = 14
        message = ''
        jarvis_message = "staring video call with "+name
    encoded_message = quote(message)
    whatsapp_url = f"whatsapp://send?phone={mobile_no}&text={encoded_message}"
    full_command = f'start "" "{whatsapp_url}"'
    subprocess.run(full_command, shell=True)
    time.sleep(5)
    subprocess.run(full_command, shell=True)
    pyautogui.hotkey('ctrl', 'f')
    for i in range(1, target_tab):
        pyautogui.hotkey('tab')
    pyautogui.hotkey('enter')
    speakFunction(jarvis_message)

def chatBot(query):
    user_input = query.lower()
    chatbot = hugchat.ChatBot(cookie_path="engine\deepseek.json")
    id = chatbot.new_conversation()
    chatbot.change_conversation(id)
    response =  chatbot.chat(user_input)
    print(response)
    speakFunction(response)
    return response

def makeCall(name, mobileNo):
    from engine.helper import replace_spaces_with_percent_s, goback, keyEvent, tapEvents, adbInput, swipe, keyevents
    mobileNo =mobileNo.replace(" ", "")
    speakFunction("Calling "+name)
    #power on phone
    keyEvent(26)
    #enter password
    keyevents(12, 14, 9, 13, 14)
    comm = 'adb shell am start -a android.intent.action.CALL -d tel:'+mobileNo
    os.system(comm)


def sendMessage(message, mobileNo, name):
    from engine.helper import replace_spaces_with_percent_s, goback, keyEvent, tapEvents, adbInput, swipe, keyevents
    message = replace_spaces_with_percent_s(message)
    mobileNo = replace_spaces_with_percent_s(mobileNo)
    speakFunction("sending message")
    #power on the phone
    keyEvent(26)
    #swipe up
    swipe(400, 1000, 400, 0)
    #enter password
    keyevents(12, 14, 9, 13, 14)
    # open sms app
    tapEvents(336, 2020)
    #start chat
    tapEvents(819, 2192)
    # search mobile no
    adbInput(mobileNo)
    #tap on name
    tapEvents(136, 620)
    # tap on input
    tapEvents(278, 2293)
    #message
    adbInput(message)
    #send
    tapEvents(994, 1560)
    speakFunction("message send successfully to "+name)

def spotify(songname):
    from engine.helper import  goback,keyEvent, tapEvents, adbInput
    sngname = extract_sp_term(songname)
    speakFunction("playing"+sngname+"on spotify")
    goback(4)
    time.sleep(1)
    keyEvent(3)
    #open spotify
    tapEvents(173, 1771)
    #go to search option
    tapEvents(408, 2277)
    #open search bar
    tapEvents(267, 432)
    #type song name
    adbInput(sngname)
    #tap search option
    tapEvents(996, 2199)
    #play song
    tapEvents(385, 466)
    speakFunction("playing song phone on spotify "+sngname)
def new_hotword():
    porcupine = pvporcupine.create(access_key= 'zUQRoKnc64bCzfppMD2kfyj/yVrIa7Rf5vEVxo+Q9syIvwE5hj0INA==' , keywords=['Nebula'])
    recorder = PvRecorder(device_index=-1, frame_length=porcupine.frame_length)
    try:
        recorder.start()
        while True:
            keyword_index = porcupine.process(recorder.read())
            if keyword_index >= 0:
                print(f"Detected")
    except KeyboardInterrupt:
        recorder.stop()
    finally:
        porcupine.delete()
        recorder.delete()
def write(test):
    text = replace_text_query(test)
    speakFunction("opening notepad")
    os.system('start notepad')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'n')
    time.sleep(1)
    speakFunction("writing")
    pyautogui.typewrite(text)
    time.sleep(1)
    speakFunction("Write successfully")

def volume_control(test):
    current_volume = volume.GetMasterVolumeLevelScalar()
    speakFunction(f"Current Volume is {str(current_volume*100)} percent")
    from engine.helper import volume_clear
    audio = volume_clear(test)
    new_volume = int(audio)/100
    volume.SetMasterVolumeLevelScalar(new_volume, None)
    speakFunction(f"Volume set to {str(audio)} percent")

def shutingdown(key):
    from engine.helper import time_clear
    tim = time_clear(key)
    if time == "now":
        speakFunction("Shutting Down Now")
        os.system('shutdown -s -t 0')
    elif time.split()[1] == "hour" or time.split()[1] == "hours":
        speakFunction(f"Shutting Down in {str(time)}")
        time1 = int(tim.split()[0])
        os.system('shutdown -s -t '+time1*3600)
    elif tim.split()[1] == "minute" or tim.split()[1] == "minutes":
        speakFunction(f"Shutting Down in {str(time)}")
        time2 = int(tim.split()[0])
        os.system('shutdown -s -t '+time2*60)
    elif tim.split()[1] == "seccond" or tim.split()[1] == "seconds":
        speakFunction(f"Shutting Down in {str(tim)}")
        os.system('shutdown -s -t '+int(tim.split()[0]))
    else:
        speakFunction("Inavlid")
