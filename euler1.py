def multiples(nat=1):
    multipler=[]
    while nat < 1000:
        if nat%3==0:
            multipler.append(nat)
        elif  nat%5==0:
            multipler.append(nat)
        nat = nat+1
    return sum(multipler)
# samme metode, skrevet direkte ind i shell: sum([x for x in range(1000) if x % 3== 0 or x % 5== 0]) 
