import random
import math
from copy import deepcopy

#
#
#       Generating for n
#
#

alldisconnected=[]
n=2
G=(2*n)+1
One=[]
Two=[]
c=0
while n>=c:
    g=str(c)+str(c)
    One.append(str(g))
    f=str(c)+'p'
    One.append(str(f))
    Two.append(str(g))
    Two.append(str(f))
    c=c+1
One.remove('0p')
Two.remove('0p')
array=[]

FacG=math.factorial(G)
LenG=2*((2*n)+1)
b = ""
fin = []
bigB=[]
bGood = []    
while len(fin) < FacG:
    aa=One.copy()
    while len(b) < LenG:
        x = random.choice(aa)
        b += x
        bigB.append(x)
        aa.remove(x)
    if b not in fin:
        fin.append(b)
        save = bigB.copy()
        bGood.append(save)
    b = ""
    bigB.clear()
fin.sort()
bGood.sort()

bgood=[]
chunki=[]
for i in bGood:
    c=0
    for j in i:
        bgood.append(str(One[c]))
        bgood.append(str(j))
        c=c+1
    save=bgood.copy()
for x in range(0, len(save), 2):
    chunki.append(save[x:x+2])
gun = []
gun2 = []
for x in chunki:
    gun.append(x)
    if len(gun) == G:
        gunTemper = gun.copy()
        gun2.append(gunTemper)
        gun.clear()
#print(gun2)            #  gun2 is all possible diags
#print(len(gun2))

holystatment=[]
for i in gun2:
    holystatment.append(['2'])
  
#
#
#       Removing disconnected diags
#
#


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
    for j in discon:                    #completely removed diags, a --> b
        if i==j:
            PLX.remove(i)
            remmed.append(i)
            alldisconnected.append(i)
            firstsweep.append(i)
#print(remmed)          #  completely removed diags

c=-1
for i in gun2:
    c=c+1
    for j in firstsweep:
        if i==j:
            for k in holystatment:
                holystatment[c]=['1']


ARRAY=PLX.copy()
full=[]
disconnnn=[]
for i in ARRAY:
    ray=i
    ARR=ray.copy()
    forcount=0
    while len(ARR)>0:
        forcount=forcount+1
        for k in ARR:
            if k[0]=='00':
                tmp=k[1]
                ARR.remove(k)
            if k[0]==k[1]:
                ARR.remove(k)
            if k[0]==tmp:
                tmp=k[1]
                ARR.remove(k)
                if k[1]=='00':
                    full.append(i)
            if len(ARR)==2:
                dee=ARR[1]
                RRA=[dee[1],dee[0]]
                if ARR[0] == RRA:
                    disconnnn.append(i)
                    ARR=[]
            if forcount>10:
                for i in ARR:
                    for j in i:
                        tmp=ARR[0][0]
                        tmp2=ARR[0][1]
                        if j[0]==tmp2:
                            tmp2=j[1]
                            ARR.remove(j)
                        if j[1]==tmp:
                            ARR.remove(j)
                            ARR=[]

c=-1
DISCONNN=[]
disconnn2=[]
remm=disconnnn.copy()
for i in disconnnn:
    if len(i)<5:
        DISCONNN.append(i)
for i in DISCONNN:
    remm.remove(i)
    alldisconnected.append(i)
    disconnn2.append(i)
FULL=full.copy()
for i in remm:
    FULL.remove(i)
    alldisconnected.append(i)
    disconnn2.append(i)

c=-1
for i in gun2:
    c=c+1
    for j in disconnn2:
        if i==j:
            for k in holystatment:
                holystatment[c]=['1']

DISSC=[]   
for i in FULL:
    if ['1p', '1p'] in i:
        if ['11', '11'] in i:
            DISSC.append(i)
    if ['2p', '2p'] in i:
        if ['22', '22'] in i:
            DISSC.append(i)   
    if ['3p', '3p'] in i:
        if ['33', '33'] in i:
            DISSC.append(i)

discoonnn3=[]
for i in DISSC:
    if i in FULL:
        FULL.remove(i)
        alldisconnected.append(i)
        discoonnn3.append(i)

c=-1
for i in gun2:
    c=c+1
    for j in discoonnn3:
        if i==j:
            for k in holystatment:
                holystatment[c]=['1']
#print(holystatment)


print(FULL)
print(len(FULL))            # ONLY CONNECTED DIAGRAMS LEFT

#print(alldisconnected)      # ONLY ALL DISCONNECTED DIAGRAMS
#print(len(alldisconnected))

#
#
#       Generating all possible transformations
#
#


full=deepcopy(FULL)
trans=FULL.copy()
c2=-1
for i in FULL:
    c2=c2+1
    aa=i
    c=-1
    for j in i:
        c=c+1
        c1=-1
        for k in j:
            c1=c1+1
            if k == '22':
                trans[c2][c][c1]='2p'
            if k == '2p':
                trans[c2][c][c1]='22'


COUN=[]
c=-1
while 4>c:
    c=c+1
    COUN.append(str(c))
Fac=math.factorial(len(FULL[0]))
b = []
fin = []
bigB=[]
bGood = []    
while len(fin) < 20:
    aa=COUN.copy()
    while len(b) < 2:
        x = random.choice(aa)
        aa.remove(x)
        y = random.choice(aa)

        b.append(x)
        b.append(y)
    if b not in fin:
        fin.append(b)
        save = b.copy()
        bGood.append(save)
    b = []
    bigB.clear()
fin.sort()
bGood.sort()
#print(bGood,'big')








                
Trans=trans.copy()   
c=-1
SAVE=[]
TT=deepcopy(trans)
TTT=deepcopy(trans)
for i in TTT:
    i[3],i[4]=i[4],i[3]
    SAVE.append(i)

TMPPP=[]
TMPPPP=[]

PLOP=[]
for j in bGood:
    for i in TT:
        if j==['3','4']:
            k=int(j[0])
            l=int(j[1])
            i[k],i[l]=i[l],i[k]
            TMPPP.append(i)
tmp=[]
c=-1
cont1=[]
cont2=[]
for i in full:
    c=c+1
    c1=-1
    for j in TMPPP:
        c1=c1+1
        if i==j:
            cont1.append(c)
            cont2.append(c1)
            tmp.append(i)
c=-1
ORD=[]
for i in cont1:
    c=c+1
    kk=0
    while kk!=1:
        order=[]
        order.append(i)
        order.append(cont2[c])
        ORD.append(order)
        kk=1
for i in ORD:
    if i[0]==i[1]:
        ORD.remove(i)
keep=[]
for i in ORD:
    if i[0] not in keep:
        keep.append(i[0])
    if i[1] not in keep:
        keep.append(i[1])
keep=keep[::2]

pUll=deepcopy(full)
for i in keep:
    kk=full[i]
    pUll.remove(kk)

#print(pUll)
#print(len(pUll))

#
#
#

POOL=deepcopy(pUll)
trans=pUll.copy()
c2=-1
for i in POOL:
    c2=c2+1
    aa=i
    c=-1
    for j in i:
        c=c+1
        c1=-1
        for k in j:
            c1=c1+1
            if k == '11':
                trans[c2][c][c1]='1p'
            if k == '1p':
                trans[c2][c][c1]='11'
###############print(trans)
Trans=trans.copy()
c=-1
for i in trans:
    c=c+1
    Trans[c][1],Trans[c][2]=Trans[c][2],Trans[c][1]
tmp=[]
c=-1
cont1=[]
cont2=[]
for i in POOL:
    c=c+1
    c1=-1
    for j in trans:
        c1=c1+1
        if i==j:
            cont1.append(c)
            cont2.append(c1)
            tmp.append(i)
c=-1
ORD=[]
for i in cont1:
    c=c+1
    kk=0
    while kk!=1:
        order=[]
        order.append(i)
        order.append(cont2[c])
        ORD.append(order)
        kk=1
for i in ORD:
    if i[0]==i[1]:
        ORD.remove(i)
keep=[]
for i in ORD:
    if i[0] not in keep:
        keep.append(i[0])
    if i[1] not in keep:
        keep.append(i[1])
keep=keep[::2]
pooo=deepcopy(POOL)
for i in keep:
    kk=POOL[i]
    pooo.remove(kk)

#print(pooo)
#print(len(pooo))

#
#
#

POOK=deepcopy(pooo)
trans=pooo.copy()
c2=-1
for i in POOK:
    c2=c2+1
    aa=i
    c=-1
    for j in i:
        c=c+1
        c1=-1
        for k in j:
            c1=c1+1
            if k == '1p':
                trans[c2][c][c1]='2p'
            if k == '2p':
                trans[c2][c][c1]='1p'
            
###############print(trans)
Trans=trans.copy()
c=-1
for i in trans:
    c=c+1
    Trans[c][2],Trans[c][4]=Trans[c][4],Trans[c][2]
tmp=[]
c=-1
cont1=[]
cont2=[]
for i in POOK:
    c=c+1
    c1=-1
    for j in trans:
        c1=c1+1
        if i==j:
            cont1.append(c)
            cont2.append(c1)
            tmp.append(i)
            ###############print(i)
c=-1
ORD=[]
for i in cont1:
    c=c+1
    kk=0
    while kk!=1:
        order=[]
        order.append(i)
        order.append(cont2[c])
        ORD.append(order)
        kk=1
for i in ORD:
    if i[0]==i[1]:
        ORD.remove(i)
keep=[]
for i in ORD:
    if i[0] not in keep:
        keep.append(i[0])
    if i[1] not in keep:
        keep.append(i[1])
keep=keep[::2]
poook=deepcopy(POOK)
for i in keep:
    kk=POOK[i]
    poook.remove(kk)

#print(poook)
#print(len(poook))

#
#
#

POOKk=deepcopy(poook)
trans=poook.copy()
c2=-1
for i in POOKk:
    c2=c2+1
    aa=i
    c=-1
    for j in i:
        c=c+1
        c1=-1
        for k in j:
            c1=c1+1
            if k == '22':
                trans[c2][c][c1]='1p'
            if k == '2p':
                trans[c2][c][c1]='11'
            if k == '11':
                trans[c2][c][c1]='2p'
            if k == '1p':
                trans[c2][c][c1]='22'

            
###############print(trans)
Trans=trans.copy()
c=-1
for i in trans:
    c=c+1
    Trans[c][2],Trans[c][3]=Trans[c][3],Trans[c][2]
    Trans[c][1],Trans[c][4]=Trans[c][4],Trans[c][1]
tmp=[]
c=-1
cont1=[]
cont2=[]
for i in POOKk:
    c=c+1
    c1=-1
    for j in trans:
        c1=c1+1
        if i==j:
            cont1.append(c)
            cont2.append(c1)
            tmp.append(i)
c=-1
ORD=[]
for i in cont1:
    c=c+1
    kk=0
    while kk!=1:
        order=[]
        order.append(i)
        order.append(cont2[c])
        ORD.append(order)
        kk=1
for i in ORD:
    if i[0]==i[1]:
        ORD.remove(i)
keep=[]
for i in ORD:
    if i[0] not in keep:
        keep.append(i[0])
    if i[1] not in keep:
        keep.append(i[1])
keep=keep[::2]
poookkk=deepcopy(POOKk)
for i in keep:
    kk=POOKk[i]
    poookkk.remove(kk)

#print(poookkk)
#print(len(poookkk))

#
#
#

DRISK=deepcopy(poookkk)
trans=poookkk.copy()
c2=-1
for i in DRISK:
    c2=c2+1
    aa=i
    c=-1
    for j in i:
        c=c+1
        c1=-1
        for k in j:
            c1=c1+1
            if k == '2p':
                trans[c2][c][c1]='1p'
            if k == '1p':
                trans[c2][c][c1]='2p'
###############print(trans)
Trans=trans.copy()
c=-1
for i in trans:
    c=c+1
    Trans[c][2],Trans[c][4]=Trans[c][4],Trans[c][2]
    Trans[c][3],Trans[c][4]=Trans[c][4],Trans[c][3]
c2=-1
for i in Trans:
    c2=c2+1
    aa=i
    c=-1
    for j in i:
        c=c+1
        c1=-1
        for k in j:
            c1=c1+1
            if k == '2p':
                trans[c2][c][c1]='22'
            if k == '22':
                trans[c2][c][c1]='2p'
tmp=[]
c=-1
cont1=[]
cont2=[]
for i in DRISK:
    c=c+1
    c1=-1
    for j in trans:
        c1=c1+1
        if i==j:
            cont1.append(c)
            cont2.append(c1)
            tmp.append(i)
c=-1
ORD=[]
for i in cont1:
    c=c+1
    kk=0
    while kk!=1:
        order=[]
        order.append(i)
        order.append(cont2[c])
        ORD.append(order)
        kk=1
for i in ORD:
    if i[0]==i[1]:
        ORD.remove(i)
keep=[]
for i in ORD:
    if i[0] not in keep:
        keep.append(i[0])
    if i[1] not in keep:
        keep.append(i[1])
keep=keep[::2]
eeee=deepcopy(DRISK)
for i in keep:
    kk=DRISK[i]
    eeee.remove(kk)

#print(eeee)
#print(len(eeee))

#
#
#

DRISKss=deepcopy(eeee)
trans=eeee.copy()
c2=-1
for i in DRISKss:
    c2=c2+1
    aa=i
    c=-1
    for j in i:
        c=c+1
        c1=-1
        for k in j:
            c1=c1+1
            if k == '11':
                trans[c2][c][c1]='22'
            if k == '1p':
                trans[c2][c][c1]='2p'
            if k == '2p':
                trans[c2][c][c1]='1p'
            if k == '22':
                trans[c2][c][c1]='11'
###############print(trans)
Trans=trans.copy()
c=-1
for i in trans:
    c=c+1
    Trans[c][1],Trans[c][3]=Trans[c][3],Trans[c][1]
    Trans[c][2],Trans[c][4]=Trans[c][4],Trans[c][2]
    Trans[c][3],Trans[c][4]=Trans[c][4],Trans[c][3]
c2=-1
for i in Trans:
    c2=c2+1
    aa=i
    c=-1
    for j in i:
        c=c+1
        c1=-1
        for k in j:
            c1=c1+1
            if k == '2p':
                trans[c2][c][c1]='22'
            if k == '22':
                trans[c2][c][c1]='2p'
tmp=[]
c=-1
cont1=[]
cont2=[]
for i in DRISKss:
    c=c+1
    c1=-1
    for j in trans:
        c1=c1+1
        if i==j:
            cont1.append(c)
            cont2.append(c1)
            tmp.append(i)
c=-1
ORD=[]
for i in cont1:
    c=c+1
    kk=0
    while kk!=1:
        order=[]
        order.append(i)
        order.append(cont2[c])
        ORD.append(order)
        kk=1
for i in ORD:
    if i[0]==i[1]:
        ORD.remove(i)
keep=[]
for i in ORD:
    if i[0] not in keep:
        keep.append(i[0])
    if i[1] not in keep:
        keep.append(i[1])
keep=keep[::2]
rrrr=deepcopy(DRISKss)
for i in keep:
    kk=DRISKss[i]
    rrrr.remove(kk)

#print(rrrr)
#print(len(rrrr))

#
#
#

DRISKssSS=deepcopy(rrrr)
trans=rrrr.copy()
c2=-1
for i in DRISKssSS:
    c2=c2+1
    aa=i
    c=-1
    for j in i:
        c=c+1
        c1=-1
        for k in j:
            c1=c1+1
            if k == '11':
                trans[c2][c][c1]='22'
            if k == '22':
                trans[c2][c][c1]='11'
###############print(trans)
Trans=trans.copy()
c=-1
for i in trans:
    c=c+1
    Trans[c][1],Trans[c][3]=Trans[c][3],Trans[c][1]
c2=-1
tmp=[]
c=-1
cont1=[]
cont2=[]
for i in DRISKssSS:
    c=c+1
    c1=-1
    for j in trans:
        c1=c1+1
        if i==j:
            cont1.append(c)
            cont2.append(c1)
            tmp.append(i)
c=-1
ORD=[]
for i in cont1:
    c=c+1
    kk=0
    while kk!=1:
        order=[]
        order.append(i)
        order.append(cont2[c])
        ORD.append(order)
        kk=1
for i in ORD:
    if i[0]==i[1]:
        ORD.remove(i)
keep=[]
skip=[]
for i in ORD:
    if i[0] not in keep or skip:
        keep.append(i[0])
    if i[1] not in keep or skip:
        keep.append(i[1])
keep=keep[::2]
qqqq=deepcopy(DRISKssSS)
for i in keep:
    kk=DRISKssSS[i]
    qqqq.remove(kk)

#print(qqqq)
#print(len(qqqq))

#
#
#

DRISKssSSss=deepcopy(qqqq)
trans=qqqq.copy()
c2=-1
for i in DRISKssSSss:
    c2=c2+1
    aa=i
    c=-1
    for j in i:
        c=c+1
        c1=-1
        for k in j:
            c1=c1+1
            if k == '11':
                trans[c2][c][c1]='22'
            if k == '1p':
                trans[c2][c][c1]='2p'
            if k == '2p':
                trans[c2][c][c1]='1p'
            if k == '22':
                trans[c2][c][c1]='11'
###############print(trans)
Trans=trans.copy()
c=-1
for i in trans:
    c=c+1
    Trans[c][1],Trans[c][3]=Trans[c][3],Trans[c][1]
    Trans[c][2],Trans[c][4]=Trans[c][4],Trans[c][2]
c2=-1
tmp=[]
c=-1
cont1=[]
cont2=[]
for i in DRISKssSSss:
    c=c+1
    c1=-1
    for j in trans:
        c1=c1+1
        if i==j:
            cont1.append(c)
            cont2.append(c1)
            tmp.append(i)
c=-1
ORD=[]
for i in cont1:
    c=c+1
    kk=0
    while kk!=1:
        order=[]
        order.append(i)
        order.append(cont2[c])
        ORD.append(order)
        kk=1
for i in ORD:
    if i[0]==i[1]:
        ORD.remove(i)
keep=[]
skip=[]
for i in ORD:
    if i[0] not in keep or skip:
        keep.append(i[0])
    if i[1] not in keep or skip:
        keep.append(i[1])
keep=keep[::2]
zzzz=deepcopy(DRISKssSSss)
for i in keep:
    kk=DRISKssSSss[i]
    zzzz.remove(kk)

print(zzzz)
print(len(zzzz))
