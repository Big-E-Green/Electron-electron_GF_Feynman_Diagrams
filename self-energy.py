from topologicalInequiv import *
from copy import deepcopy
from generator import *

def counterpart(n,inters):
    for i in inters:
        if i[0]==n:
            return i[1]
        if i[1]==n:
            return i[0]

def rev_slice(mylist):
    a = mylist[::-1]
    return a

def loops_path(init,arr):
    i1=init
    i2=rev_slice(init)
    sav_arr=[]
    c=0
    tmp=[]
    while len(i1)>0:
        c=c+1
        for i in arr:
            a=i1[0]
            b=i1[1]
            if i[0]==a:
                tmp=i[1]
                sav_arr.append(i)
                if i[0]==i[1]:
                    return False, sav_arr
                if i[1]=='00':
                    c=3
            if tmp==b:
                return False, sav_arr
            if tmp==a:
                return False, sav_arr
            if i[0]==tmp:
                tmp=i[1]
                sav_arr.append(i)
                if i[1]==b:
                    return True, sav_arr
                if i[1]=='00':
                    c=3
        if c==3:
            i1=i2
            sav_arr=[]
            tmp=[]


diags=distinctDiagrams(2)
diags2=[]
for i in diags:
    ii=deepcopy(i)
    for j in i:
        if '00' in j:
            ii.remove(j)
    diags2.append(ii)
Diags2=deepcopy(diags2)
fock=genny(2)
Fock=[]
for i in fock:
    Fock.append(i)
    Fock.append(rev_slice(i))
hartree=gen(2)
hartree.remove('00')
Hartree=[]
for i in hartree:
    tmp=[]
    tmp.append(i)
    tmp.append(i)
    Hartree.append(tmp)
c=-1

for i in Diags2:
    c=c+1
    tmparr=[]
    for k in genny(2):
        zultan=loops_path(k,diags[c])
        tmparr.append(zultan[1])
    tmp2arr=[]
    tmp3arr=[]
    for q in tmparr:
        if len(q)==1:
            tmp3arr.append(q)
        if len(q)>1:
            tmp2arr.append(q)
    one=[]
    for o in tmp2arr:
        for hp in o:
            for d in hp:
                one.append(d)
    remmed=[]
    for j in fock:   
        if j in i:
            i.remove(j)
            for u in j:
                remmed.append(u)
            for p in tmp2arr:
                if j in p:
                    i.append(j)
                    for u in j:
                        remmed.remove(u)
    for g in Hartree:
        if g in i:
            cont=counterpart(g[0],fock)
            if cont not in one:
                i.remove(g)
                remmed.append(cont)
    for l in i:
        ll=l
        for f in remmed:
            if f in l:
                ll.remove(f)
                if len(ll)==0:
                    i.remove(l)
Diagrams=deepcopy(Diags2)
for i in Diags2:
    if i==[]:
        Diagrams.remove(i)

for i in Diagrams:
    print(i)
