#!/usr/bin/python3
"""
Square Class Definition.
"""


class Square:
    """
    Represents a square with private instance attribute and a public method.
    """

    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int): The size of the square.
        """
        self.__set_size(size)

    def __set_size(self, size):
        """
        Private method to set the size of the square.

        Args:
            size (int): The size of the square.
        """
        if not isinstance(size, int):
            raise TypeError("Size must be an integer")
        elif size < 0:
            raise ValueError("Size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Computes the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2


if __name__ == "__main__":
    my_square = Square(89)
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))

    my_square.__set_size(3)
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))

    try:
        my_square.__set_size("5 feet")
        print("Area: {} for size: {}".format(my_square.area(), my_square.size))
    except Exception as e:
        print(e)
