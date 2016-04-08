__author__ = 'qiaoyang'

import os
import struct


class FileType:

    PE_HEADER_FORMAT = ''

    MAGIC_NUMS = {'4D5A':'PE',
                  '504B':'ZIP',
                  'D0CF':'MSOffice',
                  '8950':'PNG',
                  'FFD8':'JPG or JPEG',
                  '5261':'RAR',
                  'FFFB':'mp3',
                  '4944':'mp3',
                  '5249':'avi',
                  '424D':'bmp',
                  '2550':'pdf',
                  '7B5C':'rtf',
                  '5265':'eml',
                  '0001':'ttf',
                  '3C68':'html',
                  '4749':'gif'
                }

    NEED_DEAL = ('PE','ZIP','MSOffice')

    def __init__(self,filename):
        self.filename = filename
        self.data = open(self.filename,'rb').read()
        self.path = filename
        self.parse()

    def parse(self):

        self.parse_magic()


    def parse_magic(self):

        magic_num, = struct.unpack_from('>H',self.data,0)
        key = '{0:04x}'.format(magic_num).upper()

        if FileType.MAGIC_NUMS.has_key(key):
            if FileType.MAGIC_NUMS[key] in FileType.NEED_DEAL:

                module = __import__(FileType.MAGIC_NUMS[key])

                CLASS_ = getattr(module, FileType.MAGIC_NUMS[key])

                CLASS_(self.data,self.path)
            else:
                print os.path.basename(self.path),FileType.MAGIC_NUMS[key]
        else:
            print os.path.basename(self.path),"other types can not be recognized"

            # else:
            #     print 'Got File Type %s'% FileType.MAGIC_NUMS[key]
        # else:
            # print "such file with %s can not be validated" %key




