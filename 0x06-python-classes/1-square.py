#!/usr/bin/python3


"""  a class with private instance """


class Square:
    """ A square class

    Attributes:
        __size (int): size of the side of the square
    """

    def __init__(self, size):
        """ Initializes a squarre

         agrs:
            size (int): size of sqaure side

        Returns: none
        """
        self.__size = size
