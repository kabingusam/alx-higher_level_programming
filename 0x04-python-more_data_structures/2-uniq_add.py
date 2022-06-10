#!/usr/bin/python3
def uniq_add(my_list=[]):
    '''add all unique integers in a list (only once for each integer).'''
    # set() - eliminates all duplicates
    return(sum(set(my_list)))
