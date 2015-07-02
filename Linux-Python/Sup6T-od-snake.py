'''
Created on 2015-05-21
@author: gaomwang@cisco.com
'''
import sys, os
import time, datetime
from Telnet import Telnet
sys.path.append(r"C:\Cisco_File\Python_Library\File")
from TxtFileOperate import TxtFileOperate

class Sup6T_od_snake(Telnet):
    confirm_times = 1
    cwd = os.getcwd()
    
    def __init__(self, host, port=23):
        Telnet.__init__(self, host, port)
        self.conf_cmd = []
        print "Sup6T_od_snake init ok"
    
    def read_cmds(self):
        path = 'C:\\Cisco_File\\Daily_Test\\Month_06\\10\\path-2.txt'
        mode = 'r'
        cmdList = []
        handle = TxtFileOperate()#handle is an instance of ...
        handle.OpenFile(path, mode)
        ele = handle.ReadLinesFromTxtFile()
        cmdList.append(ele)
        self.conf_cmd = cmdList[0]
        print self.conf_cmd
        for cmd in self.conf_cmd:
            print cmd
    
    def write_cmds(self):
        for cmd in self.conf_cmd:
            style = self.style_cmds(cmd)
            print 'begin write command to Router:', cmd, style, datetime.datetime.now()
            self.write(cmd)
            if style == 'long':
                time.sleep(60*7)
            elif style == 'middle':
                time.sleep(1)
            elif style == 'short':
                time.sleep(0.1)
            fb = self.read()
            print fb
            #make sure the command feedback is right
            if self.confirm_cmds():
                continue
            else:
                print "write the cmd, confirm wrong:", cmd
                Sup6T_od_snake.__del__()
                break
    
    def style_cmds(self, cmd):
        str = cmd
        rtn = ''
        if 'sn activate' in cmd:
            rtn = 'long'
        elif 'sn display' in cmd:
            rtn = 'middle'
        elif 'sn path' in cmd:
            rtn = 'short'
        else:
            rtn = '\n'
            raise ValueError
        return rtn
    
    def confirm_cmds(self):
        keyword = 'SP3>'
        self.write('\n')
        str = self.read(1)
        if keyword in str:
            print 'confirm ok: ', Sup6T_od_snake.confirm_times
            Sup6T_od_snake.confirm_times+=1
            return True
        else:
            return False
    
    def __del__(self):
        Telnet.__del__()

if __name__ == '__main__':
    host = '10.74.88.26'
    port = 2012
    #port = 23
    obj = Sup6T_od_snake(host, port)
    obj.read_cmds()
    obj.write_cmds()
    del obj
    print 'write successfully!'
    print 'init version of git'

