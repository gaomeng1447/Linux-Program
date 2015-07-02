#------------------------------------------------------------------
#  TxtFileOperate.py
#
#  Created on: Obj 30, 2012
#  Author: Jason Liu <Jason.liu@finisar.com>
#  Description: TxtFile operation class
#------------------------------------------------------------------

from FileOperate import FileOperate

class TxtFileOperate(FileOperate):

    def OpenFile(self, path, mode):
        try:
            if self.fileH:
                self.CloseFile()
            self.fileH = open(path, mode)
        except IOError, e:
               print e
               return False
        else:
            return True
            
    def ReadLinesFromTxtFile(self):
        if    None != self.fileH:
            lines = self.fileH.readlines()
            return lines
        else:
            print "open file first!"
        
    def AppendLineToTxtFile(self, line):
        if    None != self.fileH:
            self.fileH.write(line)
        else:
            print "open file first!"
            
    def ReplaceLineToTxtFile(self, line):
        import re
        p = re.compile(r'\s+')
        
        if    None != self.fileH:
            lines = self.ReadLinesFromTxtFile()
            itemNum = 0
            for item in lines:
                readKeyWord = p.split(item)
                writeKeyWord = p.split(line)
                if(0 == cmp(writeKeyWord[0],readKeyWord[0])):
                    lines[itemNum] = line
                    break
                itemNum += 1
            if    itemNum == len(lines):
                self.AppendLineToTxtFile(line)
            else:
                self.fileH.truncate(0)
                self.AppendLinesToTxtFile(lines)
        else:
            print "open file first!"
        
    def AppendLinesToTxtFile(self, lines):
        if    None != self.fileH:
            self.fileH.writelines(lines)
        else:
            print "open file first!"
            
    def CloseFile(self):
        try:
            if self.fileH:
                self.fileH.close()
                self.fileH = None
        except IOError, e:
            print e

