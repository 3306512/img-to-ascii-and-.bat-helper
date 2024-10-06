from video_formating.vid_ascii import BatchAnimation, ImageAnimation
# should make it better


def main():
    # put some png in input/ dir before run main.py
    img = ImageAnimation('XOsX.gif')
    BatchAnimation(img)


if __name__ == '__main__':
    main()
