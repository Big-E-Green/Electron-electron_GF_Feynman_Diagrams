from generator import *
print(len(generall(2)))
gun2=generall(2)
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
            firstsweep.append(i)
print(remmed)                           #completely removed diags
print(len(remmed))

cheeko=genny(2)

ARRAY=PLX.copy()
full=[]
disconnnn=[]
for i in ARRAY:
    Truth=0
    input()
    print(i)
    ray=i
    ARR=ray.copy()
    coun=0
    finall=0
    kile=[]
    tmp3=''
    while finall!=1:
        coun=coun+1
        if coun>30:
                print('                                FAILED')
                finall=finall+1
        for k in ARR:
            print(k)           
            
            if k[0]=='00':
                tmp=k[1]
                ARR.remove(k)
                for p in cheeko:
                    coll=-2
                    for z in p:
                        coll=coll+1
                        if tmp==z:
                            tmp2=p[coll] 
            if k[0]==tmp:
                tmp=k[1]
                ARR.remove(k)
                if k[1]=='00':
                    Truth=Truth+1


            print(tmp2)       
            if k[0]==tmp2:
                if k[1]==tmp2:
                    ARR.remove(k)
                    Truth=Truth+1
                    print('                           TRUE LOOP')
            if k[0]==tmp2:
                kile=tmp2
                tmp3=k[1]
                for i in cheeko:
                    coll=-1
                    for j in i:
                        coll=coll+1
                        if tmp2==j:
                            tmp2=p[coll]

            if tmp3==kile:
                
                print('TRUE')
            
            

c=-1
DISCONNN=[]
disconnn2=[]
remm=disconnnn.copy()
for i in disconnnn:
    if len(i)<5:
        DISCONNN.append(i)
for i in DISCONNN:
    remm.remove(i)
    disconnn2.append(i)
FULL=full.copy()
for i in remm:
    FULL.remove(i)
    disconnn2.append(i)

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
        discoonnn3.append(i)

print(FULL)
print(len(FULL))                    #ONLY CONNECTED DIAGRAMS LEFT
