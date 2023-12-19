#!/usr/bin/python3
"""
Square Class Definition.
"""


class Square:
    """
    Defines the properties of a square.

    Attributes:
        __size (int): Represents the size of a square (1 side).
    """

    def __init__(self, size=0):
        """
        Initializes new square instances.

        Args:
            size (int): Represents the size of the square (1 side).
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
