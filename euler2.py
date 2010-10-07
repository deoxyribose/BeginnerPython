#Jeg starter med at definere en liste, fib, med de første to elementer, 1 og 1.
fib=[1,1]
#Laver en "for" loop som mens det sidste element i fib er mindre end 4 millioner, adderer det næstesidste og sidste tal i fib og tilføjer det i enden af fib.
for n in fib:
    while fib[-1]<4000000:
            fib.append(fib[-2]+fib[-1])
            n=n+1
#Viser summen af hvert tredje tal i sekvensen, startende med 2. Hvert tredje tal er lige.
print sum(fib[2::3])

