# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 18:49:47 2023

@author: Mariano
"""

# usaTimePeriod.py

from TimePeriod import *

oTimePeriod1 = TimePeriod(1, 10)
oTimePeriod2 = TimePeriod(1, 10)
oTimePeriod3 = TimePeriod(0, 51)

# Print objects (calls the __str__() method)
print(oTimePeriod1)
print(oTimePeriod2)
print(oTimePeriod3)

oTimePeriod4 = oTimePeriod1 + oTimePeriod3
print(oTimePeriod4)

print(oTimePeriod1 == oTimePeriod2)  # True
print(oTimePeriod1 > oTimePeriod2)   # False