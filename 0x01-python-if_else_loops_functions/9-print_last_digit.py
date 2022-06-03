def print_last_digit(number):
    '''print the last didgit of a number and return it'''
    '''Use the modulus operator with 10: This gives the remainder when dividing by 10,
     which will always be the last digit (when the number is positive).'''
    #abs() function returns the absolute value of the specified number.
    print(abs(number) % 10 , end=" ")
    return(abs(number) % 10)