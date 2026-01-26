# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 18:35:51 2023

@author: Mariano
"""

# usaPerson.py

from Person import *

oPerson1 = Person('Joe Schmoe', 90000)
oPerson2 = Person('Jane Smith', 99000)

# Get the salaries using getter and print
print(oPerson1.getSalary())
print(oPerson2.getSalary())

# Change the salaries using setter
oPerson1.setSalary(100000)
oPerson2.setSalary(111111)

# Get the salaries and print again
print(oPerson1.getSalary())
print(oPerson2.getSalary())
