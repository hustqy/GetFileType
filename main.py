import sys
import os
from FileType import FileType

def Main():
    args = sys.argv[1:]
    filepath = args[0]

    i = 0
    for filename in os.listdir(filepath):
        if i < 100:
            FileType(os.path.join(filepath,filename))
            i += 1
        else:
            break



if __name__ == '__main__':
    Main()