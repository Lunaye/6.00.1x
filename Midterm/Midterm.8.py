def applyF_filterG(L, f, g):
    newlist = []
    
    for i in L: 
        if g(f(i)) == True:
            newlist.append(i)
    L[:] = newlist
    
    if L == []:
        return (-1)
    
    return max(L)
            
