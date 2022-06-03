#!/usr/bin/python3
if _name_ == "_main_":
    '''normal math functions are to be done: add,subtract,muiltply and divide'''
    from calculator_1.py import add,sub,mul,div

    a = 10
    b = 5

    print("{} + {} = {}".format(a,b, add(a,b)))
    print("{} - {} = {}".format(a,b, sub(a,b)))
    print("{} * {} = {}".format(a,b, mul(a,b)))
    print("{} / {} = {}".format(a,b, div(a,b)))