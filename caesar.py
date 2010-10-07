#Caeser
while 1:
    def caesar(o,n):
        alpha="abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
        b=[]
        w=[]
        if n>26:
            n=n-26
        antal=range(len(o))
        for i in antal:
            if o[i] in [" ", ".","'","(",")","()"]:
                w.append(o[i])
            else:
                b=alpha.find(o[i])+int(n)
                w.append(alpha[b])
        return "".join(w)
# Update: .lower() tilfoejet for at omforme tekst til lowercase
    print caesar(raw_input("Skriv ordet: ").lower(),input("Skriv hvor mange bogstaver ordet skal flyttes: "))
    print "For at dechifrere, indtast chifferteksten og -(noeglen)"
