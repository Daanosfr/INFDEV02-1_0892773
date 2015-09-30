while True:
    tempC = (input("What's the temperature in Celsius? "))    
    if ( tempC > -273.15):
        tempK = tempC  + 273.15
        print "It's ", tempK , "K outside."
        break
    else:
        print" This is not a valid temperature "