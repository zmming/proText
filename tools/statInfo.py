# -*- coding: utf-8 -*-
__author__ = 'zhaoming'

def statInfo_orig(lst=[]):
    data={}
    for item in lst:
        try:
            data[item]+=1
        except:
            data[item]=1
    return data

def statInfo(lst=[]):
    from collections import Counter
    return Counter(lst)

if __name__=='__main__':
    from cutWord import cutWordFromFile
    lst=cutWordFromFile('../corpus/test.txt')
    from collections import Counter
    data=statInfo(lst)
    sortLst=sorted(data,reverse=False)
    print data
    # for item in sortLst:
    #     print item,data[item]
