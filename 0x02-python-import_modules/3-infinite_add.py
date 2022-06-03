#!/usr/bin/python3
if _name_ == "_main_":
    '''addition of all arguments'''
    import sys
    count = len(sys.argv)

    for i in range((sys.argv)- 1):
        sum =+ int(sys.argv[i + 1])
    print("{}".format(sum))