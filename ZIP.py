import zipfile
import xml.etree.ElementTree as ET
import os

class ZIP:

    MAGIC_NUM = '504B0506'
    MAGIC_FORMAT = ''
    FILE_TYPE = ['zip','docx','xlsx','pptx','apk']
    MAP_RELATIONS= {'word':'docx','excel':'xlsx','powerpoint':'pptx'}

    def __init__(self,data,path = None):
        self.data = data
        self.path = path
        self.parse()

    def parse(self):
        zf = zipfile.ZipFile(self.path, 'r')
        if 'AndroidManifest.xml' in zf.namelist():
            print os.path.basename(self.path),"apk "
        elif 'docProps/app.xml' in zf.namelist() :
            xmltree = ET.fromstring( zf.read('docProps/app.xml'))
            ns={'vt': 'http://schemas.openxmlformats.org/officeDocument/2006/extended-properties'}

            type = xmltree.find('vt:Application',ns)
            version = xmltree.find('vt:AppVersion',ns)
            if type is not None:
                for i in type.text.lower().split():
                    if i in ZIP.MAP_RELATIONS:
                        print os.path.basename(self.path),ZIP.MAP_RELATIONS[i]
                        break
            else:
                print os.path.basename(self.path),"zip file can't be recognized"

        else:
            print os.path.basename(self.path),"common zip"