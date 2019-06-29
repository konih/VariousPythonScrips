import os.path

from filehash import FileHash

from HelperFunctions import move_to_dir

FOLDER = 'F:/Sortiert/'


def findDup(parentFolder):
    # Dups in format {hash:[names]}
    dups = {}
    md5hasher = FileHash('md5')
    for dirName, subdirs, fileList in os.walk(parentFolder):
        print('Scanning %s...' % dirName)
        for filename in fileList:
            # Get the path to the file
            path = os.path.join(dirName, filename)
            # Calculate hash
            file_hash = md5hasher.hash_file(path)
            # Add or append the file path
            if file_hash in dups:
                fullpath = os.path.join(dirName, filename)
                destpath = dirName.replace('Sortiert', 'Duplikate')
                move_to_dir(fullpath, destpath)
            else:
                dups[file_hash] = [path]
    return dups


if __name__ == "__main__":
    findDup(FOLDER)
