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

def reachzero(start,i):
    c=0
    hold=[]
    while len(i)!=0:
        c=c+1
        for k in i:
            if k[0]==start:
                print(k)
                start=k[1]
                hold.append(k)
                i.remove(k)
                if k[1]=='00':
                    i=[]
                    return True, hold
            if c>10:
                i=[]
                return False, hold
def loopcheck(start,i,end):
    c=0
    hold=[]
    while len(i)!=0:
        c=c+1
        for k in i:
            if k[1] and k[0]!='00':
                if k[1]==start:
                    print(k)
                    start=k[0]
                    hold.append(k)
                    i.remove(k)
                    if k[1]==end:
                        i=[]
                        return True, hold
                    if start[1]==end[0]:
                        hold.append(k)
                        i=[]
                        return True, hold
                if c>10:
                    i=[]
                    return False, hold
            
    
#for i in ARRAY:
#    input()
#    print(i)
#    print(loopcheck('1p',i,'1p'))



for i in ARRAY:
    input()
    print(i)
    ray=i
    ARR=ray.copy()
    c=0
    true=0
    for x in cheeko:
        for j in x:
            print(j,'jay')
            print(reachzero(j,i),'zero')
            #print(loopcheck(j,i,j),'loop')


                
            
            

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
