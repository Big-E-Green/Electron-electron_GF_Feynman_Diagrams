from RemovingDisconnected import *
from generator import *
import itertools
from copy import deepcopy

gen=genny(2)
nums=[]
for i in gen:
    for j in i:
        nums.append(j)
lev=list(itertools.combinations(nums,2))
c=0
cool=[]
for i in lev:
    c=c+1
    if c>1:
        dunce=list(itertools.combinations(lev,c))
        cool.append(dunce)

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
                
def reparam(trans,inp):
    c=-1
    ii=deepcopy(inp)
    for k in inp:
        c=c+1
        c2=-1
        for q in k:
            c2=c2+1
            if q==trans[0]:        
                ii[c][c2]=trans[1]
            if q==trans[1]:
                ii[c][c2]=trans[0]
    sw=swap(trans)
    ii[sw[0]],ii[sw[1]]=ii[sw[1]],ii[sw[0]]
    return ii

conn=connectedDiagrams(2)
connn=deepcopy(conn)
for i in connn:
    tmp=i
    for j in cool:
        for k in j:
            c=0
            while c!=len(k):
                for q in k:
                    gens=reparam(q,tmp)
                    tmp=gens                                    #removal of all higher order transformations
                    c=c+1
                    if c==len(k):
                        if gens in connn:
                            if gens!=i:
                                connn.remove(gens)
print(connn)
print(len(connn))

con2=deepcopy(connn)
for i in con2:
    for j in lev:
        gens=reparam(j,i)
        if gens in con2:                                        #removal of len 1 transformations
            if gens!=i:
                con2.remove(gens)
print(con2)
print(len(con2))


