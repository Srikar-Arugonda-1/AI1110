import os
import numpy
from pygame import mixer
l = os.listdir("songs")
mixer.init()
print("\t\tp to pause\n\t\te to exit\n\t\tn to next song\n\t\tr to resume")
while True:
    if len(l)==0:
        mixer.music.stop()
        print("songs done. do you want to repeat?(y/n)")
        r = input(" ")
        if r=='n':
            break
        else:
            l = os.listdir("songs")
#    while True:
#       p = random.choice(l)
#       if p in d:
#           break
    p = numpy.random.choice(l)
    l.remove(p)
    mixer.music.load("songs/"+p)
    mixer.music.set_volume(10)
    mixer.music.play()
    print("playing...."+p)
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
    
