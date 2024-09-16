# cli_music_downloader
Downloads the user entered song by converting the video file from youtube into an mp3 audio file and stores it in a preferred location.

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
