import random
import math

def generall(n):
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
    return gun2

def genny(n):
    G=(2*n)+1
    One=[]
    Two=[]
    c=0
    while n>=c:
        g=str(c)+str(c)
        One.append(str(g))
        f=str(c)+'p'
        One.append(str(f))
        c=c+1
    One.remove('0p')
    One.remove('00')
    chunkii=[]
    for x in range(0, len(One), 2):
        chunkii.append(One[x:x+2])
    return chunkii

