import subprocess
import os
import time
import mimetypes
from shutil import which


def checkffmpeg():
    if which("ffmpeg"):
        return
    print(
        "\033[31m Please install ffmpeg with your package manager, or download the binaries into the current folder."
    )
    exit(1)


def createFolders(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)


def findVideoFiles(list):
    for fileName in os.listdir("input"):
        if mimetypes.guess_type(fileName)[0].startswith("video"):
            list.append(fileName)


def crfValueInput():
    while True:
        try:
            crf = int(input("\033[37m Please enter a CRF value. [0-51]: "))
        except ValueError:
            print("\033[31m That isn't a number between 0 - 51.")
            continue
        if (crf < 0) or (crf > 51):
            print("\033[31m That isn't a number between 0 - 51.")
            continue
        else:
            return crf


def main():
    print(
        "\033[34m",
        r"""
        _     _ ____                                             
 __   _(_) __| |___ \ ___ ___  _ __ ___  _ __  _ __ ___  ___ ___ 
 \ \ / / |/ _` | __) / __/ _ \| '_ ` _ \| '_ \| '__/ _ \/ __/ __|
  \ V /| | (_| |/ __/ (_| (_) | | | | | | |_) | | |  __/\__ \__ \
   \_/ |_|\__,_|_____\___\___/|_| |_| |_| .__/|_|  \___||___/___/
                                        |_|                      
                                            by obvRedwolf
    """,
    )
    videoFiles = []
    checkffmpeg()
    createFolders("input")
    createFolders("compressed")
    findVideoFiles(videoFiles)
    if not videoFiles:
        print(
            "\033[31m No video files were detected in the input folder. Please insert video files into the input folder and try again."
        )
        time.sleep(1)
        exit(2)
    print(
        "\033[32m The files below have been detected as video files. These files will be compressed."
    )
    for fileName in videoFiles:
        print("\033[37m", fileName)
    print(""" \033[37m
    How do you want your videos compressed?
    0 = lossless
    17 = visually lossless
    23 = recommended for compression
    28 = ultra compression
    51 = worst quality
    """)
    crfValue = crfValueInput()
    input("The files will be compressed now. \n ...press any key to start...")
    for file in videoFiles:
        print("\033[32m", file)
        cmd = (
            'ffmpeg -i ".\\input\\'
            + file
            + '" -c:v libx264 -crf '
            + str(crfValue)
            + ' -c:a copy ".\\compressed\\'
            + file
            + '"'
        )
        print("\033[0m", cmd)
        subprocess.run(cmd)
    print("\033[32m Your video files have been compressed!")
    input("...press any key to exit...")


if __name__ == "__main__":
    main()
