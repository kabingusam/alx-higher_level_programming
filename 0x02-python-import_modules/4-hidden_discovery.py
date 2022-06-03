#!/usr/bin/python3
if _name_ = "_main_":
    '''dir() function is used to list all defined names belonging to a function'''
    import hidden_4
    names_defined = dir(hidden_4)
    for name in names_defined:
        if name[:2] != '__':
            print(name)