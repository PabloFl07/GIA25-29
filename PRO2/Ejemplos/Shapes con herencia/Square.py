# -*- coding: utf-8 -*-
"""
Irv Kalb.
Object-oriented Python: master OOP by building games and GUIs.
No Starch Press, 2021
"""

# Square class

from Shape import *
import random


class Square(Shape):

    def __init__(self, maxWidth, maxHeight):
        super().__init__('Square', maxWidth, maxHeight)
        self.widthAndHeight = random.randrange(10, 100)

    def getArea(self):
        theArea = self.widthAndHeight ** 2
        return theArea

    def __str__(self):
        output = super().__str__()
        output += f'Side {self.widthAndHeight}\n'
        return output