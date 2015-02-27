__author__ = 'Lyan'

from PIL import Image

def printIMG():
    f=Image.open('/Workspace/test.png')
    print f.format,f.size,f.mode
    return 0

def printText():
    print 'This is Module Main'
    return 0

if __name__ == '__main__':
    printIMG()
