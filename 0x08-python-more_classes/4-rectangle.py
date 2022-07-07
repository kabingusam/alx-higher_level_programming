#!usr/bin/python3
'''Defines a rectangle'''
class Rectangle:
    '''Represents a rectangle'''
    def __init__(self,width = 0,height = 0):
        '''
        Initialize the rectangle
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
        def height(self,value):
            if not isinstance (value,int):
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be >= 0")
            self.__height = value

        def area():
            '''Return the area of the rectangle'''
            return(self.__height * self.__width)

        def perimeter():
            '''Return the perimeter of the rectangle'''
            if (self.__height == 0 or self.__width == 0):
                return(0)
            return((self.__height * 2) + (self.__width * 2))

        def __str__(self):
            '''Return the printable representation of the rectangle'''
            if ((self.__height == 0) or (self.__width == 0)):
                return(0)

        Rectangle []
        for i range (self.__height):
            [Rectangle.append('#') for j in range self.__width]
            if i != self.__height - 1:
                Rectangle.append('\n')
                return("".join(Rectangle))

        def __repr__(self):
            '''return the string representation of the Rectangle'''
            Rectangle = "Rect("+ str(self.__width)
            Rectangle += "," + str(self.__height) + ")"
            return(Rectangle)