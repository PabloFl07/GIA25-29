# -*- coding: utf-8 -*-
"""
Irv Kalb.
Object-oriented Python: master OOP by building games and GUIs.
No Starch Press, 2021
"""

# Deck Class


import random
from Card import *


class Deck():
    SUIT_TUPLE = ('Diamonds', 'Clubs', 'Hearts', 'Spades')
    STANDARD_DICT = {'Ace': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
                      '9': 9, '10': 10, 'Jack': 11, 'Queen': 12, 'King': 13}

    def __init__(self, rankValueDict=STANDARD_DICT):
        self.startingDeckList = []
        self.playingDeckList = []
        for suit in Deck.SUIT_TUPLE:
            for rank, value in rankValueDict.items():
                oCard = Card(rank, suit, value)
                self.startingDeckList.append(oCard)
        self.shuffle()

    def shuffle(self):
        # Copy the starting deck and save it in the playing deck list
        self.playingDeckList = self.startingDeckList.copy()
        random.shuffle(self.playingDeckList)

    def getCard(self):
        if len(self.playingDeckList) == 0:
            raise IndexError('No more cards')
        # Pop one card off the deck and return it
        oCard = self.playingDeckList.pop()
        return oCard

    def returnCardToDeck(self, oCard):
        # Put a card back into the deck
        self.playingDeckList.insert(0, oCard)
