import pytube

link = input("Enter youtube video URl:-")

#link of the video
yt = pytube.YouTube(link)
yt.streams.first().download()
print("downloaded",link)