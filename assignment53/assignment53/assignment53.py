import sys
word = raw_input("Give me a word or a sentence: ") #asks for input sentence or word
n = input("How much do you want to shift? ") #asks for number of shift


for c in word:
    c = ord(c) #turn letters into number
    if ord('a') <= c <= ord('z'): #if its number is between the values of the lower a and lower z
        c = c - ord('a') #decrease the value to its value counting from 1 to make it possible to calculate between 1 and 26.
        c = (c + n) % 26 #calculates with a max of 26
        c = c + ord('a') #add the amount we decreased the number earlier so it will be back at its original range.
        c = chr(c) #turns the number back into a character

    elif ord('A') <= c <= ord('Z'): #same here only this time with capital letters
        c = c - ord('A')
        c = (c + n) % 26
        c = c + ord('A')
        c = chr(c)
    else:
        c = chr(c) #numbers and special characters will automaticaly be printed
    sys.stdout.write(c) #prints it without enters
sys.stdout.write('\n') #exit on next line

