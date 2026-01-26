# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 23:10:42 2023

@author: Mariano Cabrero Canosa
"""

# TimePeriod Class

class TimePeriod:

    def __init__(self, hours=0, minutes=0):
        self.hours = hours
        self.minutes = minutes
        self.value = hours * 60 + minutes

    def getValue(self):
        return self.value

    def __add__(self, oOther):
        '''Add two TimePeriod objects'''
        if not isinstance(oOther, TimePeriod):
            raise TypeError('Second object must be a TimePeriod')
        minutes = self.minutes + oOther.minutes
        hours = self.hours + oOther.hours

        if minutes >= 60:
            minutes -= 60
            hours += 1

        return TimePeriod(hours, minutes)

    def __gt__(self, oOther):
        if not isinstance(oOther, TimePeriod):
            raise TypeError('Second object must be a TimePeriod')
        if self.hours > oOther.hours:
            return True
        elif self.hours < oOther.hours:
            return False
        elif self.minutes > oOther.minutes:
            return True
        else:
            return False

    def __eq__(self, oOther):
        '''Test for equality'''
        if not isinstance(oOther, TimePeriod):
            raise TypeError('Second object must be a TimePeriod')
        return self.hours == oOther.hours and self.minutes == oOther.minutes

    def __str__(self):
        return f"{self.hours} hours, {self.minutes} minutes"


oTimePeriod1 = TimePeriod(1, 10)
print(oTimePeriod1)

oTimePeriod2 = TimePeriod(1, 10)
print(oTimePeriod2)

oTimePeriod3 = TimePeriod(0, 51)
print(oTimePeriod3)

oTimePeriod4 = oTimePeriod1 + oTimePeriod3
print(oTimePeriod4)

print('Are time period 1 and 2 equal?', oTimePeriod1 == oTimePeriod2)
print('Are time period 1 greater than 3?', oTimePeriod1 > oTimePeriod2)









