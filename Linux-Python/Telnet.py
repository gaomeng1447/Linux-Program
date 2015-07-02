'''
Created on 2015-03-10
@author: gaomwang@cisco.com
'''
import time
import telnetlib

class Telnet:
    count = 0  #class variable, equal c++ static member
    def __init__(self, host, port=23):
        pot = int(port)#+ 2000
        try:
            self.tn = telnetlib.Telnet(host, pot)
        except:
            print "Exception at Telnet init, occupied?\n"
        Telnet.count += 1
    
    def __del__(self):
        Telnet.count -= 1
        self.close()
        
    def close(self):
        self.tn.close()
    
    def read(self, delay = 0.5):
        time.sleep(delay)
        return self.tn.read_very_eager()
    
    def write(self, str):
        time.sleep(0.1)
        bk = self.tn.write(str)
        time.sleep(0.1)
        return bk
    
    def read_until(self, match, timeout=2):
        #match = '*Password:'
        try:
            bk = self.tn.read_until(match, timeout)
        except:
            print 'wait you given time, but cannot find the given string format! \n'
        finally:
            return bk
    
    def expect(self, expt, timeout = 2):
        try:
            bk = self.tn.expect(expt, timeout)
        except Exception as e:
            print e
        finally:
            return bk
    
    def howMany(self):
        # calculates the Number of the instance of Telnet.
        return Telnet.count

if __name__ == '__main__':
    host = '10.74.88.235'
    #port = 23
    bb = Telnet(host, 2018)
    time.sleep(3)
    bb.write(' \n')
    pp = bb.read()
    print pp
    time.sleep(1800)
    #del bb
    print 'Closed successfully!'
