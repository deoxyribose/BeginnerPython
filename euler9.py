from operator import mul
a = range(100,250)
b = range(200,400)
c = range(300,450)
p = []
for i in a:
    for j in b:
        for k in c:
            if i**2+j**2==k**2 and i<j<k:
                p.append((i,j,k))
for l in p:
    if sum(l)==1000:
        print l,reduce(mul,l)
