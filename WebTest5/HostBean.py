__author__ = 'Lyan'

class HostBean(object):
    def __init__(self):
        self.__ip='NULL'
        self.__group='NULL'

    def setip(self,ip):
        self.__ip=ip

    def setgroup(self,group):
        self.__group=group

    def getip(self):
        return self.__ip

    def getgroup(self):
        return self.__group


if __name__ == '__main__':
    host=HostBean()
    host.setip('10.6.1.1')
    print host.getip()
    print "this is a py to gether host info from DB"
