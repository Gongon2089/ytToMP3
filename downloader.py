import os
import time
from moviepy.editor import *
import pytube as p
import getpass


def download(URL, name):

    ytObj = p.YouTube(URL)
    stream = ytObj.streams.get_by_itag(22)
    if stream is None:
        stream = ytObj.streams.get_by_itag(18)
    stream.download(filename=name)
    enter = False
    if name == "":
        files = os.listdir()
        for f in files:
            if ".mp4" in f:
                enter = True
                name = f

    if not enter:
        video = VideoFileClip(filename=f"{name}.mp4")
    else:
        video = VideoFileClip(filename=name)
    video.audio.write_audiofile(f'C:\\Users\\{getpass.getuser()}\\Music\\{name.replace(".mp4", "")}.mp3')
    video.close()
    time.sleep(5)
    if not enter:
        os.remove(f"{name}.mp4")
    else:
        os.remove(name)