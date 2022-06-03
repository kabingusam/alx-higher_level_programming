#!/usr/bin/python3
for n in range (0,10):
    for x in range (n,10):
        if n == 8 and x == 9:
            print("{}{}".format(n,x))
        else:
            print("{}{}".format(n,x),end="")