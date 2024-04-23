from pytube import YouTube
from sys import argv
link = argv[1]
video = YouTube(link)
folder = input("Where to download video to: ")
vid_download = video.streams.get_highest_resolution()
print("Downloading...")
vid_download.download(folder)
print(f"Downloaded: {video.title} to {folder}")