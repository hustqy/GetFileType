import struct
import os


class PE:

    MAGIC_NUM = '4D5A'
    MAGIC_FORMAT = ''
    FILE_TYPE = ['EXE','DLL']

    COFF_FORMAT = '<2h3I2H'
    def __init__(self,data,path = None):
        self.data = data
        self.path = path
        self.SIG_OFFSET = 0x3c
        self.Machine = None
        self.NumberOfSections = None
        self.TimeDateStamp =None
        self.PointerToSymbolTable =None
        self.NumberOfSymbols =None
        self.SizeOfOptionalHeader= None
        self.Characteristics= None
        self.parse_coff_header()


    def parse_coff_header(self):

        fp, = struct.unpack_from('I',self.data,self.SIG_OFFSET)

        signature, = struct.unpack_from('I',self.data,fp)

        if signature == int('0x4550',16):
            print os.path.basename(self.path), "PE"


        fp += struct.calcsize('I')
        (self.Machine,self.NumberOfSections,self.TimeDateStamp, self.PointerToSymbolTable,
         self.NumberOfSymbols,  self.SizeOfOptionalHeader, self.Characteristics) = struct.unpack_from(PE.COFF_FORMAT,
                                                                        self.data, fp)

        # print self.Machine,self.NumberOfSections,self.TimeDateStamp, self.PointerToSymbolTable,\
        #  self.NumberOfSymbols,  self.SizeOfOptionalHeader, self.Characteristics
        # if self.Characteristics == int('0x2000',16) :
        #     print 'GET FILE TYPE DLL'
        # elif self.Characteristics == 0x02:
        #     print 'GET FILE TYPE EXE'
        # else:
        #     print hex(self.Characteristics)
            # print 'GET FILE TYPE OTHER EXECUTABLE'
