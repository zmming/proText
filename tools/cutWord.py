# -*- coding: utf-8 -*-
__author__ = 'zhaoming'

import jieba
def cutWord(con):
    seg_list=jieba.cut(con)
    return seg_list


if __name__=='__main__':
    import codecs
    from baseLib.getCharCode import getCharType
    charType=getCharType('../corpus/test.txt')
    with codecs.open('../corpus/test.txt','r',charType) as fin:
        con=fin.read()

    print '/'.join(cutWord(con))

