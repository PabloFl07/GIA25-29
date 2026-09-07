# -*- coding: utf-8 -*-
"""
Irv Kalb.
Object-oriented Python: master OOP by building games and GUIs.
No Starch Press, 2021
"""

# Square class

import random

class Square():

    def __init__(self, maxWidth, maxHeight):
        self.widthAndHeight = random.randrange(10, 100)
        self.x = random.randrange(1, maxWidth - 100)
        self.y = random.randrange(25, maxHeight - 100)
        self.shapeType = 'Square'

    def getType(self):
        return self.shapeType

    def getArea(self):
        theArea = self.widthAndHeight * self.widthAndHeight
        return theArea
