#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    '''Print all integers of a list, in reverse order.'''
    '''isinstance() function returns True if the specified object is of the specified type, otherwise False.'''
    if isinstance (my_list,list):
        my_list.reverse()
        for i in range(len(my_list)):
            print("{:d}".format(my_list[i]))
    