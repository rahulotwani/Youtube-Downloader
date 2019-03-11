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
	yt = YouTube('http://youtube.com/watch?v=9bZkp7q19f0')
    	yt.streams.all()
   	print("Dowmload is Complete\n")
	
except: 
	print("Error while Downloading... Please Try Again !! \n")
