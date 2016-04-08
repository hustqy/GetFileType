import sys
import os
from FileType import FileType

def Main():
    args = sys.argv[1:]
    filepath = args[0]

    for filename in os.listdir(filepath):

        try:
            FileType(os.path.join(filepath,filename))
        except:
            print filename,"unable to recognize file type"





if __name__ == '__main__':
    Main()