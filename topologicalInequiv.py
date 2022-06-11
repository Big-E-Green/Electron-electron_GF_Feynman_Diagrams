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
    ss=timeit.default_timer()
    gen=genny(n)
    nums=[]
    for i in gen:
        for j in i:                                              
            nums.append(j)
    lev=list(itertools.combinations(nums,2))
    cool=[]

    ##########################################################################
    # k-k'

    ktok=[]
    gell=[]
    for i in gen:
        for k in lev:
            if i[0] in k:                                           
                if i[1] in k:
                    gell.append(k)
    combs=list(itertools.combinations(gell,1))
    ktok.append(combs)
    c=0
    for i in gell:
        c=c+1
        if c>1:
            combs2=list(itertools.combinations(gell,c))
            ktok.append(combs2)                             
    kktok=deepcopy(ktok)
    cool=ktok

    ##########################################################################
    # interaction pairs 

    combos=deepcopy(lev)
    for i in lev:
        for j in gen:
            if i[0]==j[0]:
                if i[1]==j[1]:
                    combos.remove(i)
    pairs=[]
    for i in gen:
        for j in i:
            tmp=[]
            for k in combos:
                if j==k[0]:
                    tmp.append(k)
            pairs.append(tmp)
    pairs2=deepcopy(pairs)
    c=-1
    pairCombs=[]    
    for i in pairs:
        print(i)                                          
    for i in pairs:
        c=c+1
        for j in i:
            tempT=[]
            c2=-1
            for k in pairs2:
                c2=c2+1
                if c2==c:
                    c=c
                else:
                    for p in k:
                        temp=[]
                        temp.append(j)
                        temp.append(p)
                        tempT.append(temp)
            pairCombs.append(tempT)
    print(gen)
    remm=[]
    for i in pairCombs:
        for j in i:
            tetts=[]
            for k in j:
                tetts.append(k[0])
                if len(tetts)==2:
                    for h in gen:
                        if tetts[0] in h:
                            if tetts[1] in h:
                                remm.append(j)
    delec=[]
    for i in remm:
        tello=[]
        tello.append(i)
        delec.append(tello)
    pairCombs=delec
    for i in pairCombs:
        for j in i:
            tmp=[]
            for k in j:
                tmp.append(k[1])
            if tmp[0]==tmp[1]:
                for s in pairCombs:
                    if j in s:
                        s.remove(j)
    tmp3=[]
    for i in pairCombs:
        for j in i:
            if j not in tmp3:
                tmp3.append(j)
    for i in pairCombs:
        print(i)
        for j in i:
            print(j)
    pairCombs=tmp3
    cool.append(pairCombs)
    
    ######################################################################
    # for each k-k' pair swaps

    combo=[]
    for z in pairCombs:
        tmp2=[]
        smashh=[]
        for l in z:
            tmp2.append(l)
            for i in kktok:      
                for j in i:
                    tmp=[]
                    for q in j:
                        tmp.append(q)
                    smash=[]
                    smash.append(tmp2)
                    smash.append(tmp)
                    smashh.append(smash)
        for w in smashh:
            ttmp=[]
            for r in w:
                for u in r:
                    ttmp.append(u)
            combo.append(ttmp)
    cool.append(combo)

    ######################################################################
    # transforming each i by k-k', interact pairs, and k-k' + interact pairs

    conn=connectedDiagrams(n)
    connn=deepcopy(conn)
    for i in connn:
        sav=[]
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
                                    sav.append(i)
        #print(len(sav))
    st=timeit.default_timer()
    print('Time Inequiv:',st-ss)
    return connn

#print(distinctDiagrams(2))
print(len(distinctDiagrams(2)))