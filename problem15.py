import time

d = dict({(1,1):2,(2,2):6,(2,1):3,(1,2):3})

def paths(m,n):
    if (m,n) in d:
        return d[(m,n)]
    elif m==0:
        d[(m,n)] = 1
        return 1
    elif n==0:
        d[(m,n)] = 1
        return 1
    else:
        d[(m,n)] = paths(m-1,n) + paths(m,n-1)
        return paths(m-1,n) + paths(m,n-1)
    

t = time.clock()
print paths(20,20)
print "computation took", time.clock()-t,"seconds"
