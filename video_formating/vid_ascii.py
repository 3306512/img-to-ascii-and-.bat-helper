from typing import Optional
from video_formating.utils.image_utils import image_to_ascii, out_file
path_ = out_file
# Future me should make this for .gif, and fix some bugs


class ImageAnimation:
    def __init__(self, path):
        self.path = path

    def convert_to_ascii(self) -> Optional[str]:
        image_to_ascii(self.path)
        return None


class BatchAnimation:
    def __init__(self, img: ImageAnimation):
        self.img = img
        img.convert_to_ascii()
        pattern_top = """        
::output
@echo OFF
Title output
color 0A
echo.
:output
ping localhost -n 1 >nul
cls\n
"""
        with open(path_, 'r') as f1:
            with open('output/batch/output.bat', 'w') as f2:
                f2.write(pattern_top)
                for line in f1:
                    if line.strip() != '':
                        f2.write(f"echo {line}")
                f2.write('pause >nul')
