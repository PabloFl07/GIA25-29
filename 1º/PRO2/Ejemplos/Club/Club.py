# -*- coding: utf-8 -*-
"""
Irv Kalb.
Object-oriented Python: master OOP by building games and GUIs.
No Starch Press, 2021
"""

# CLub Class


class Club():

    def __init__(self, clubName, maxMembers):
        self.clubName = clubName
        self.maxMembers = maxMembers
        self.membersList = []

    def addMember(self, name):
        if len(self.membersList) < self.maxMembers:
            self.membersList.append(name)
        else:
            print('Maximum of members reached.')

    def report(self):
        print('Club: ', self.clubName)
        print('Members: ', len(self.membersList))
        for name in self.membersList:
            print('   ' + name)
        print()


oProgrammingClub = Club('Programming', 3)

for name in ['Joe', 'Cindy', 'Dino']:
    oProgrammingClub.addMember(name)

oProgrammingClub.addMember('Nancy')

oProgrammingClub.membersList.append('Nancy')
oProgrammingClub.report()

oProgrammingClub.maxMembers = 'Tres'
oProgrammingClub.addMember('Fred')

