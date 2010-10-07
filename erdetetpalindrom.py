def vend(s):
    return s[::-1]
s = raw_input("Skriv ordet: ").lower()
b = []
antal=range(len(s))
for i in antal:
    if s[i].isalpha():
        b.append(s[i])
b = "".join(b)
v = vend(b)
print(v)
print(b)
if b==v:
    print(s + " is a palindrome...!")
else:
    print(s + " is not a palindrome...!")
