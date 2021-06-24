from pytube import YouTube
SavePath = "/home/soham/YouTube Downloads"
print("Add links of video to the \'links.txt\' file")
file = open('links.txt','r')
links = file.read().split(',')
for i in links:
    #Check whether link valid or not
    try:
        yt = YouTube(i) #yt is an object
    except:
        print("Invalid Link")
        continue
#Print Tittle of the tittle
    title = yt.title
    print(title)
    stream = yt.streams.get_by_resolution("480p")
    if stream == None:
        stream = yt.streams.get_highest_resolution()
    stream.download(output_path=SavePath,max_retries=1)
    caption = yt.captions.get_by_language_code('en')
    if caption == None:
        print("No Caption")
    else:
        srt_captions = caption.generate_srt_captions()
        subtitles = open(SavePath+"/"+title+".txt","w")
        subtitles.write(srt_captions)
        subtitles.close()
        print("English Caption There")
        print()
print("Done")

