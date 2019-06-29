import os


def move_to_dir(fullpath: str, dest: str):
    print('Moving from %s to %s' % (fullpath, dest))
    if not os.path.isdir(dest):
        os.mkdir(dest)
    os.rename(fullpath, os.path.join(dest, os.path.basename(fullpath)))