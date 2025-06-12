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
lines = file.readlines()

for i, line in enumerate(lines):
    line = line.strip().split(maxsplit=1)
    mpdUrl = line[0]
    titol = line[1]
    # titol = f"{i}_{mpdUrl.split('/')[-3]}"
    print("Descarregant " + titol + " de " + mpdUrl)
    if not os.path.exists("./output/"):
        os.mkdir("./output/")
    subprocess.Popen(["youtube-dl", mpdUrl, '-o', f'./output/{titol}'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)