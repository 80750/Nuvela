import os
import re
import time
def extract_yt_term(command):
    pattern = r'play\s+(.*?)\s+on\s+youtube'
    match = re.search(pattern, command, re.IGNORECASE)
    return match.group(1) if match else None
def remove_words(input_string, words_to_remove):
    words = input_string.split()
    filtered_words = [word for word in words if word.lower() not in words_to_remove]
    result_string = ' '.join(filtered_words)
    return result_string
# input_string = "make a phone call to pappa"
# words_to_remove = ['make', 'a', 'to', 'phone', 'call', 'send', 'message', 'wahtsapp', '']
# result = remove_words(input_string, words_to_remove)
# print(result)
def keyEvent(key_code):
    command =  f'adb shell input keyevent {key_code}'
    os.system(command)
    time.sleep(1)

# Tap event used to tap anywhere on screen
def tapEvents(x, y):
    command =  f'adb shell input tap {x} {y}'
    os.system(command)
    time.sleep(1)

# Input Event is used to insert text in mobile
def adbInput(message):
    command =  f'adb shell input text "{message}"'
    os.system(command)
    time.sleep(1)

# to go complete back
def goback(key_code):
    for i in range(6):
        keyEvent(key_code)
def swipe(a, b, c, d):
    command = f'adb shell input swipe {a} {b} {c} {d}'
    os.system(command)
    time.sleep(1)
def keyevents(u, v, w, x, y):
    command = f'adb shell input keyevent {u} {v} {w} {x} {y}'
    os.system(command)
    time.sleep(1)

# To replace space in string with %s for complete message send
def replace_spaces_with_percent_s(input_string):
    return input_string.replace(' ', '%s')
def extract_sp_term(song):
    pattern1 = r'play\s+(.*?)\s+on\s+spotify'
    match1 = re.search(pattern1, song, re.IGNORECASE)
    return match1.group(1) if match1 else None
def replace_text_query(word):
    pattern2 = r'type\s+(.*?)\s+on\s+notepad'
    match2 = re.search(pattern2, word, re.IGNORECASE)
    return match2.group(1) if match2 else None
def volume_clear(vol):
    return vol.split()[-1]
def time_clear(time):
    y = len(time)
    if y == 3:
        return time.split()[-1]
    elif y == 9:
        return time[-6:]
    elif y == 10:
        if len(time.split()[1]) == 2 or len(time.split()[1]) == 1:
            return time[-7:]
    elif y == 11:
        if len(time.split()[1]) == 1 or len(time.split()[1]) == 2:
            return time[-8:]
    elif y == 12:
        if len(time.split()[1]) == 1 or len(time.split()[1]) == 2:
            return time[-9:]
    elif y == 13:
        return time[-10:]