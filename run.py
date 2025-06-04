import multiprocessing
import subprocess
from main import start
import pyautogui
def startjarvis():
    print("process 1 is running")
    start()
def listenhotword():
    print("process 2 is running")
    from engine.feature import new_hotword
    new_hotword()
if __name__ == "__main__":
    p1 = multiprocessing.Process(target=startjarvis)
    p2 = multiprocessing.Process(target=listenhotword)
    pyautogui.hotkey('win', 'm')
    p1.start()
    subprocess.call([r'device.bat'])
    p2.start()
    p1.join()
    if p2.is_alive():
        p2.terminate()
        p2.join()
    print("System Stop")