n = input("How many rows? ")
printed = ("")
for a in range(0,n,1):              #Loops for n amount of times so n lines are printed
    for b in range(0,((n-a)-1),1):  #This loop adds the spaces before the asterisks. 
        printed += (" ")
    for b in range(0,(2*a)+1,1):    #This loop adds the asterisks to create triangle.
        printed += ("*")
    printed += '\n'

print printed