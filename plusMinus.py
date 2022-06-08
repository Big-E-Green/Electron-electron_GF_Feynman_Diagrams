from functions import *
from topologicalInequiv import *
from copy import deepcopy

def posneg(n):
    def comp(jee,temp):
        for i in temp:
            if i[1]==j[0]:
                j[0],j[1],i[0],i[1]=j[0],i[1],i[0],j[1]
                return temp
    swaps=[]
    kiss=distinctDiagrams(n)
    kisss=deepcopy(kiss)
    for i in kiss:
        sort=0
        tmp=i
        sw=0
        while sort<len(i):
            for j in tmp:
                if j[0]==j[1]:
                    sort=sort+1
                    tmp.remove(j)
                if j[0]!=j[1]:
                    w=comp(j,tmp)
                    tmp=w
                    sw=sw+1
        swaps.append(sw)
    posNeg=[]
    for i in swaps:
        if (i % 2) == 0:
            posNeg.append('P')
        else:
            posNeg.append('N')
    final=[]
    c=0
    for i in kisss:
        final.append(i)
        final.append(posNeg[c])
        c=c+1
    return final