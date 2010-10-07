#Euler 6: Find the difference between the sum of the squares of the first one hundred natural numbers 
#and the square of the sum.
def DBSuOSqASqOSu(x):
    n=range(1,x+1)
    print n
    print reduce(lambda x,y: (x + y), n)**2
    print reduce(lambda x,y: x + y**2, n)
    return reduce(lambda x,y: (x + y), n)**2-reduce(lambda x,y: x + y**2, n)
print DBSuOSqASqOSu(10)
print DBSuOSqASqOSu(100)
#solution from forum:
def ssq(n):
    answer = 0
    for i in range(n+1):
        answer += pow(i,2)
    return answer

def sqs(m):
    answer = 0
    for j in range(m+1):
        answer += j
    return pow(answer,2)

print sqs(100) - ssq(100) 
