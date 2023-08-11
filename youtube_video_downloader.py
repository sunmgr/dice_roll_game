
from pytube import YouTube
print("---------------------------------")

get_link = 'https://www.youtube.com/watch?v=CAr0q_Nhj1I&list=RDGMEMHDXYb1_DDSgDsobPsOFxpAVMCAr0q_Nhj1I&start_radio=1'
youtube = YouTube(get_link)

vide = youtube.streams.all()
videos = list (enumerate(vide))
for vid in videos:
    print(vid)

print("---------------------------------")
strm = int(input("Enter the stream: "))
vide[strm].download()
print("download sucessfully")
