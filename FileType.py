__author__ = 'qiaoyang'


import struct


class FileType:

    PE_HEADER_FORMAT = ''

    MAGIC_NUMS = {'4D5A':'PE',
                  '504B':'ZIP',
                  'D0CF':'MSOffice',
                  '8950':'PNG',
                  'FFD8':'JPG',
                  '5261':'RAR',
                  'FFFB':'mp3',
                  '4944':'mp3',
                  '5249':'avi',
                  '424D':'bmp'
                }

    NEED_DEAL = ('PE','ZIP','MSOffice')

    def __init__(self,filename):
        self.filename = filename
        self.data = open(self.filename,'rb').read()

        self.parse()

    def parse(self):

        self.parse_magic()




    def parse_magic(self):

        magic_num, = struct.unpack_from('>H',self.data,0)
        key = hex(magic_num).strip('0x').upper()

        if FileType.MAGIC_NUMS.has_key(key):
            if FileType.MAGIC_NUMS[key] in FileType.NEED_DEAL:

                module = __import__(FileType.MAGIC_NUMS[key])

                CLASS_ = getattr(module, FileType.MAGIC_NUMS[key])

                CLASS_(self.data)

            # else:
            #     print 'Got File Type %s'% FileType.MAGIC_NUMS[key]
        # else:
            # print "such file with %s can not be validated" %key




