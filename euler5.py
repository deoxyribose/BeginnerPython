#Euler 5
def smalln(x):
    r=range(1,x)
    c=[]
    d=[]
    n=[]
    i=0
    while x>1 and x-i!=0:
       for i in r:
            if x%(x-i)!=0 and len(c)<x and d.count(x-i)==0:
                c.append(1)
            elif len(c)<x:
                c.append(0)
                d.append(x-i)
            if c==[1,1,1,1,1,1,1,1,1,1] and len(c)==x:
                n.append(x)
                x+=-1
            print c,n
       x+=-1
    return c
print smalln(10)
         
