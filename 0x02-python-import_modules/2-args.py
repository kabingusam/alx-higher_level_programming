#!/usr/bin/python3
if _name_ = "_main_":
    '''print the number and list of arguments.Conditions for 0 and 1 already given'''
    # len is used to give the number of elements of arg.
    import sys

    count = len(sys.argv)
    if count == 0:
        print("0 arguments")
    elif count == 1:
        print("1 argument: ")
    else:
        print("{} arguments: ".format(count))
    for i in range(count):
        print("{} : {}".format(i+1,sys.argv[i+1]))