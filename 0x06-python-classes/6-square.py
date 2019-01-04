#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    # Size property
    @property
    def size(self):
        return self.__size

    # Size setter modifies
    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value
    
    # Position property
    @property
    def position(self):
        return self.__position

    # Position setter modifies
    @position.setter
    def position(self, value):
        if type(value) != tuple or len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')

        for items in value:
            if type(items) != int or items < 0:
                raise TypeError('position must be a tuple of 2 positive integers')

        self.__position = value

    # Functions
    def area(self):
        return self.__size ** 2

    def my_print(self):
        size = self.__size
        nl = self.position[1]
        ws = self.position[0]

        if size == 0:
            print()

        for newlines in range(nl):
            print()

        for row in range(size):
            print((' ' * ws) + ('#' * size))
