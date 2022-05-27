from RemovingDisconnected import *
from generator import *
import random
import math
import itertools
from copy import deepcopy

gen=genny(2)
nums=[]
for i in gen:
    for j in i:
        nums.append(j)
#print(nums)

lev=list(itertools.combinations(nums,2))
#for i in lev:
#    print(i)



def swap(translation):
    cc=[]
    for i in translation: 
        c=0
        for j in nums:
            c=c+1
            if j==i:
                cc.append(c)
                if len(cc)==2:
                    return cc
#print(gen[1],'gen1')
#print(swap(gen[0]))

conn=connectedDiagrams(2)
#print(conn)
#print(len(conn))


for i in conn:
    c=-1
    input()
    print(i)

    for j in lev:
        print(j)
        ii=deepcopy(i)
        for k in i:
            c=c+1
            c2=-1
            for q in k:
                c2=c2+1
                if q==j[0]:
                    
                    print(c,'TIME 1')
                    print(c2,'TIME 2')
                    
                    ii[c][c2]=j[1]
                if q==j[1]:
                    print(c,'TIME 11')
                    print(c2,'TIME 22')
                    ii[c][c2]=j[0]
                    
    print(ii)
