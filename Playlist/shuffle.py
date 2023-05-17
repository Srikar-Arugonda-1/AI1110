import os
import random
from pygame import mixer
l = os.listdir("songs")
d = l
mixer.init()
print("\t\tp to pause\n\t\te to exit\n\t\tn to next song\n\t\tr to resume")
while True:
    if len(d)==0:
        print("songs done")
        break
    while True:
        p = random.choice(l)
        if p in d:
            break
    d.remove(p)
    mixer.music.load("songs/"+p)
    mixer.music.set_volume(3)
    mixer.music.play()
    print("playing....")
    while True:
        i = input(" ") 
        if i == 'p':
            mixer.music.pause()
            print("-----------PAUSED------------")
        elif i == 'r':
            mixer.music.unpause()
            print("------------RESUMED-----------")
        elif i == 'e':
            mixer.music.stop()
            print("stopped")
            quit()
        elif i == 'n':
            print("next song")
            break
    
