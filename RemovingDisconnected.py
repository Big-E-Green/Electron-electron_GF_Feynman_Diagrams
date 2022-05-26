from generator import *

def connectedDiagrams(n):
    gun2=generall(n)
    discon=[]
    qweqwe=[]
    for i in gun2:
        for j in i:
            if j==['00', '00']:
                discon.append(i)
    PLX=gun2.copy()
    remmed=[]
    firstsweep=[]
    for i in gun2:
        for j in discon:                    
            if i==j:
                PLX.remove(i)
                remmed.append(i)
                firstsweep.append(i)
    cheeko=genny(n)
    ARRAY=PLX.copy()
    def reachzero(start,array):
        c=0
        hold=[]
        RAY=array.copy()
        while len(RAY)!=0:
            c=c+1
            for k in RAY:
                if k[0]==start:
                    start=k[1]
                    hold.append(k)
                    RAY.remove(k)
                    if k[1]=='00':
                        return True, hold
                if c>10:
                    return False, hold
    def loopcheck(var,i):
        c=0
        hold=[]
        tmp=var
        while len(i)!=0:
            c=c+1      
            for k in i:
                if k[0]==tmp:
                    if k[1]!='00':
                        tmp=k[1]
                        hold.append(k)
                        if k[0]==k[1]:
                            return True, hold
                        if k[1]==var:
                            return True, hold
                if c>10:
                    i=[]
                    return False, hold
    connected=[]
    for z in ARRAY:
        sigma=cheeko.copy()
        i=z.copy()
        for x in cheeko:
            arr=[]
            for j in x:          
                zero=reachzero(j,i)
                arr.append(zero[0])
                if len(arr)==2:
                    if True in arr:
                        sigma.remove(x)
        for x in cheeko:
            arr2=[]
            arr3=[]
            for j in x:
                looper=loopcheck(j,i)
                arr2.append(looper[0])
                arr3.append(looper[1])
                if len(arr2)==2:
                    if arr2[0] and arr2[1]==True:
                        for i in arr3:
                            for j in i:
                                for k in j:
                                    for q in sigma:
                                        if k not in q:
                                            sigma.remove(x)
                                
        if len(sigma)==0:
            connected.append(z)
    return connected
    









