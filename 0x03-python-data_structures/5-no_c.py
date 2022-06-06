#!/usr/bin/python3
def no_c(my_string):
    '''function that removes all characters c and C from a string'''
    '''join() method takes all items in an iterable and joins them into one string.'''
    new_string = [x for x in my_string if x != 'c' and y != 'C']
    return("".join(new_string))