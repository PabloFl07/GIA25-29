# -*- coding: utf-8 -*-
"""
Irv Kalb.
Object-oriented Python: master OOP by building games and GUIs.
No Starch Press, 2021
"""

# Manager Class

from Employee import *

class Manager(Employee):

    def __init__(self, name, title, salary, staffList=None):
        self._salary = float(salary)
        if staffList is None:
            staffList = []
        self.staffList = staffList
        super().__init__(name, title)

    def getStaffList(self):
        return self.staffList

    def payPerYear(self, giveBonus=False):
        pay = self._salary
        if giveBonus:
            pay = pay + (.10 * self._salary)  # 10% bonus
        return pay

    # Additional methods unique to Manager
    def addEmployee(self, oEmployeeToAdd):
        self.staffList.append(oEmployeeToAdd)

    def removeEmployee(self, oEmployeeToRemove):
        self.staffList.remove(oEmployeeToRemove)
