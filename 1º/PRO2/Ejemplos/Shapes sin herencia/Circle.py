# -*- coding: utf-8 -*-
"""
Irv Kalb.
Object-oriented Python: master OOP by building games and GUIs.
No Starch Press, 2021
"""

# Circle Class

import random
import math

class Circle():

    def __init__(self, maxWidth, maxHeight):
        self.x = random.randrange(1, maxWidth - 100)
        self.y = random.randrange(25, maxHeight - 100)
        self.radius = random.randrange(10, 50)
        self.centerX = self.x + self.radius
        self.centerY = self.y + self.radius
        self.shapeType = 'Circle'

    def getType(self):
        return self.shapeType

    def getArea(self):
        theArea = math.pi * (self.radius ** 2)
        return theArea
