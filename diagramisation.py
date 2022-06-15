from feynman import Diagram
import matplotlib.pyplot as plt
from topologicalInequiv import *
from generator import *
from functions import *
from copy import deepcopy

n=2
diags=distinctDiagrams(n)
interacts=genny(n)
def main():
    fig, axes = plt.subplots(figsize=(16,8), nrows=1, ncols=len(diags),
                             subplot_kw=dict(aspect='equal', frameon=True),
                             sharex=True, sharey=True,
                            )
    G_style = dict(style='single', arrow=True, arrow_param={'width':0.05, 'length': .15})
    Ph_style = dict(style='wiggly', ellipse_spread=.55, xamp=0.035, yamp=-0.05, nloops=5)
    Phel_style = dict(style='elliptic wiggly', ellipse_spread=-.5, xamp=0.14, yamp=-0.15, nloops=15)
    GCircle_style = dict(style='circular', circle_radius=.115, xamp=.04, yamp=.05, nloops=15)
    Gelip = dict(style='elliptic single', circle_radius=.25, xamp=.04, yamp=.05, nloops=15)
    V_style = dict()
    c=0
    for i in diags:
        get_diagram(axes[c],diags[c],interacts, Ph_style, G_style, V_style, GCircle_style, Phel_style, Gelip)
        c=c+1
    plt.tight_layout()
    plt.show()

def get_diagram(ax,gram,interact,fermion_style, boson_style, vertex_style, Gloop_style, fermionElipse_style,GGelip):
    D = Diagram(ax)
    w = 0.5
    xy0 = [0.06, 0.25]

    def counterpart(n,inters):
        for i in inters:
            if i[0]==n:
                return i[1]
            if i[1]==n:
                return i[0]

    def reachzero_no_out(start,array):
        c=0
        RAY=array.copy()
        while len(RAY)!=0:
            c=c+1
            for k in RAY:
                if k[0]==start:
                    start=k[1]
                    RAY.remove(k)
                    if k[1]=='00':
                        return True
                if c>10:
                    return False
    
    def conned_to_line(inpint,holo):
        cc=counterpart(inpint,interacts)
        c=0
        for i in holo:
            if i[1]==cc:
                return True, inpint, i[1], i[0]
        for i in holo:
            if i[1]!=cc:
                c=c+1
                if c==len(holo):
                    return False, inpint

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
    hold=[]
    c=0
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
    onlineLoop=[]
    if len(hh)!=0:
        for i in hh:
            if i not in onlineLoop:
                onlineLoop.append(i)
    onlineBigLoop=[]
    if len(zz)!=0:
        for i in zz:
            if i not in onlineBigLoop:
                onlineBigLoop.append(i)
    on_line_small_loop=[]
    off_line_small_loop=[]
    for i in onlineLoop:
        toto=counterpart(i[1],interacts)
        truth=reachzero_no_out(toto,gramDeep)
        if truth == True:
            on_line_small_loop.append(i)
        if truth == False:
            off_line_small_loop.append(i)
    hadd=[]
    while len(offline)!=0:
        for i in on_line_small_loop:
            on_line_conterpart=counterpart(i[1],interact)
            for q in hold:
                if q[1]==on_line_conterpart:
                    stop=q[0]
                    v1 = D.vertex(v00.xy, dx=(w/2)*stop, **vertex_style)
                    v2 = D.vertex(v00.xy, dx=(w/2)*stop, dy=(w/2), **vertex_style)
                    A = D.line(v2, v2, **Gloop_style)
                    A = D.line(v1, v2, **fermion_style)
                    if i in offline:
                        offline.remove(i)
        tmp_actual=[]
        c=0
        for i in onlineBigLoop:
            on_line_big_counterpart=counterpart(i[1],interact)
            for q in hold:
                if q[1]==on_line_big_counterpart:
                    if i[1] not in hadd:
                        c=c+1
                        hadd.append(i[1])
                        stop=q[0]
                        v1 = D.vertex(v00.xy, dx=(w/2)*stop, **vertex_style)
                        v2 = D.vertex(v00.xy, dx=(w/2)*stop, dy=(w/2), **vertex_style)
                        A = D.line(v1, v2, **fermion_style)
                        tmpp=[]
                        tmpp.append(c)                                               #bug with count positions
                        tmpp.append(i[1])
                        tmp_actual.append(tmpp)
                        tmp_actual.append(q)
                        if i in offline:
                            offline.remove(i)
        chunk_size = 2
        tmp_act_chunked = [tmp_actual[i:i + chunk_size] for i in range(0, len(tmp_actual), chunk_size)]
        teemp=[]
        of_line_loop=[]
        gnaught_save=[]
        for i in tmp_act_chunked:
            teemp.append(i[0][1])
            if len(teemp)>=2:
                for k in onlineBigLoop:
                    chell=0
                    for l in teemp:
                        if l in k:
                            chell=chell+1
                            if chell>1:
                                of_line_loop.append(k)
                                gnaught_save.append(k)
        for i in of_line_loop:
            sav=[]
            for j in i:
                for k in tmp_act_chunked:
                    if j==k[0][1]:
                        sav.append(k[1][0])
                        for f in gnaught_save:
                            if f in onlineBigLoop:
                                onlineBigLoop.remove(f)
            stop1=sav[0]
            stop2=sav[1]
            v1 = D.vertex(v00.xy, dx=(w/2)*stop1, dy=(w/2), **vertex_style)
            v2 = D.vertex(v00.xy, dx=(w/2)*stop2, dy=(w/2), **vertex_style)
            A = D.line(v2, v1, **GGelip)
        z=[]
        while len(onlineBigLoop)!=0:
            for i in onlineBigLoop:
                z=conned_to_line(i[0],hold)
                if z[0]==True:
                    initial=z[1]
                    stop=int(z[3])
                    v1 = D.vertex(v00.xy, dx=(w/2)*stop, dy=(w/2), **vertex_style)
                    stop2=stop+1
                    v2 = D.vertex(v00.xy, dx=(w/2)*stop2, dy=(w/2), **vertex_style)
                    A = D.line(v2, v1, **GGelip)
                    tmp=i
                    tmp2=i[1]
                    e=tmp[::-1]
                    for s in onlineBigLoop:
                        if s!=tmp:
                            e=s[::-1]
                            if e==tmp:
                                A = D.line(v1, v2, **GGelip)
                    if i in onlineBigLoop:
                            onlineBigLoop.remove(i)
                    if i in offline:
                        offline.remove(i)
                    for o in off_line_small_loop:
                        for p in o:
                            loopcounterpart=counterpart(p,interacts)
                            if loopcounterpart in i:
                                v = D.vertex(v00.xy, dx=(w/2)*stop2, dy=(w/2)*2, **vertex_style)
                                A = D.line(v, v2, **fermion_style)
                                A = D.line(v, v, **Gloop_style)
                                onlineBigLoop=[]
                if i!=tmp:
                    if tmp2 in i:
                        ve = D.vertex(v00.xy, dx=(w/2)*stop2, dy=(w/2)*2, **vertex_style)
                        A = D.line(ve, v2, **GGelip)
                        if i in onlineBigLoop:
                            onlineBigLoop.remove(i)
                        for h in interacts:
                            if tmp2 in h:
                                if i[1] in h:
                                    A = D.line(ve, v2, **fermion_style)
                        if i[1]==initial:
                            A = D.line(v1, ve, **GGelip)
                        tmp=i
                        tmp2=i[1]
    
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