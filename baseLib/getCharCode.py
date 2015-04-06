# -*- coding: utf-8 -*-
__author__ = 'zhaoming'

def getCharType(filename):
    from chardet.universaldetector import UniversalDetector
    #创建一个检测对象
    detector = UniversalDetector()
    with open(filename,'rb') as fin:
        for line in fin.readlines():
            detector.feed(line)
            if detector.done:break
        detector.close()
    print detector.result


if __name__=='main':
    #print 'start getCharType'
    print getCharType('../corpus/test.txt')
    #print 'end getCharType'