import time
class vlc:
    def apl_open(self):
        print("Vlc apl opened")
        time.sleep(3)
    def video_start(self):
        print("Video started playing")
        time.sleep(3)
    def audio_start(self):
        print("Audio started playing")
        time.sleep(3)
    def pro_bar(self):
        print("Progress bar is activated")
        time.sleep(3)
    def valume(self):
        print("Volume is increasing")
        time.sleep(3)
    def apl_close(self):
        print("Vlc apl closed")
        time.sleep(3)
v=vlc()
v.apl_open()
v.video_start()
v.audio_start()
v.pro_bar()
v.valume()
v.apl_close()