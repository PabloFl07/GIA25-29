# -*- coding: utf-8 -*-
"""
Irv Kalb.
Object-oriented Python: master OOP by building games and GUIs.
No Starch Press, 2021
"""

# usaManager.py

from Manager import *


# Create objects
oEmployee1 = Employee('Joe', 'Pizza Maker', 16)
oEmployee2 = Employee('Chris', 'Cashier', 14)
oManager = Manager('Sue', 'Manager', 55000, [oEmployee1])

# Add staff members
oManager.addEmployee(oEmployee2)

# Call methods of the Employee1 object
for oEmployee in oManager.getStaffList():
    print(f'Employee name: {oEmployee.name}')
    print(f'Employee salary:', '{oEmployee.payPerYear():.2f}')
print()

# Give the manager a bonus
print(f'{oManager.name} ({oManager.title}) staff members:')
for oEmployee in oManager.getStaffList():
    print(f'\t {oEmployee.name} ({oEmployee.title})')
print(f'Manager salary: {oManager.payPerYear(True):.2f}')

