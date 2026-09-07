# -*- coding: utf-8 -*-
"""
Irv Kalb.
Object-oriented Python: master OOP by building games and GUIs.
No Starch Press, 2021
"""

# usaDimmerSwitch2.py

from DimmerSwitch2 import *


oDimmer1 = DimmerSwitch2('Dimmer1')
oDimmer2 = DimmerSwitch2('Dimmer2')

# Turn switch1 on, and raise level 3 times
oDimmer1.turnOn()
oDimmer1.raiseLevel()
oDimmer1.raiseLevel()

# Lower switch2 level 5 times
oDimmer2.raiseLevel()
oDimmer2.raiseLevel()
oDimmer2.raiseLevel()
oDimmer2.raiseLevel()
oDimmer2.raiseLevel()

# Show switches status
oDimmer1.show()
oDimmer2.show()