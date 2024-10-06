import cv2
from typing import Optional

# you can change grayscale, for example reverse this one so the black will be white etc.
GRAYSCALE = " :-=+*#%@"
COEF = 255 / (len(GRAYSCALE) - 1)
out_file = 'output/ascii.txt'


# Future me should make this for .gif files, probably split it in frames and then convert frames to ascii
def image_to_ascii(path):
    """
        thanks to https://habr.com/ru/articles/790318/, func made to convert .png files to ascii .txt
        you can decrease step in the for-loop(s) to increase quality of ascii image, for example 8-4 and 4-2
        in second loop will make quality better and increase quantity of symbols
    :param path: path to .png
    :return: ---
    """
    im = cv2.imread(path)
    height, width, channels = im.shape
    gray_im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    with open(out_file, 'w') as f:
        for x in range(0, width - 1, 8):
            string = ''
            for y in range(0, height - 1, 4):
                try:
                    string += GRAYSCALE[len(GRAYSCALE) - int(gray_im[x, y] / COEF) - 1]
                    continue
                except IndexError:
                    pass
            if len(string) != 0:
                f.write(string + '\n')

