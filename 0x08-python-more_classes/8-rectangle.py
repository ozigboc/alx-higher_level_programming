#!/usr/bin/python3
"""define a rectangle"""


class Rectangle:
    """Represent a rectangle."""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle.
        Args:
            width (int): the width of a rectangle
            height (int): the height of a rectangle
        """
        Rectangle.number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of a Rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of a Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """prints the rectangle with the character #"""
        if self.__height == 0 or self.__width == 0:
            return("")
        rect = ""
        for i in range(self.__height):
            rect += str(self.print_symbol) * self.__width
            if i + 1 < self.__height:
                rect += '\n'
        return rect

    def __repr__(self) -> str:
        """Return the string representation of the Rectangle."""
        new = "Rectangle(" + str(self.__width)
        new += ", " + str(self.__height) + ")"
        return (new)

    def __del__(self):
        """Destroys the Rectangle"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """static method
        returns the biggest rectangle based on the area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
        raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
