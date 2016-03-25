import struct

class MSOffice:

    MAGIC_NUM = 'D0CF11E0A1B11AE1'
    MAGIC_FORMAT = ''
    FILE_TYPE = ['doc','xls','ppt','msg']

    def __init__(self,data):
        self.data = data
        # print 'MSOffice'

    def parse(self):
        pass