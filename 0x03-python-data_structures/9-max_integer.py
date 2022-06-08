#!/usr/bin/python3
def max_integer(my_list=[]):
    '''find the biggest integer of a list'''
    if len(my_list) < 0:
        return(None)
    else:
        my_list.sort()
        highest = my_list[-1]
        return(highest)
