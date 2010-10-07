import numpy as np
r=[]
u = []
for i in range(1000):
    omega = [0]
    while omega[-1] not in omega[:-1]:
        omega.append(np.random.random_integers(1,6,size=1)[0])
    r.append(len(omega)-1)
for j in range(1,8):
    u.append(r.count(j))
print u
pr = 0
for k in range(len(u)):
    pr += u[k]/float(sum(u))
    print "%i forekommer med sandsynlighed %f" % (k,u[k]/float(sum(u)))
print "summen er: ", pr
print ""
print 1.0/6, 5.0/18, 5.0/18, 5.0/27, 25.0/324, 5.0/324

