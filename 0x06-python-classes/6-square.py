#!/usr/bin/python3
"""Define a class Square"""


class Square:
    def __init__(self,size = 0):
        """"Initialize the square

        Args: size(int)  = size of the new square

        """"
        self.size = size

        @property
        def size(self):
            return(self.__size)
        
        @size.setter
        def size(self, value):
            if not isinstance(size,)



