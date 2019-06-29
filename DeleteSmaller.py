import os, os.path

MAX_FILE_SIZE = 1024 #KB


for root, _, files in os.walk("F:/"):
    for f in files:
        fullpath = os.path.join(root, f)
        try:
            if os.path.getsize(fullpath) < MAX_FILE_SIZE * 1024:   #set file size in kb
                print fullpath
                os.remove(fullpath)
        except WindowsError:
            print "Error" + fullpath