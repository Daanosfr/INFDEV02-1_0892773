x = input ("how many rows? ")
printed = ("")              #The printing string
n = x + 1                   #Make sure it is x rows becasue of the range
for a in range(n):      #Main for loop which prints n amount of lines
    for b in range(a):  #For loop which adds a amount of asterisks per line
        printed += '*'
    printed += '\n'         

print printed