#!/usr/bin/python3

from __future__ import unicode_literals
import youtube_dl
import sys

ydl_opts = {
    'outtmpl': '~/Videos/%(title)s-%(id)s.%(ext)s',
    'verbose': True,
}

if (len(sys.argv) != 2):
    sys.exit('use format :\nyoutube.py [link_vid]')

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([sys.argv[-1]])