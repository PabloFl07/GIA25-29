# -*- coding: utf-8 -*-
"""
Irv Kalb.
Object-oriented Python: master OOP by building games and GUIs.
No Starch Press, 2021
"""

# usaDimmerSwitch.py

from DimmerSwitch import *

oDimmer = DimmerSwitch()

# Turn switch on, and raise level 3 times
oDimmer.turnOn()
oDimmer.raiseLevel()
oDimmer.raiseLevel()
oDimmer.raiseLevel()
oDimmer.show()

# Lower level 2 times, and turn switch off
oDimmer.lowerLevel()
oDimmer.lowerLevel()
oDimmer.turnOff()
oDimmer.show()

# Turn switch on, and raise level 1 time
oDimmer.turnOn()
oDimmer.raiseLevel()
oDimmer.show()
