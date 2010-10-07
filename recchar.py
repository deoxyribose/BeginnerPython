#Weed out non-alphabet characters.
def reccar(x):
    c=[]
    alpha="abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    for i in x:
        if i in alpha:
            c.append(i)
    return "".join(c)
from data import data
print reccar(data)
