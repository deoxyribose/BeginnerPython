# Execute the Rank-Sum test for two given samples, with H0: populations identical and alt H1: populations not identical.
def ranksum(x, y):
    n1 = len(x)
    n2 = len(y)
    x = list(x)
    y = list(y)
    tmp = x[:]
    tmp.extend(y)
    tmp.sort()
    rankx = []
    sammetal = 0
    gennem = 0
    for i in range(len(tmp)):
        if tmp.count(tmp[i]) > 1 and tmp[i] in x:
            while sammetal < tmp.count(tmp[i]):
                gennem += i + 1 + sammetal
                sammetal += 1
            for j in range(1,tmp.count(tmp[i])):
                rankx.append(float(gennem) / tmp.count(tmp[i]))
        elif tmp[i] in x:
            rankx.append(i + 1)
    W1 = sum(rankx)
    U1 = W1 - ((n1*(n1+1))/float(2))
    mu = float(n1*n2)/2
    var = float(n1*n2*(n1+n2+1))/12
    sd = var**(0.5)
    Z = float(U1 - mu)/sd
    alpha = input("Choose level of significance; type 5 for 5%, or 1 for 1% ")
    assert alpha == 5 or 1
    if alpha == 5:
        if Z < -1.959964 or Z > 1.959964:
            print "Nul-hypotesen forkastes, da Z ikke ligger i [-1.959964;1.959964]"
        else:
            print "Nul-hypotesen kan ikke forkastes, da Z ligger i [-1.959964;1.959964]. Altsaa er den alternative hypotese sand."
    if alpha ==1:
        if Z < -2.575829 or Z > 2.575829:
            print "Nul-hypotesen forkastes, da Z ikke ligger i [-2.575829;2.575829]"
        else:
            print "Nul-hypotesen kan ikke forkastes, da Z ligger i [-2.575829;2.575829]. Altsaa er den alternative hypotese sand."
    return tmp, rankx, n1, n2, W1, U1, mu, var, sd, Z, alpha
if __name__ == "__main__":
    x = input("List sample 1: ")
    y = input("List sample 2: ")
    print ranksum(x,y) 
