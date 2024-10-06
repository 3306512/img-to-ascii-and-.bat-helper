import os
import shutil
import sys

import cv2
from typing import Optional

from PIL import Image

# you can change grayscale, for example reverse this one so the black will be white etc.
GRAYSCALE = " :-=+*#%@"
COEF = 255 / (len(GRAYSCALE) - 1)
out_file = 'output/ascii.txt'


def extract_frames(inGif, outFolder):
    folder = sys.path[0] + '\\' + outFolder
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

    frame = Image.open(inGif)
    nframes = 0
    while frame:
        frame.save( '%s/%s-%s.png' % (outFolder, os.path.basename(inGif), nframes), 'PNG')
        nframes += 1
        try:
            frame.seek(nframes)
        except EOFError:
            break
    return True


# Future me should make this for .gif files, probably split it in frames and then convert frames to ascii
def image_to_ascii(path):
    """
        thanks to https://habr.com/ru/articles/790318/, func made to convert .png files to ascii .txt
        you can decrease step in the for-loop(s) to increase quality of ascii image, for example 8-4 and 4-2
        in second loop will make quality better and increase quantity of symbols
    :param path: path to .png
    :return: ---
    """
    extract_frames(path, 'output/frames')
    for i in range(len([name for name in os.listdir('output/frames')])):
        new_path = f'{sys.path[0]}\\output\\frames\\{path}-{i}.png'
        print(new_path)
        image = cv2.imread(new_path)
        height, width, channels = image.shape
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        with open(out_file, 'a') as f:
            for x in range(0, width - 1, 8):
                string = ''
                for y in range(0, height - 1, 4):
                    try:
                        string += GRAYSCALE[len(GRAYSCALE) - int(gray_image[x, y] / COEF) - 1]
                        continue
                    except IndexError:
                        pass
                if len(string) != 0:
                    f.write(string + '\n')
            f.write("""
ping localhost -n 1 >nul
cls
            """)
