while True:
    tempC = int(input("What's the temperature in Celsius? "))    
    if ( tempC > -273.15):
        K = C  + 273.15
        print ("It's ", Kelvin , "K outside.")
        break
    else:
        print(" This is not a valid temperature ")