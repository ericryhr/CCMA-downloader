import os
import subprocess
import sys

def Usage():
    print("Usage: $python 3Cat_downloader.py mpdFile")
    exit(1)

if len(sys.argv) != 2:
    Usage()

fileName = sys.argv[1]
file = open(fileName)
urls = file.readlines()

for i, mpdUrl in enumerate(urls):
    mpdUrl = mpdUrl.strip()
    titol = f"{i}_{mpdUrl.split('/')[-3]}"
    print("Descarregant " + titol + " de " + mpdUrl)
    if not os.path.exists("./output/"):
        os.mkdir("./output/")
    subprocess.Popen(["youtube-dl", mpdUrl, '-o', f'./output/{titol}'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)