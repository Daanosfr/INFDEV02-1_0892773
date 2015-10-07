n = input("Give me the size of the hallow square: ")
square = ("")                      #The printing string

for a in range(0,n,1):              #Top line which is n amount of asterisks
    square += ("*")                  
square += ("\n")                     
for b in range(0,(n-2),1):          #Prints the middle lines n-2 times
    square += ("*")      
    for c in range(0,(n-2),1):      #Prints the middle 'empty' section of the n-2 lines.
        square += (" ")
    square += ("*")
    square += ("\n")
for d in range(0,n,1):              #Bottom line of n amount of asterisks
    square += ("*")                
square += ("\n")                   
        
print square
                       #Prints square.