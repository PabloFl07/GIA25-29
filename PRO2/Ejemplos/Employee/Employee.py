# -*- coding: utf-8 -*-
"""
Irv Kalb.
Object-oriented Python: master OOP by building games and GUIs.
No Starch Press, 2021
"""

# Employee Class

class Employee:

    def __init__(self, name, title, ratePerHour=None):
        self._name = name
        self._title = title
        if ratePerHour is not None:
            ratePerHour = float(ratePerHour)
        self.ratePerHour = ratePerHour

    @property 
    def name(self):
        return self._name

    @name.setter 
    def name(self, name):
        self._name = name
        
    @property 
    def title(self):
        return self._title

    @title.setter 
    def title(self, title):
        self._title = title
        
    def payPerYear(self):
        # 52 weeks * 5 days a week * 8 hours per day
        pay = 52 * 5 * 8 * self.ratePerHour
        return pay
