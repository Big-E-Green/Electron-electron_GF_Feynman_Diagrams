from re import T
from feynman import Diagram
import matplotlib.pyplot as plt
from topologicalInequiv import *
from generator import *
from functions import *
from disconnected import *
from copy import deepcopy

print(distinctDiagrams(1))
print(genny(1))

def main():
    diags=distinctDiagrams(2)
    interacts=genny(2)

    fig, axes = plt.subplots(figsize=(10,5), nrows=1, ncols=len(diags),
                            subplot_kw=dict(aspect='equal', frameon=True),
                            sharex=True, sharey=True,
                            )

    G_style = dict(style='single', arrow=True, arrow_param={'width':0.05, 'length': .15})
    Ph_style = dict(style='wiggly', ellipse_spread=.55, xamp=0.035, yamp=-0.05, nloops=5)
    Phel_style = dict(style='elliptic wiggly', circle_radius=.25, xamp=.04, yamp=.05, nloops=15)
    GCircle_style = dict(style='circular', circle_radius=.115, xamp=.04, yamp=.05, nloops=15)
    V_style = dict()

    c=0
    for i in diags:
        print(i,'55')
        get_diagram(axes[c],diags[c],interacts, Ph_style, G_style, V_style, GCircle_style, Phel_style)
        c=c+1

    plt.tight_layout()
    plt.show()
    
def get_diagram(ax,gram,interact,fermion_style, boson_style, vertex_style, Gloop_style, fermionElipse_style):
    D = Diagram(ax)
    w = 0.5
    xy0 = [0.5 - w/2, 0.25]


    def createvertex(inp,prev,count):
        count=D.vertex(prev.xy, dx=2*(w/2), **vertex_style)
        return count,inp
    def counterpart(n,inters):
        for i in inters:
            if i[0]==n:
                return i[1]
            if i[1]==n:
                return i[0]
        
    online=[]
    offline=[]
    gramDeep=deepcopy(gram)

    while len(gram)!=0:
        for i in gram:
            if i[1]!= '00':
                ke=reachzero(i[1],gramDeep)
                je=genloopcheck(i[1],gramDeep)
                if ke[0]==True:
                    online.append(i)
                    gram.remove(i)
                if je[0]==True:
                    offline.append(i)
                    gram.remove(i)
            if i[1]=='00':
                online.append(i)
                gram.remove(i)
    #print(online,'on line')
    #print(offline,'off line')
    hold=[]
    c=0
    deepOnline=deepcopy(online)
    while len(online)!=0:
        for i in online:
            if i[0]=='00':
                v00 = D.vertex(xy0, **vertex_style)
                prev=v00
                tmp=i[1]
                online.remove(i)
            if i[0]==tmp:
                c=c+1
                hol=[]
                hol.append(c)
                hol.append(tmp)
                hold.append(hol)
                v = D.vertex(prev.xy, dx=(w/2), **vertex_style)
                A = D.line(v, prev, **boson_style)
                prev=v
                tmp=i[1]
                if i[1]=='00':
                    v = D.vertex(prev.xy, dx=(w/2), **vertex_style)
                    A = D.line(v, prev, **boson_style)
                online.remove(i)
        inn=[]
        for q in interact:
            save=[]
            for h in hold:
                if q[0]==h[1]:
                    save.append(h[0])
                if q[1]==h[1]:
                    save.append(h[0])
                if len(save)==2:
                    inn.append(save)
        for z in inn:
            v1 = D.vertex(v00.xy, dx=(w/2)*z[0], **vertex_style)
            v2 = D.vertex(v00.xy, dx=(w/2)*z[1], **vertex_style)
            A = D.line(v1, v2, **fermionElipse_style)

    zz=[]
    hh=[]
    for i in offline:
        z=bigloopcheck(i[1],gramDeep)
        h=smallloopcheck(i[1],gramDeep)
        if z[0] == True:
            zz.append(i)
        if h[0] == True:
            hh.append(i)
    print(zz,'zzzzzzzzzzzzz')
    #print(hh,'hhhhhhhhhhhhh')
    onlineLoop=[]
    if len(hh)!=0:
        for i in hh:
            loopcounter=counterpart(i[1],interact)
            for q in deepOnline:
                for k in q:
                    if k==loopcounter:
                        if i not in onlineLoop:
                            onlineLoop.append(i)
    #print(onlineLoop,'LINERRRRR')
    onlineBigLoop=[]
    if len(zz)!=0:
        for i in zz:
            for k in i:
                bigloopcounter=counterpart(k,interact)
                for q in deepOnline:
                    for a in q:
                        if a==bigloopcounter:
                            if i not in onlineBigLoop:
                                onlineBigLoop.append(i)
    print(onlineBigLoop,'OLBL')
    while len(offline)!=0:
        #input()
        end=[]
        for i in onlineLoop:
            ell=counterpart(i[1],interact)
            for q in hold:
                if q[1]==ell:
                    stop=q[0]
                    v1 = D.vertex(v00.xy, dx=(w/2)*stop, **vertex_style)
                    v2 = D.vertex(v00.xy, dx=(w/2)*stop, dy=(w/2), **vertex_style)
                    A = D.line(v2, v2, **Gloop_style)
                    A = D.line(v1, v2, **fermion_style)
                    if i in offline:
                        offline.remove(i)
        eli2=[]
        effi=[]

        fullLine=[]
        oneLine=[]
        count=0
        hold2=[]
        for g in onlineBigLoop:
            eli2=[]
            for f in g:
                eli=counterpart(f,interact)
                eli2.append(eli)
            #print(eli2,'e2222222222222222222222222')
            
            for p in deepOnline:
                c=0
                for o in p:
                    for l in eli2:
                        if l==o:
                            c=c+1
                            if c>1:
                                if eli2 not in fullLine:
                                    fullLine.append(eli2)
                            if c<2:
                                if eli2 not in oneLine:
                                    if eli2 not in fullLine:
                                        oneLine.append(eli2)
                            for q in hold:
                                if q[1]==eli:
                                    if q[1] not in effi:
                                        count=count+1
                                        hol=[]
                                        hol.append(count)
                                        hol.append(q[0])
                                        hold2.append(hol)
                                        #print(count,'count')
                                        effi.append(q[1])
                                        stop=q[0]
                                        v1 = D.vertex(v00.xy, dx=(w/2)*stop, **vertex_style)
                                        v2 = D.vertex(v00.xy, dx=(w/2)*stop, dy=(w/2), **vertex_style)
                                        A = D.line(v1, v2, **fermion_style)
            print(fullLine,'full')
            print(oneLine,'one')
            for d in fullLine:
                for u in d:
                    for q in hold2:
                        if q[1]==u:
                            print(q[0],'COUNT WHENNNNN')
 
        for i in offline:
            if i[0]==i[1]:
                offline.remove(i)

            if i[0]!=i[1]:
                offline.remove(i) 

    
    D.scale(0.5)
    D.plot()
    return D

if __name__ == '__main__':
    main()
