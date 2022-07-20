#!/usr/bin/python3

""" Class that defines a square """


class Square:
    """ This defines the class square """
    def __init__(self, size=0):
        """ This object defines Size of square side
            Args: self , size = 0
        """
        if type(size) is not int:
            raise TypeError("sizie must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0)
            else:
                self.__size = size
