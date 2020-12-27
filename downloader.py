import os
from moviepy.editor import *
import pytube as p


def download(URL, name):
    for s in p.YouTube(URL).streams:
        print(s)
    stream = p.YouTube(URL).streams.get_by_itag(140)
    stream.download(filename=name)