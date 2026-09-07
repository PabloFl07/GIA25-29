# -*- coding: utf-8 -*-
"""
Irv Kalb.
Object-oriented Python: master OOP by building games and GUIs.
No Starch Press, 2021
"""

# Shape Class

import random

class Shape():

    def __init__(self, shapeType, maxWidth, maxHeight):
        self.shapeType = shapeType
        self.x = random.randrange(1, maxWidth - 100)
        self.y = random.randrange(25, maxHeight - 100)

    def getType(self):
        return self.shapeType

    def __str__(self):
        output = f'{self.shapeType}\n'
        output += f'Coordinates x={self.x}, y={self.y}\n'
        return output