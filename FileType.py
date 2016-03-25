__author__ = 'qiaoyang'
import struct


class FileType:

    PE_HEADER_FORMAT = ''

    def __init__(self,filename):
        self.filename = filename
        self.data = open(self.filename,'rb').read()

        self.parse()

    def parse(self):
        pass




    def parse_header(self):
        pass




