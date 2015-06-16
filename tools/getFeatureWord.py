# -*- coding: utf-8 -*-
__author__ = 'zhaoming'

import jieba
import jieba.analyse

def getFeatureWord(content,topK):
    return jieba.analyse.extract_tags(content, topK=topK, withWeight=True)

def getFeaturWordByTextRank(con, topK):
    return jieba.analyse.textrank(con, topK=topK, withWeight=True)


if __name__=='__main__':
    from baseLib.getCharCode import getCharType
    import codecs
    charType=getCharType('../corpus/test3.txt')
    #with codecs.open('../corpus/test2.txt','r',charType) as fin:
    #    con=fin.read()
    with open('../corpus/test3.txt') as fin:
        con=fin.read()
    word_lst=getFeatureWord(con.decode(charType,'ignore').encode('utf-8'), 100)
    #print '/'.join(word_lst)
    #for x,w in getFeaturWordByTextRank(con):
    #    print x,w
    for x,w in word_lst:
        print x,w