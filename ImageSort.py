import datetime
import imghdr
import os, os.path
import os, time, shutil, sys
from typing import Optional

import exifread

from exif import Image

MAX_FILE_SIZE = 1024  # KB
PATH = 'F:/NotSorted/'
EXIFPATH = 'F:/Sortierbar/'
NOEXIFPATH = 'F:/Unsortierbar/'
ERRORPATH = 'F:/Fehlerhaft/'


def try_get_exifdate(fullpath: str) -> Optional[str]:
    with open(fullpath, 'rb') as image_file:
        try:
            tags = exifread.process_file(image_file)
            for tag in tags.keys():
                if str(tag).find('DateTimeOriginal') > 0:
                    return tags[tag]
        except:
            return None


def move_to_dir(fullpath: str, dest: str):
    if not os.path.isdir(dest):
        os.mkdir(dest)
    print('Moving from %s to %s' % (fullpath, dest))
    os.rename(fullpath, os.path.join(dest, os.path.basename(fullpath)))


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
