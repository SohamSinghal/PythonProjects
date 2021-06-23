from pytube import YouTube
SavePath = "~/Videos"
print("Add links of video to the \'links.txt\' file")
file = open('links.txt','r')
links = file.read().split(',')
for i in links:
    #Check whether link valid or not
    try:
        yt = YouTube(i)
    except:
        print("Invalid Link")
        continue
#Print Tittle of the tittle
    print(yt.title)
