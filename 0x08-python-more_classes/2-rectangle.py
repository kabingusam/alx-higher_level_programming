#!usr/bin/python3
'''
Defines a rectangle
'''
class Rectangle:
    '''Represents a rectangle'''
    def __init__(self,width = 0,height = 0)

     ''' 
        Initialize a new rectangle 
        Args: 
        width(int) : width of the rectangle
        height(int) : height of the rectangle
        
    '''
    self.width = width
    self.height = height
    @property
    def width(self):
        '''get the width of the triangle'''
        return  self.__width
        
    @width.setter
    def width(self,value):
        if not isinstance(value,int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self,value):
        if not isinstance(value,int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value
    def area():
        '''Return area of the rectangle'''
        return(self.__width * self.__height)
    def perimeter():
        '''Return perimeter of the rectangle'''
        if (self.__width == 0 or self.__height == 0):
            return(0)
        return((self.__width * 2) + (self.__height * 2))  
