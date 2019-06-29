import json
import os
import pprint

from exif import Image
import exifread

ROOT = 'F:\\NotSorted\\'
for file in os.listdir(ROOT):
    print(file)
    try:

    except:
        pass

with open('F:\\Fehlerhaft\\10539671.jpg', 'rb') as image_file:
    image = Image(image_file)
    print(dir(image))