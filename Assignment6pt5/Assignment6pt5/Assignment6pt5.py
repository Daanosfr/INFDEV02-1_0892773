radius = input("Radius: ")
a = radius #define a b and r to calculate the delta x and delta y in the following lines of code 
b = radius
r = radius
width = 2 * radius + 1 #2 times the radius for the diameter. +1 for the range
height = 2 * radius + 1


map_ = [[' ' for x in range(width)] for y in range(height)] #creates the map-width and height and put's "space" on all points

for y in range(height):
    for x in range(width): 
        if (x-a)**2 + (y-b)**2 - r**2 < r : 
            map_[y][x] = '*' #draw a * on al spots for x & y
for line in map_: #printing the map
    print ' '.join(line) #creates a space between dots and asterisks. join for the sequence.