# -*- coding: utf-8 -*-
"""
Irv Kalb.
Object-oriented Python: master OOP by building games and GUIs.
No Starch Press, 2021
"""

# Triangle class

import random
from Shape import *


class Triangle(Shape):

    def __init__(self, maxWidth, maxHeight):
        super().__init__('Triangle', maxWidth, maxHeight)
        self.base = random.randrange(10, 100)
        self.height = random.randrange(10, 100)

    def getArea(self):
        theArea = .5 * self.base * self.height
        return theArea

    def __str__(self):
        output = super().__str__()
        output += f'Base {self.base}\n'
        output += f'Height {self.height}'
        return output