from pytube import YouTube

line = "https://www.youtube.com/watch?v=Xbzb2ASpWlc&t=224s"
yt = YouTube(line).streams.filter(progressive=True, file_extension="mp4")
yt_high = yt.get_highest_resolution()
yt_low = yt.get_lowest_resolution()
print(yt_low)
