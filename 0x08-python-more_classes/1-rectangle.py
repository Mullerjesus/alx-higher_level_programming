#!/usr/bin/python3
"""Defines a Rectangle class."""

class Rectangle:
"""Represents a rectangle shape."""

def __init__(self, width=0, height=0):
"""Initializes a rectangle with a given width and height."""
self.width = width
self.height = height

@property
def width(self):
"""Retrieves the width of the rectangle."""
return self.__width

@width.setter
def width(self, value):
"""Sets the width of the rectangle."""
if not isinstance(value, int):
raise TypeError("width must be an integer")
elif value < 0:
raise ValueError("width must be >= 0")
self.__width = value

@property
def height(self):
"""Retrieves the height of the rectangle."""
return self.__height

@height.setter
def height(self, value):
"""Sets the height of the rectangle."""
if not isinstance(value, int):
raise TypeError("height must be an integer")
elif value < 0:
raise ValueError("height must be >= 0")
self.__height = value

def __str__(self):
"""Returns a string representation of the rectangle."""
return "[Rectangle] {}/{}".format(self.__width, self.__height)
