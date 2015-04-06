# -*- coding: utf-8 -*-
__author__ = 'zhaoming'

def cutWordFromFile(filename):
    import sys
    sys.path.append('..')
    from baseLib.getCharCode import getCharType
    import jieba
    import codecs
    charType=getCharType(filename)
    with codecs.open(filename,'r',charType) as fin:
        con=fin.read()

    seg_list=jieba.cut(con)
    return seg_list


if __name__=='__main__':
    seg_list=cutWordFromFile('../corpus/test.txt')
    print '/'.join(seg_list)
    print 'end...'


