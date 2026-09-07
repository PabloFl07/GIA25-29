# -*- coding: utf-8 -*-
"""
Irv Kalb.
Object-oriented Python: master OOP by building games and GUIs.
No Starch Press, 2021
"""

# usaShapes.py

from Square import *
from Circle import *
from Triangle import *

# Set up the constants
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
N_SHAPES = 4

# Creation list of shapes
shapesList = []
shapeClassesTuple = (Square, Circle, Triangle)
for i in range(0, N_SHAPES):
    randomlyChosenClass = random.choice(shapeClassesTuple)
    oShape = randomlyChosenClass(WINDOW_WIDTH, WINDOW_HEIGHT)
    shapesList.append(oShape)

# Main loop
for oShape in shapesList:
    print(oShape)
    area = oShape.getArea()
    print(f'Area is {area:.2f}\n')