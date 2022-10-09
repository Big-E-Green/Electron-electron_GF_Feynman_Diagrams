from el_el_generator import *
from el_el_genFunctions import *

def connected_check(inp,n):
    for i in inp:
        if i==['00', '00']:
            return False 
    direct_on_line=[]                                    # finds all on_line varibles
    for k in var_list(n):                                # saves to said array
        epsilon=reachzero(k,inp)
        if epsilon[0]==True:
            for l in epsilon[1]:
                for g in l:
                    if g not in direct_on_line:
                        direct_on_line.append(g)
                        if len(direct_on_line)==len(inp):
                            return True
    final_big_array=[]
    for q in var_list(n):
        eta=bigloopcheck(q,inp)
        if eta[0]==True:
            big_array=[]
            for j in eta[1]:
                for h in j:
                    if h not in big_array:
                        big_array.append(h)
            final_big_array.append(big_array)
    remm=[]
    for w in final_big_array:
        for y in w:
            if y in direct_on_line:
                if w not in remm:
                    remm.append(w)
                for t in w:
                    if t not in direct_on_line:
                        direct_on_line.append(t)
            z=counterpart(y,genall2(n))
            if z in direct_on_line:
                if w not in remm:
                    remm.append(w)
                for t in w:
                    if t not in direct_on_line:
                        direct_on_line.append(t)
    for i in remm:
        if i in final_big_array:
            final_big_array.remove(i)
    if final_big_array!=[]:
        counter=5
        while counter!=0:
            counter-=1
            for p in final_big_array:
                for f in p:
                    eta=counterpart(f,genall2(n))
                    if eta in direct_on_line:
                        if f not in direct_on_line:
                            direct_on_line.append(f)
                            if f in p:
                                p.remove(f)
    if len(direct_on_line)==len(inp):
        return True
    for i in var_list(n):
        mu=smallloopcheck(i,inp)
        if mu[0]==True:
            var=mu[1][0][0]
            zeta=counterpart(var,genall2(n))
            if zeta in direct_on_line:
                if var not in direct_on_line:
                    direct_on_line.append(var)

    if len(direct_on_line)==len(inp):
        return True                
    return False