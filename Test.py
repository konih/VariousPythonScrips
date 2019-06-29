import json
import os
import pprint

from exif import Image
import PIL.Image

ROOT = 'F:\\Fehlerhaft\\'
for file in os.listdir(ROOT):
    full_path = os.path.join(ROOT, file)
    print(file)

    try:
        img = PIL.Image.open(full_path)
        exif_data = img._getexif()
        if (exif_data):
            ret = {}
            if 0x9003 in exif_data: #CreatedDateTime
                created = exif_data[0x0132]
            elif 0x9004 in exif_data: #DateTimeDigitized
                created = exif_data[0x0132]
            elif 0x0132 in exif_data: #DateTime
                created = exif_data[0x0132]
            print(created)
        else:
            print("Not possibru")
    except Exception as E:
        print(E)
        pass

with open('F:\\Fehlerhaft\\10539671.jpg', 'rb') as image_file:
    image = Image(image_file)
    print(dir(image))