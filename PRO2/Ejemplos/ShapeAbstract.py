# -*- coding: utf-8 -*-
"""
Irv Kalb.
Object-oriented Python: master OOP by building games and GUIs.
No Starch Press, 2021
"""


# Shape class
#
# To be used as a base class for other classes

import random
from abc import ABC, abstractmethod


class Shape(ABC):  # identifies this as an abstract base class

    def __init__(self, shapeType, maxWidth, maxHeight):
        self.shapeType = shapeType
        self.x = random.randrange(1, maxWidth - 100)
        self.y = random.randrange(25, maxHeight - 100)

    def getType(self):
        return self.shapeType

    @abstractmethod
    def getArea(self):
        pass

class Rectangle(Shape):

    def __init__(self, maxWidth, maxHeight):
        super().__init__('Rectangle', maxWidth, maxHeight)
        self.width = random.randrange(10, 100)
        self.height = random.randrange(10, 100)
 
    # def getArea(self):
    #     theArea = self.width * self.height
    #     return theArea