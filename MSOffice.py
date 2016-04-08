import struct
import ole
import sys
import os

class MSOffice:

    MAGIC_NUM = 'D0CF11E0A1B11AE1'
    MAGIC_FORMAT = ''
    FILE_TYPE = ['doc','xls','ppt','msg']

    def __init__(self, data, path=None):

        self.data = data
        self.path = path
        self.prove_header()
        self.parse()

    def prove_header(self):
        top8 = struct.unpack_from('8B',self.data,0)

        assert ''.join(['{0:02x}'.format(i) for i in top8]).upper() == MSOffice.MAGIC_NUM, "not Msoffice file"

    def parse(self):
        ole_obj = ole.OleFileIO(self.data, raise_defects=ole.DEFECT_INCORRECT)
        meta = ole_obj.get_metadata()
        print os.path.basename(self.path),meta.creating_application
        # if len(self.data) < 512:
        #     logging.warning('document is less than 512 bytes')
        # self.header = Header(self.data[:512],self.path)


if __name__ == "__main__":
    args = sys.argv[:]
    data = open(args[1],'rb').read()

    obj = MSOffice(data,args[1])

