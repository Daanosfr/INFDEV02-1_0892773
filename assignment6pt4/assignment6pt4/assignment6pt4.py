x = input("How many rows? ")
for i in range(x, 0, -1):
    white = i * " "
    pyramid = "*" + 2 * (x-i) * "*"
    print white, pyramid
    
