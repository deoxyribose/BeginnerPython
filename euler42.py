#euler41
# Generate list of triangle numbers up to 26 squared.
# A triangle number is given by the formula ½*t*(t+1)
# Assign a list of all uppercase letters to alpha
# For every word in the words.txt
# For every letter in every word
# Append the corresponding number to the letter. Python counts from 0, so add 1.
# If the sum of the numbers is a triangle number
# Append the word to triword
# Find how many words there are in triword
def triangle(x):
    triword = []
    tri = []
    let = []
    for t in range(1,26):
        tri.append((1/float(2))*t*(t+1))
    alpha = map(chr, range(65, 91))
    for w in x:
        for l in w:
            let.append(alpha.index(l)+1)
        if sum(let) in tri:
            triword.append(w)
        let = []
    return len(triword)
from words import Words
print triangle(Words)
