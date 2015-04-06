# -*- coding: utf-8 -*-
__author__ = 'zhaoming'

def statInfo(lst=[]):
    data={}
    for item in lst:
        try:
            data[item]+=1
        except:
            data[item]=1
    return data

if __name__=='__main__':
    #from cutWord import cutWordFromFile
    lst=cutWordFromFile('../corpus/test.txt')
    data=statInfo(lst)