x = input("Size of square: ") #asks for input
square = ""

for i in range(x):
    for j in range (x):
        square += '*'
    square += '\n'
print square

