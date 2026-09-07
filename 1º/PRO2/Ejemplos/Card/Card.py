# -*- coding: utf-8 -*-
"""
Irv Kalb.
Object-oriented Python: master OOP by building games and GUIs.
No Starch Press, 2021
"""

# Card Class


class Card():
    def __init__(self, rank, suit, value):
        self.rank = rank
        self.suit = suit
        self.cardName = rank + ' of ' + suit
        self.value = value

    def getName(self):
        return self.cardName

    def getValue(self):
        return self.value

    def getSuit(self):
        return self.suit

    def getRank(self):
        return self.rank
