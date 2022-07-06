#!usr/bin/python3
def say_my_name(first_name, last_name=""):
    '''
    Print both first name and last name of which both are strings
    
    Raise TypeError exception if either of the first and last names are 
    not strings

    Args:
    first_name(str) 
    last_name(str)

    '''
    if not isinstance (first_name,str):
        raise TypeError("first name must be a string")
    if not isinstance (last_name,str)
        raise TypeError("last name must be a string")
    print("My name is {} {}".format(first_name,last_name))