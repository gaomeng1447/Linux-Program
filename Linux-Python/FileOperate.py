#------------------------------------------------------------------
#  FileOperate.py
#
#  Created on: Obj 30, 2012
#  Author: Jason Liu <Jason.liu@finisar.com>
#  Description: File operation base class
#------------------------------------------------------------------

class FileOperate:

    def __init__(self):
        self.fileH = None
        
    def OpenFile(self, path, mode):
        pass
        
    def CloseFile(self):
        pass
    
