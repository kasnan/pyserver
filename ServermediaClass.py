from pytube import YouTube
from os import path as pt
import os

class ServerData:
    path = "C:/Users/kasna/Documents/vsworkspace/Pyworkspace/pyserver/trailers/"  
    
    def __init__(self):
        pass
    def __init__(self,file_name):
        self.file_name=file_name

    def setFileName(self,file_name):
        self.file_name=file_name

    def downFromUrl(self):
        print("download video")
        self.setFileName()
        f = open(self.path+self.file_name+".txt","r")
        line = f.readline()
        f.close()

        yt = YouTube(line)
        print(yt.title)
        yt.set
        yt.streams.filter(progressive=True, file_extension="mp4")\
        .order_by("resolution")\
        .desc()\
        .first()\
        .download(self.path)

        for filename in os.listdir(self.path):
            if filename == yt.title+".mp4":
                print(filename)
                os.rename(self.path+filename,self.path+self.file_name+".mp4")