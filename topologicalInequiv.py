from disconnected import *
from generator import *
from functions import *
import itertools
from copy import deepcopy
import timeit


def swap(translation,numm):
    cc=[]
    for i in translation: 
        c=0
        for j in numm:
            c=c+1
            if j==i:
                cc.append(c)
                if len(cc)==2:
                    return cc
                    
def reparam(trans,inp,numm):
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
    sw=swap(trans,numm)
    ii[sw[0]],ii[sw[1]]=ii[sw[1]],ii[sw[0]]
    return ii

def distinctDiagrams(n):
    s=timeit.default_timer()
    gen=genny(n)
    nums=[]
    for i in gen:
        for j in i:
            nums.append(j)
    lev=list(itertools.combinations(nums,2))
    c=0
    cool=[]
    for i in lev:
        c=c+1
        if c<2:
            dunce=list(itertools.combinations(lev,c))
            cool.append(dunce)
    gell=[]
    for i in gen:
        for k in lev:
            if i[0] in k:
                if i[1] in k:
                    gell.append(k)
                    print(k)
    amm=list(itertools.combinations(gell,2))
    colin=list(itertools.combinations(gell,3))
    print(colin)
    print(amm)
    coot=[]
    genn=deepcopy(gen)
    c=0
    for i in gen:
        colo=[]
        colo2=[]
        c=c+1
        if c==1:
            for k in lev:
                if i[0] in k:
                    colo.append(k)
                if i[1] in k:
                    colo2.append(k)
            for z in colo:
                for a in genn:
                    if z[0]==a[0]:
                        if z[1]==a[1]:
                            if z in colo:
                                colo.remove(z)
            for z in colo2:
                for a in genn:
                    if z[0]==a[0]:
                        if z[1]==a[1]:
                            if z in colo2:
                                colo2.remove(z)
            coot.append(colo)
            coot.append(colo2)
    disso=[]
    for i in coot:
        for j in i:
            if j not in disso:
                disso.append(j)
    dett=list(itertools.combinations(disso,2))
    for i in dett:
        if i[1][0]==i[0][0]:
            dett.remove(i)
    smash=[]
    for k in lev:
        for i in dett:
            too=[]
            for j in i:
                too.append(j)
                if len(too)==len(i):
                    too.append(k)
                    smash.append(too)
    cool.append(amm)
    #cool.append(colin)
    cool.append(dett)
    cool.append(smash)
    conn=connectedDiagrams(n)
    connn=deepcopy(conn)
    #ce=0
    for i in connn:
        #cole=[]
        for j in cool:
            for k in j:
                tmp=i
                orig=i
                c=0
                while c!=len(k):
                    for q in k:
                        gens=reparam(q,tmp,nums)
                        tmp=gens                                  
                        c=c+1
                        if c==len(k):
                            if gens in connn:
                                if gens!=orig:
                                    connn.remove(gens)
                                    #print(k,ce)
                                    #ce=ce+1
                                    #cole.append(gens)
        #print(len(cole))
    st=timeit.default_timer()
    print('Time Inequiv:',st-s)
    return connn
    
#print(distinctDiagrams(2))
print(len(distinctDiagrams(3)))
