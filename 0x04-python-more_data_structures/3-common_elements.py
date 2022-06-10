#!/usr/bin/python3
def common_elements(set_1, set_2):
    '''Returns a set of common elements in two sets'''
    c = [value for value in set_1 if value in set_2]
    return(c)
