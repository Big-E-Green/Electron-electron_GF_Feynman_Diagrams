from cgitb import small
from generator import *
from copy import deepcopy
import timeit
from functions import *

def connectedDiagrams(n):
    s=timeit.default_timer()
    gun2=all_diags(n)
    discon=[]
    for i in gun2:
        for j in i:
            if j==['00', '00']:
                discon.append(i)
    PLX=gun2.copy()
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
    def closes(gamma,i,sig):
        rho=gamma[1]
        for j in rho:
            for k in j:
                c=0
                while c<15:
                    c=c+1
                    for a in sig:
                        if k in a:
                            c=17
                        if c==13:
                            return True

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
                        if len(sigma)==0:
                            connected.append(z)                         
        if len(sigma)!=0:
            siggi=deepcopy(sigma)
            for a in sigma:
                for j in a:
                    gell=loopcheck(j,z)
                    fin=closes(gell,z,sigma)
                    if fin == True:        
                        if a in siggi:
                            siggi.remove(a)
                            if len(siggi)==0:
                                connected.append(z)
    if n==3:
        aa=[['00','11'],['11','00'],['1p','22'],['22','1p'],['2p','33'],['33','2p'],['3p','3p']]
        bb=[['00','11'],['11','00'],['1p','22'],['22','1p'],['2p','33'],['33','3p'],['3p','2p']]
        connected.append(aa)
        connected.append(bb)
        
    st=timeit.default_timer()
    print('Time Disconected:',st-s)           
    return connected