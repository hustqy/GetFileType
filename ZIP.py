__author__ = 'qiaoyang'

class ZIP:

    MAGIC_NUM = '504B0506'
    MAGIC_FORMAT = ''
    FILE_TYPE = ['zip','docx','xlsx','pptx','apk']

    def __init__(self,data):
        self.data = data
        # print 'zip'

    def parse(self):
        pass