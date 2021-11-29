# -*- coding: utf-8 -*-
"""
colRGBDim.py
Author: SMFSW
Copyright (c) 2016-2021 SMFSW
Description: RGBDim color space class
"""

from colorConv import *
from colorConvTemperature import TEMPtoRGB
from colBase import ColBase as cB
import colRGB as cRGB
import colHSV as cHSV


class ColRGBDim(cB):
    """ RGBDim color class
    Inherits from ColBase """
    lfields = ['R', 'G', 'B', 'Dim']

    def __init__(self, R=0, G=0, B=0, Dim=100.0, *args, **kwargs):     # default: Black
        """ Init self with R (Red), G (Green), B (Blue) & Dim (Dimming with limit of 255%... Higher values doesn't make sense) """
        cB.__init__(self, *args, **kwargs)
        self.type = 'RGBDim'    # can be used instead of isinstance on an object

        if R in range(256) and G in range(256) and B in range(256):
            self.R, self.G, self.B = R, G, B
            self.Dim = max(0.0, min(Dim, 255.0))
        else:
            self.R = self.G = self.B = 0
            self.Dim = 100.0

    # TO COLOR SPACE
    def toRGBDim(self):
        """ :return: RGBDim class from self """
        return self

    def toRGB(self):
        """ :return: RGB class from self """
        return cRGB.ColRGB(*RGBDimtoRGB(*self.refs()))

    def toHSV(self):
        """ :return: HSV class from self """
        return cHSV.ColHSV(*RGBDimtoHSV(*self.refs()))

    # FROM COLOR SPACE (DIRECT)
    @cB.cancel_on(TypeError)
    def fromRGBDim(self, *col):
        """ RGBDim -> RGBDim conversion
        :param col: either RGBDim tuple or ColRGBDim class
        :return: RGBDim class """
        self.R, self.G, self.B, self.Dim = self._parse_input(ColRGBDim, *col)
        return self

    @cB.cancel_on(TypeError)
    def fromRGB(self, *col):
        """ RGB -> RGBDim conversion
        :param col: either RGB tuple or ColRGB class
        :return: RGBDim class """
        self.R, self.G, self.B, self.Dim = RGBtoRGBDim(*self._parse_input(cRGB.ColRGB, *col))
        return self

    @cB.cancel_on(TypeError)
    def fromHSV(self, *col):
        """ HSV -> RGBDim conversion
        :param col: either HSV tuple or ColHSV class
        :return: RGBDim class """
        self.R, self.G, self.B, self.Dim = HSVtoRGBDim(*self._parse_input(cHSV.ColHSV, *col))
        return self

    # FROM COLOR SPACE (INDIRECT)
    def fromTemp(self, Temp):
        """ Temperature -> RGBDim conversion
        :param Temp: White temperature in Kelvins
        :return: RGBDim class """
        self.R, self.G, self.B, self.Dim = RGBtoRGBDim(*TEMPtoRGB(Temp))
        return self


if __name__ == "__main__":
    col_rgbDim = ColRGBDim(10, 150, 20, 90.0)
    print(col_rgbDim)
    print(str(col_rgbDim))
    print(col_rgbDim.fromTemp(3000))
