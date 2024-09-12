"""

Hello There! :D

The Program does the following:

1. Gets the video_id for the user entered song using the youtube_api library
2. Downloads the specific song using the pytube library(in mp4 format)
3. Converts the mp4 format into mp3 using the FFmpeg library
4. Deleted the mp4 video

Make sure you have FFmpeg installed on your computer before running the program.

You also need a YouTube API Key to access the video IDs

pip install youtube-data-api
pip install pytube

"""


import os
from youtube_api import YouTubeDataAPI
from pytube import YouTube
from moviepy.editor import *


print()
song =  input("Enter name of the song: ")
artist = input("Enter name of the artist: ")
print()

query = song + " " + artist

#Replace API Key
YT_KEY = "Enter_Your_Youtube_API_Key"
yt = YouTubeDataAPI(YT_KEY)

searches = yt.search(q=query, max_results=5)

yt = YouTube('http://youtube.com/watch?v=' + searches[0]["video_id"])

print("Downloading video file: " + yt.title)
print()
print("Current Video ID: " + searches[0]["video_id"])

ind = yt.streams.filter(progressive=True)[0].itag

stream = yt.streams.get_by_itag(ind)
x = stream.download(output_path="/path/to/video/file")

print("Video File has been Downloaded")
print()
print("Converting to audio file using FFmpeg and MoviePy")
print()

#The Video file will be deleted instantly after conversion

video = VideoFileClip(os.path.join("same/path/to/video/file" + yt.title + ".mp4"))
video.audio.write_audiofile(os.path.join("/store/audio/file/" + yt.title + ".mp3"))

print()

print("Deleting video file")
print()

os.remove("/same/path/to/video/file" + yt.title + ".mp4")

print("Download process Has Been Completed")

#-----
