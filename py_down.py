from pytube import YouTube
import random
link=input('Please Enter the URL of the video -- \n')
try: 
	yt = YouTube(link)
except: 
	print("Connection Error")
stream = yt.streams.filter(file_extension='mp4').all()[2]
try: 
	print("Starting to download : " )
	print(yt.title)
	stream.download()
	
except: 
	print("Error while Downloading... Please Try Again !! \n")
