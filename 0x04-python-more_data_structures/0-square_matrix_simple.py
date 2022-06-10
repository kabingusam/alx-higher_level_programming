#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    '''computes the square value of all integers of a matrix'''
    return([list(map(lambda i: i * i ,row))for row in matrix])
