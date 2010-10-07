#Programmet vil finde primfaktorerne og vaelge den stoerste:
from math import log
def biggestprime(x):
    factors=[1]
    primes=[1,2]
    n=1
    p=1
    isprime=1
    while p<12000:
        for n in primes:
            if p%n==0 and n!=1 and n!=p and p*factors[-1]<x:
                isprime=0
                break
            n=n+1
        if isprime:
            primes.append(p)
        p=p+1
        n=1
        isprime = 1
    for t in primes:
        if x%t==0:
            factors.append(t)
#returner en liste over primtal, liste over faktorer(for mange 1 taller pga. startdefinitionerne), største faktor, og produkt af faktorer.
    return (primes, factors, "Den stoerste faktor er: "+ str(max(factors)), reduce(lambda x,y: x*y, factors))
if __name__=="__main__":
    print biggestprime(int(raw_input("Skriv tallet: ")))
# Find en bedre måde at begrænse p på.
# Find en bedre måde at generere primtal på (Sieve of Erastothenes).
