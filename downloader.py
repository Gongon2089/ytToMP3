import os
import time
from moviepy.editor import *
import pytube as p


def download(URL, name):

    stream = p.YouTube(URL).streams.get_by_itag(22)
    stream.download(filename=name)

    video = VideoFileClip(filename=f"{name}.mp4")
    video.audio.write_audiofile(os.path.join(os.getcwd(), f"{name}.mp3"))
    video.close()
    time.sleep(5)
    os.remove(f"{name}.mp4")
