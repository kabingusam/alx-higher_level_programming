def islower(c):
    '''print lowercase characters'''
    # ord() function returns the number representing the unicode code of a specified character.
    # The ASCII value of the lowercase alphabet is from 97 to 122.
    if ord(c) => 97  and ord(c) <= 122:
        return true
    else:
        return false