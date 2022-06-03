def uppercase(str):
    ''' print uppercase characters '''
    #chr() function returns the character that represents the specified unicode.
    #ASCII value of the uppercase alphabet is from 65 to 90.
    for c in str:
        if ord(c) => 97 and ord(c) <= 122:
            c =  char(ord(c) - 32)
            print(f"{}".format(c), end=" ")
            print("")