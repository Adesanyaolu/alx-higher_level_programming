#!/usr/bin/python3

""" A rectangle class """


class Rectangle:

    """
        Class that defines a Rectangle
    """

    def __init__(self, width=0, height=0):
        """ initializes the class """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Get triangle width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Set triangle width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Get triangle height """
        return self.__height

    @height.setter
    def height(self, value):
        """ set triangle height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
