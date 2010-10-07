from  math import *
def sieve(n):
    c = range(2,n)
    for i in range(len(c)):
#The prime number theorem tells us the number of primes less than n is about n/log(n-1).
        if i <= n/log(n-1):
            p = c[i]
        e = [p*x for x in c]
        for d in range(len(e)):
            if e[d] in c:
                c.remove(e[d])
    return c
