#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """
    A class that represents a square.

    Attributes:
        size (int): The size of the square (1 side).
    """
    def __init__(self, size=0):
        """Initializes a new square instance.

        Args:
            size (int): The size of the square (1 side).
        """
        self.__size = size

    def area(self):
        """Calculates the area of the square.

        Returns:
            int: The calculated area of the square.
        """
        return self.__size ** 2

    @property
    def size(self):
        """Gets the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square.

        Args:
            value (int): The size of the square (1 side).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
