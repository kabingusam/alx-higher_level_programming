#!/usr/bin/python3
for letter in range(97, 123):
     #The ASCII value of the lowercase alphabet is from 97 to 122.
     #chr() function returns the character that represents the specified unicode.
    if chr(letter) is not 'q' and chr(letter) is not 'e':
        print("{}".format(chr(letter)), end="")