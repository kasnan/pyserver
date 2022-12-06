import socket
from pytube import YouTube
from os import path as pt
from threading import Thread
import os
import time

global conn

soc = socket.socket()

host = "127.0.0.1"
port = 2004
soc.bind((host, port))
soc.listen(5)
soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


path = "C:/Users/kasna/Documents/vsworkspace/Pyworkspace/pyserver/trailers/"
#path = "C:/Users/kasna/Documents/workspace/py/pyserver/trailers/"


def getJason(file_name,conn):
    print("getJason")

    length_of_message = int.from_bytes(conn.recv(2), byteorder='big')
    msg = conn.recv(length_of_message).decode("UTF-8")
    
    if msg == "subtype?":
        print(msg)
        if pt.exists(path+file_name+".json"):
            print("json")
            message_to_send = "json".encode("UTF-8")
            conn.send(len(message_to_send).to_bytes(2, byteorder='big'))
            conn.send(message_to_send)

            with open(path+file_name+".json", "rb") as js:
                data = js.read(1024) #1024바이트 읽는다
                data_transferred = 0
                while data: #데이터가 없을 때까지
                    data_transferred += conn.send(data) #1024바이트 보내고 크기 저장
                    data = js.read(1024) #1024바이트 읽음
                print("전송완료 %s, 전송량 %d" %(filename, data_transferred))
        elif pt.exists(path+file_name+".smi"):
            print("smi")
            message_to_send = "smi".encode("UTF-8")
            conn.send(len(message_to_send).to_bytes(2, byteorder='big'))
            conn.send(message_to_send)

            with open(path+file_name+".smi", "rb") as js:
                data = js.read(1024) #1024바이트 읽는다
                data_transferred = 0
                while data: #데이터가 없을 때까지
                    data_transferred += conn.send(data) #1024바이트 보내고 크기 저장
                    data = js.read(1024) #1024바이트 읽음
                print("전송완료 %s, 전송량 %d" %(filename, data_transferred))
        elif pt.exists(path+file_name+".srt"):
            print("srt")
            message_to_send = "srt".encode("UTF-8")
            conn.send(len(message_to_send).to_bytes(2, byteorder='big'))
            conn.send(message_to_send)

            with open(path+file_name+".srt", "rb") as js:
                data = js.read(1024) #1024바이트 읽는다
                data_transferred = 0
                while data: #데이터가 없을 때까지
                    data_transferred += conn.send(data) #1024바이트 보내고 크기 저장
                    data = js.read(1024) #1024바이트 읽음
                print("전송완료 %s, 전송량 %d" %(filename, data_transferred))

def downFromUrl(file_name):
    print("download vid")
    f = open(path+file_name+".txt","r")
    line = f.readline()
    print(line)
    f.close()

    yt = YouTube(line)
    print(yt.title)
    yt.streams.filter(progressive=True, file_extension="mp4")\
    .order_by("resolution")\
    .desc()\
    .first()\
    .download(path)

    for filename in os.listdir(path):
        if filename == yt.title+".mp4":
            print(filename)
            os.rename(path+filename,path+file_name+".mp4")

def getMovie(file_name, conn):
    print("getMovie")
    print(path+file_name+".mp4")
    if not pt.exists(path+file_name+".mp4"):
        downFromUrl(file_name)
    
    global data_transferred
    data_transferred=0
    #send video
    with open(path+file_name+".mp4", "rb") as video:
        data = video.read(1024) #1024바이트 읽는다
        while data: #데이터가 없을 때까지
            data_transferred += conn.send(data) #1024바이트 보내고 크기 저장
            data = video.read(1024) #1024바이트 읽음

        print("전송완료 %s, 전송량 %d" %(filename, data_transferred))

    if pt.exists(path+file_name+".mp4"):
        os.remove(path+file_name+".mp4")

while True:
    conn, addr = soc.accept()
    print("Got connection from",addr)

    length_of_message = int.from_bytes(conn.recv(2), byteorder='big')
    msg = conn.recv(length_of_message).decode("UTF-8")
    print(msg)


    # Note the corrected indentation below
    if "check"in msg:
        message_to_send = "bye".encode("UTF-8")
        conn.send(len(message_to_send).to_bytes(2, byteorder='big'))
        conn.send(message_to_send)
    elif "Stop" in msg:
        conn.close()
        break
    elif "json" in msg:
        filename=msg[5:]
        getJason(filename,conn)
        print("send message")
        
    elif "mp4" in msg:
        filename=msg[4:]
        getMovie(filename,conn)

    elif "subtype?" in msg:
        print("miss-sink")
        conn.close()

print("Exitting Program!")
soc.close()