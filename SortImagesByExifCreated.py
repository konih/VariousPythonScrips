import datetime
import imghdr
import os
import time
from typing import Optional

import PIL.Image

from HelperFunctions import move_to_dir

MAX_FILE_SIZE = 1024  # KB
PATH = 'F:/NotSorted/'
EXIFPATH = 'F:/Sortiert/'
NOEXIFPATH = 'F:/Unsortierbar/'
ERRORPATH = 'F:/Fehlerhaft/'


def try_get_exifdate(fullpath: str) -> Optional[str]:
    with open(fullpath, 'rb') as image_file:
        try:
            created: Optional[str] = None
            img = PIL.Image.open(fullpath)
            exif_data = img._getexif()
            if (exif_data):
                if 0x9003 in exif_data:  # CreatedDateTime
                    created = exif_data[0x0132]
                elif 0x9004 in exif_data:  # DateTimeDigitized
                    created = exif_data[0x0132]
                elif 0x0132 in exif_data:  # DateTime
                    created = exif_data[0x0132]
            return created
        except:
            return None


numfiles = 0
exiffiles = 0
print("Strating the sort")
for file in os.listdir(PATH):
    print(file)
    numfiles += 1
    fullpath = os.path.join(PATH, file)
    # print(time.ctime(os.path.getctime(fullpath)))
    try:
        if imghdr.what(fullpath) == 'jpeg':
            datetime_exif = try_get_exifdate(fullpath)
            if datetime_exif:
                exiftime = datetime.datetime.strptime(str(datetime_exif), '%Y:%m:%d %H:%M:%S')
                exif_folder = '%s-%s/' % (exiftime.year, exiftime.month)
                move_to_dir(fullpath, os.path.join(EXIFPATH, exif_folder))
                exiffiles += 1
            else:
                ftime_file = time.gmtime(os.path.getctime(fullpath))
                ctime_dir = '%s-%s/' % (ftime_file.tm_year, ftime_file.tm_mon)
                move_to_dir(fullpath, os.path.join(NOEXIFPATH, ctime_dir))
        else:
            raise Exception('No JPG')
    except Exception as exception:
        print('Error in file %s: %s' % (fullpath, exception))
        move_to_dir(fullpath, ERRORPATH)

    print('Number of files ' + str(numfiles))
    print('Number of files with exif ' + str(exiffiles))

print("Finished")
