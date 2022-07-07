#!usr/bin/python3
'''
Define the rectangle
'''
class Rectangle:
    '''
    Intitialize the rectangle

    Args:
    width(int) : width of the rectangle
    height(int) : height of the rectangle

    '''
    @property
    def width(self):
        '''get the width of the rectangle'''
        return self.__width

    @width.setter
    def width(self,value):
        if not isinstance (value,int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    
    @property
    def height(self):
        '''get the height of the rectangle'''
        return self.__height

    @height.setter
    def height(self,value):
        if not isinstance (value,int):
            raise TypeError("height must")