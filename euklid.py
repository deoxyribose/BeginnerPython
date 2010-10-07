#euklids algoritme

def sfd(para1,para2):
    para1=input("Skriv det stoerste tal: ")
    para2=input("Skriv det mindste tal: ")
    rest=para1
    l=range(1,para2);
    while rest>1:
        for i in l:
            if (para1-para2)>para2:
                if para1-i*para2<para2:
                    x=i-1
                    rest=para1-(i-1)*para2  
                else:
                    i+=1
                    rest=para1-2*para2
            elif para1-para2<para2:
                rest=para1-para2
                x=1
            else:
                print "Dit andet tal skal vaere mindre end det foerste!!!! Spasser..."
                break
        print str(para1)+" = "+str(x)+"*"+str(para2)+" + "+str(rest)
        para1=para2
        para2=rest
        
sfd(400,67)
