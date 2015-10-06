import re
running=True
while running:
    p=raw_input("What is your Password? ")
    if len(p) <6:
        print "Your Password is too short, you must at least have 6 characters."
    if len(p) >12:
        print "Your Password is too long, 12 characters is the maximum."
    if 6 <= len(p) <=12:
        print "Your password Length is OK."
        running=False
if re.search(r'[a-z]', p):
    if re.search(r'[A-Z]' ,p):
        if re.search(r'[\d]',p):
            if re.search(r'[^a-zA-Z0-9_]', p):
                print "Your password is super strong!"
            else:
                print "Your password is strong, but you can strengthen it by using a special character."
        else: "Your password is OK, but you can strenghten it by using a digit."
    else: "Your password is too weak, it must contain a uppercase character."
else: "Your password is shit, it must contain lowercase character. "