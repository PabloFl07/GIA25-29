# -*- coding: utf-8 -*-
"""
Irv Kalb.
Object-oriented Python: master OOP by building games and GUIs.
No Starch Press, 2021
"""

# Person Class

# Person class

class Person():

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    # Allow the caller to get the salary
    def getSalary(self):
        return self.salary

    # Allow the caller to set a new salary
    def setSalary(self, salary):
        self.salary = salary
