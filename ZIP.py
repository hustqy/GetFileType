__author__ = 'qiaoyang'

import zipfile
import xml.etree.ElementTree as ET
import os
class ZIP:

    MAGIC_NUM = '504B0506'
    MAGIC_FORMAT = ''
    FILE_TYPE = ['zip','docx','xlsx','pptx','apk']

    def __init__(self,data,path = None):
        self.data = data
        self.path = path
        self.parse()

    def parse(self):
        zf = zipfile.ZipFile(self.path, 'r')
        if 'AndroidManifest.xml' in zf.namelist():
            print "file apk"
        elif 'docProps/app.xml' in zf.namelist() :
            xmltree = ET.fromstring( zf.read('docProps/app.xml'))
            ns={'vt': 'http://schemas.openxmlformats.org/officeDocument/2006/extended-properties'}

            res = xmltree.find('vt:Application',ns)
            version = 0
            print res.text
        else:
            print "common zips"