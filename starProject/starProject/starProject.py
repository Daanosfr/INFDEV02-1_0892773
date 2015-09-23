x = None
while not x:
    try:
        x = int(input("How many rows? "))
    except ValueError:
        print ("Invalid Number")
    

