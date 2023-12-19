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
        self._Square__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """
        Computes the area of the square.

        Returns:
            int: The area of the square.
        """
        return self._Square__size ** 2


if __name__ == "__main__":
    my_square = Square(89)
    print("Area: {} for size: {}".format(my_square.area(), my_square._Square__size))

    my_square._Square__size = 3
    print("Area: {} for size: {}".format(my_square.area(), my_square._Square__size))

    try:
        my_square._Square__size = "5 feet"
        print("Area: {} for size: {}".format(my_square.area(), my_square._Square__size))
    except Exception as e:
        print(e)
