#!/usr/bin/python3

from __future__ import unicode_literals
import youtube_dl
import sys
import time

ydl_opts = {
    'outtmpl': '~/Videos/Youtube/%(title)s-%(id)s.%(ext)s',
    'verbose': True,
}

if (len(sys.argv) != 2):
    sys.exit('use format :\nyoutube.py [link_vid]')

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    is_fail = True
    while is_fail:
        try:
            is_fail = False
            ydl.download([sys.argv[-1]])
        except youtube_dl.utils.DownloadError:
            is_fail = True
            time.sleep(1)
