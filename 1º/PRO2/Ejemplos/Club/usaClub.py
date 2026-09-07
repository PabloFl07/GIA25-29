# -*- coding: utf-8 -*-
"""
Irv Kalb.
Object-oriented Python: master OOP by building games and GUIs.
No Starch Press, 2021
"""

# usaClub.py

from Club import *	

oProgrammingClub = Club('Programming', 3)

for name in ['Joe', 'Cindy', 'Dino']:
    oProgrammingClub.addMember(name)

oProgrammingClub.addMember('Nancy')

oProgrammingClub.membersList.append('Nancy')
oProgrammingClub.report()

oProgrammingClub.maxMembers = 'Tres'
oProgrammingClub.addMember('Fred')
