from threading import Thread
import time
class VLC(Thread):
    def run(self):
        print("Vlc apl opened")
        time.sleep(3)
class Video_start(Thread):
    def run(self):
        print("Video started playing")
        time.sleep(3)
class Audio_start(Thread):
    def run(self):
        print("Audio started playing")
        time.sleep(3)
class Pro_bar(Thread):
    def run(self):
        print("Progress bar is activated")
        time.sleep(3)
class Valume(Thread):
    def run(self):
        print("Volume is increasing")
        time.sleep(3)
class Apl_close(Thread):
    def run(self):
        print("Vlc apl closed")
        time.sleep(3)
v1=VLC()
v2=Video_start()
v3=Audio_start()
v4=Pro_bar()
v5=Valume()
v6=Apl_close()
v1.start()
v2.start()
v3.start()
v4.start()
v5.start()
v6.start()
print("Excecuted Successfully")
from threading import Thread
import time
class Print_names(Thread):
    def run(self):
        names=["Rama","Krishna","Arjuna"]
        for i in names:
            print(i)
        time.sleep(2)
class Print_nums(Thread):
    def run(self):
        # for i in range(10):
        #     print(i)
            time.sleep(2)
class Print_sum(Thread):
    def run(self):
        a=100
        b=200
        c=a+b
        d=a-b
        print(d)
        print(c)
        time.sleep(2)
d1=Print_names()
d2=Print_nums()
d3=Print_names()
d4=Print_sum()
d1.start()
d2.start()
d3.start()
d4.start()