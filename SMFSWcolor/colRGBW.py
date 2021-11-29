# -*- coding: utf-8 -*-
"""
colRGBW.py
Author: SMFSW
Copyright (c) 2016-2021 SMFSW
Description: RGBW color space class
"""

from colorConv import *
from colorConvTemperature import TEMPtoRGB
from colBase import ColBase as cB
import colRGB as cRGB


class ColRGBW(cB):
    """ RGBW color class
    Inherits from ColBase """
    lfields = ['R', 'G', 'B', 'W']

    def __init__(self, R=0, G=0, B=0, W=0, *args, **kwargs):     # default: Black
        """ Init self with R (Red), G (Green), B (Blue) & W (White) """
        cB.__init__(self, *args, **kwargs)
        self.type = 'RGBW'  # can be used instead of isinstance on an object

        if R in range(256) and G in range(256) and B in range(256) and W in range(256):
            self.R, self.G, self.B, self.W = R, G, B, W
        else:
            self.R = self.G = self.B = self.W = 0

    # TO COLOR SPACE (DIRECT)
    def toRGBW(self):
        """ :return: RGBW class from self """
        return self

    def toRGB(self):
        """ :return: RGB class from self """
        return cRGB.ColRGB(*RGBWtoRGB(*self.refs()))

    # FROM COLOR SPACE (DIRECT)
    @cB.cancel_on(TypeError)
    def fromRGBW(self, *col):
        """ RGBW -> RGBW conversion
        :param col: either RGBW tuple or ColRGBW class
        :return: RGBW class """
        self.R, self.G, self.B, self.W = self._parse_input(ColRGBW, *col)
        return self

    @cB.cancel_on(TypeError)
    def fromRGB(self, *col):
        """ RGB -> RGBW conversion
        :param col: either RGB tuple or ColRGB class
        :return: RGBW class """
        self.R, self.G, self.B, self.W = RGBtoRGBW(*self._parse_input(cRGB.ColRGB, *col))
        return self

    # FROM COLOR SPACE (INDIRECT)
    def fromTemp(self, Temp):
        """ Temperature -> RGBW conversion
        :param Temp: White temperature in Kelvins
        :return: RGBW class """
        self.R, self.G, self.B, self.W = RGBtoRGBW(*TEMPtoRGB(Temp))
        return self


if __name__ == "__main__":
    col_rgbw = ColRGBW(10, 150, 20, 150)
    print(col_rgbw)
    print(str(col_rgbw))
    print(col_rgbw.fromRGB(10, 150, 20))
    print(col_rgbw.fromTemp(3000))
