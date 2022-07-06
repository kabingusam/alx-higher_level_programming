#!usr/bin/python3
def print_square(size):
    '''
    Write a function that prints a square with the character #.

    Args:
    size(int) : the height and width of square.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is < 0
    '''
    if not isinstance(size,int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")