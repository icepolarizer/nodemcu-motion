import requests
import time
from pygame import mixer

mixer.init()
mixer.music.load('BEEP.WAV')
detect_flag = False

while(True):
    p = requests.get("http://192.168.1.165")
    if p.text == 'true':
        detected = True
    else:
        detected = False
    print(detected)
    if detected and (detect_flag == False):
        print("Got it")
        mixer.music.play()
    detect_flag = detected
    time.sleep(0.5)

