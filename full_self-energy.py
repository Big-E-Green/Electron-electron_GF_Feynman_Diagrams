from self_energy import *

Final=[]
for i in Diagrams:
    fl=0
    c=-1
    for t in Fock:
        if t not in i:
            c=c+1
            if c==len(i):
                fl=fl+1
    c=-1
    for s in Hartree:
        if s not in i:
            c=c+1
            if c==len(i):
                fl=fl+1
    if fl==2:
        Final.append(i)
    for j in Hartree:
        if j in i:
            cc=counterpart(j[0],fock)
            i.remove(j)
            new=[]
            a=[]
            b=[]
            for k in i:
                if cc==k[0]:
                    a=k[1]
                if cc==k[1]:
                    b=k[0]
                if a!=[] and b!=[]:
                    c=[]
                    c.append(a)
                    c.append(b)
                    new.append(c)
            if new not in Final:
                Final.append(new)
    for j in Fock:
        if j in i:
            one=j[0]
            two=j[1]
            new=[]
            a=[]
            b=[]
            for q in i:
                if two==q[0]:
                    a=q[1]
                if one==q[1]:
                    b=q[0]
                if a!=[] and b!=[]:
                    c=[]
                    c.append(a)
                    c.append(b)
                    if c not in new:
                        new.append(c)
            if new not in Final:
                Final.append(new)
for i in Final:
    print(i)
