import struct
import olefile

class MSOffice:

    MAGIC_NUM = 'D0CF11E0A1B11AE1'
    MAGIC_FORMAT = ''
    FILE_TYPE = ['doc','xls','ppt','msg']

    def __init__(self,data,path = None):
        self.data = data
        # print 'MSOffice'
        self.parse()
    def parse(self):
        ole = olefile.OleFileIO(self.data, raise_defects=olefile.DEFECT_INCORRECT)
        # print('Non-fatal issues raised during parsing:')
        # if ole.parsing_issues:
        #     for exctype, msg in ole.parsing_issues:
        #         print('- %s: %s' % (exctype.__name__, msg))
        # else:
        #     print('None')

        meta = ole.get_metadata()
        print meta.creating_application
