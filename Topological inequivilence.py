import random
import math
from copy import deepcopy

#
#                                            Generating for n
#

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
for i in bGood:
    c=0
    for j in i:
        bgood.append(str(One[c]))
        bgood.append(str(j))
        c=c+1
    save=bgood.copy()
chunki=[]
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
print(gun2)                             #gun2 == all possible diagrams
print(len(gun2))

holystatment=[]
for i in gun2:                          #True/False/Skip
    holystatment.append(['1'])
    
#
#                                       Removing diagrams
#

discon=[]
for i in gun2:
    for j in i:
        if j==['00', '00']:
            discon.append(i)
remmed=[]
firstsweep=[]
for i in gun2:
    for j in discon:
        if i==j:
            remmed.append(i)
            firstsweep.append(i)
print(remmed)                           #completely disconnected diagrams
print(len(remmed))

c=-1
for i in gun2:
    c=c+1
    for j in firstsweep:
        if i==j:
            for k in holystatment:
                holystatment[c]=['3']

print(holystatment)
