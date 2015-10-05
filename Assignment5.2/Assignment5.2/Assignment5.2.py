lengthCheck=True
while lengthCheck:
    p=raw_input("What is your Password? ")
    if len(p) <6:
        print "Your Password is too short, you must at least have 6 characters."
    if len(p) >12:
        print "Your Password is too long, 12 characters is the maximum."
    if 6 <= len(p) <=12:
        print "Your password Length is OK."
        lenghtCheck=False


