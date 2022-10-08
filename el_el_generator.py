from itertools import permutations
import timeit

def var_list(n):
    vars=[]
    c=0
    while n>=c:
        g=str(c)+str(c)
        f=str(c)+'p'
        vars.extend([str(g),str(f)])
        c+=1
    vars.remove('0p')
    return vars

def all_diagrams(n):                    # Finds all permutations of var_list
    perm=permutations(var_list(n))      # then pairs them with the unaltered var_list     
    all_permutations=list(perm)         # yielding all possible diagrams
    final=[]
    for i in all_permutations:
        c=-1
        tmp=[]
        for k in var_list(n):
            c+=1
            tmp.append([k,i[c]])
        final.append(tmp)
    return final