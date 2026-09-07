# -*- coding: utf-8 -*-
"""
Irv Kalb.
Object-oriented Python: master OOP by building games and GUIs.
No Starch Press, 2021
"""

# TV Class


class TV():
    def __init__(self):
        self.isOn = False
        self.isMuted = False

        self.chList = [2, 11, 54, 65]
        self.nChannels = len(self.chList)
        self.chIndex = 0
        self.VOLUME_MIN = 0  # constant
        self.VOLUME_MAX = 10  # constant
        self.volume = self.VOLUME_MAX // 2

    def power(self):
        self.isOn = not self.isOn  # toggle

    def volumeUp(self):
        if not self.isOn:
            return
        if self.isMuted:
            self.isMuted = False
        if self.volume < self.VOLUME_MAX:
            self.volume = self.volume + 1

    def volumeDown(self):
        if not self.isOn:
            return
        if self.isMuted:
            self.isMuted = False
        if self.volume > self.VOLUME_MIN:
            self.volume = self.volume - 1

    def channelUp(self):
        if not self.isOn:
            return
        self.chIndex = self.chIndex + 1
        if self.chIndex > self.nChannels:
            self.chIndex = 0  # wrap around to the first channel

    def channelDown(self):
        if not self.isOn:
            return
        self.chIndex = self.chIndex - 1
        if self.chIndex < 0:
            self.chIndex = self.nChannels - 1  # wrap around to the top channel

    def mute(self):
        if not self.isOn:
            return
        self.isMuted = not self.isMuted

    def setChannel(self, newChannel):
        if newChannel in self.chList:
            self.chIndex = self.chList.index(newChannel)

    def showInfo(self):
        if self.isOn:
            print(' TV is: On')
            print(' Ch:', self.chList[self.chIndex])
            if self.isMuted:
                print(' Volume is:', self.volume, '(muted)')
            else:
                print(' Volume is:', self.volume)
        else:
            print(' TV is: Off')
