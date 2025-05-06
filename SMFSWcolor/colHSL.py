# -*- coding: utf-8 -*-
"""
colHSL.py
Author: SMFSW
Copyright (c) 2016-2025 SMFSW
Description: HSL color space class
"""

from colorConv import *
from colBase import ColBase as cB
from colorFuncs import Harmonies
import colRGB as cRGB


class ColHSL(cB, Harmonies):
    """ HSL color class
    Inherits from ColBase, Harmonies """

    lfields = ['H', 'S', 'L']

    def __init__(self, H=-1.0, S=0.0, L=0.0, *args, **kwargs):   # default: Black
        """ Init with H, S, L values """
        cB.__init__(self, *args, **kwargs)
        self.type = 'HSL'   # can be used instead of isinstance on an object
        self.H, self.S, self.L = H, S, L

    # TO COLOR SPACE (DIRECT)
    def toHSL(self):
        """ :return: HSL class from self """
        return self

    def toRGB(self):
        """ :return: RGB class from self """
        return cRGB.ColRGB(*HSLtoRGB(*self.refs()))

    # FROM COLOR SPACE (DIRECT)
    @cB.cancel_on(TypeError)
    def fromHSL(self, *col):
        """ HSL -> HSL conversion
        :param col: either HSL tuple or ColHSL class
        :return: HSL class """
        self.H, self.S, self.L = self._parse_input(ColHSL, *col)
        return self

    @cB.cancel_on(TypeError)
    def fromRGB(self, *col):
        """ RGB -> HSL conversion
        :param col: either RGB tuple or ColRGB class
        :return: HSL class """
        self.H, self.S, self.L = RGBtoHSL(*self._parse_input(cRGB.ColRGB, *col))
        return self


if __name__ == "__main__":
    col_HSL = ColHSL(30, 60, 192)
    print(col_HSL)
    print(str(col_HSL))


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
