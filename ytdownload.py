from pytube import YouTube

link = input("Link: ")

yt = YouTube(link)
ys = yt.streams.get_highest_resolution()
print("indiriliyor")
ys.download()
print("indirildi")