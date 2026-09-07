# -*- coding: utf-8 -*-
"""
Irv Kalb.
Object-oriented Python: master OOP by building games and GUIs.
No Starch Press, 2021
"""

# Circle class

from Shape import *
import math
import random


class Circle(Shape):

    def __init__(self, maxWidth, maxHeight):
        super().__init__('Circle', maxWidth, maxHeight)
        self.radius = random.randrange(10, 50)
        self.centerX = self.x + self.radius
        self.centerY = self.y + self.radius

    def getArea(self):
        theArea = math.pi * (self.radius ** 2)
        return theArea

    def __str__(self):
        output = super().__str__()
        output += f'Radius {self.radius}'
        return output