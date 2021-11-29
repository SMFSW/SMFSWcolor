# -*- coding: utf-8 -*-
"""
colHSV.py
Author: SMFSW
Copyright (c) 2016-2021 SMFSW
Description: HSV color space class
"""

from colorConv import *
from colBase import ColBase as cB
from colorFuncs import Harmonies
import colRGB as cRGB
import colRGBDim as cRGBDim


class ColHSV(cB, Harmonies):
    """ HSV color class
    Inherits from ColBase, Harmonies """
    lfields = ['H', 'S', 'V']

    def __init__(self, H=0.0, S=0.0, V=0.0, *args, **kwargs):   # default: Black
        """ Init with H, S, V values """
        cB.__init__(self, *args, **kwargs)
        self.type = 'HSV'   # can be used instead of isinstance on an object
        self.H, self.S, self.V = H, S, V

    # TO COLOR SPACE (DIRECT)
    def toHSV(self):
        """ :return: HSV class from self """
        return self

    def toRGB(self):
        """ :return: RGB class from self """
        return cRGB.ColRGB(*HSVtoRGB(*self.refs()))

    def toRGBDim(self):
        """ :return: RGBDim class from self """
        return cRGBDim.ColRGBDim(*HSVtoRGBDim(*self.refs()))

    # FROM COLOR SPACE (DIRECT)
    @cB.cancel_on(TypeError)
    def fromHSV(self, *col):
        """ HSV -> HSV conversion
        :param col: either HSV tuple or ColHSV class
        :return: HSV class """
        self.H, self.S, self.V = self._parse_input(ColHSV, *col)
        return self

    @cB.cancel_on(TypeError)
    def fromRGB(self, *col):
        """ RGB -> HSV conversion
        :param col: either RGB tuple or ColRGB class
        :return: HSV class """
        self.H, self.S, self.V = RGBtoHSV(*self._parse_input(cRGB.ColRGB, *col))
        return self

    @cB.cancel_on(TypeError)
    def fromRGBDim(self, *col):
        """ RGBDim -> HSV conversion
        :param col: either RGBDim tuple or ColRGBDim class
        :return: HSV class """
        self.H, self.S, self.V = RGBDimtoHSV(*self._parse_input(cRGBDim.ColRGBDim, *col))
        return self


if __name__ == "__main__":
    col_HSV = ColHSV(30, 60, 192)
    print(col_HSV.toHSV())
    print(col_HSV)
    print(str(col_HSV))

    print(col_HSV.complement())     # from Harmonies class
    print(col_HSV.split_complement())
    print(col_HSV.triadic())
    print(col_HSV.analogous())

"""
HSL, HSB and HSV ranges in standard applications

Application      Space    H range        S range        L/V/B range
Paint Shop Pro   HSL      0 - 255        0 - 255        L  0 - 255
Gimp             HSV      0 - 360deg     0 - 100        V  0 - 100
Photoshop        HSV      0 - 360deg     0 - 100%       B  0 - 100%
Windows          HSL      0 - 240        0 - 240        L  0 - 240
Linux / KDE      HSV      0 - 360deg     0 - 255        V  0 - 255
GTK              HSV      0 - 360deg     0 - 1.0        V  0 - 1.0
Java             HSV      0 - 1.0        0 - 1.0        B  0 - 1.0
Apple            HSV      0 - 360deg     0 - 100%       L  0 - 100%
"""
