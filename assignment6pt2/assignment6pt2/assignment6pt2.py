size = input("Size of your square: ")
top="*" * size
centreSize = size - 2
centre="*"+ centreSize * " " + "*"
centrePattern= (centre + "\n") * centreSize
print top + "\n" + centrePattern + top