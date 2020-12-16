
class InOutString(object):
    def __init__(self):
        self.s=""
    
    def getString(self):
        self.s=input()
    
    def printString(self):
        print(self.s.upper())

strObj = InOutString();
strObj.getString();
strObj.printString();