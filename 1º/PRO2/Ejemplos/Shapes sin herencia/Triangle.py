# -*- coding: utf-8 -*-
"""
Irv Kalb.
Object-oriented Python: master OOP by building games and GUIs.
No Starch Press, 2021
"""

# Triangle Class

import random

class Triangle():

    def __init__(self, maxWidth, maxHeight):
        self.base = random.randrange(10, 100)
        self.height = random.randrange(10, 100)
        self.x = random.randrange(1, maxWidth - 100)
        self.y = random.randrange(25, maxHeight - 100)
        self.shapeType = 'Triangle'

    def getType(self):
        return self.shapeType

    def getArea(self):
        theArea = .5 * self.base * self.height
        return theArea
