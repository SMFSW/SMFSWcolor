# -*- coding: utf-8 -*-
"""
colCMY.py
Author: SMFSW
Copyright (c) 2016-2025 SMFSW
Description: CMY color space class
"""

from colorConv import *
from colBase import ColBase as cB
import colRGB as cRGB
import colCMYK as cCMYK


class ColCMY(cB):
    """ CMY color class
    Inherits from ColBase """
    lfields = ['C', 'M', 'Y']

    def __init__(self, C=1.0, M=1.0, Y=1.0, *args, **kwargs):    # default: Black
        """ Init with C, M, Y values """
        cB.__init__(self, *args, **kwargs)
        self.type = 'CMY'   # can be used instead of isinstance on an object
        self.C, self.M, self.Y = C, M, Y

    # TO COLOR SPACE (DIRECT)
    def toCMY(self):
        """ :return: CMY class from self """
        return self

    def toRGB(self):
        """ :return: RGB class from self """
        return cRGB.ColRGB(*CMYtoRGB(*self.refs()))

    def toCMYK(self):
        """ :return: CMYK class from self """
        return cCMYK.ColCMYK(*CMYtoCMYK(*self.refs()))

    # FROM COLOR SPACE (DIRECT)
    @cB.cancel_on(TypeError)
    def fromCMY(self, *col):
        """ CMY -> CMY conversion
        :param col: either CMY tuple or ColCMY class
        :return: CMY class """
        self.C, self.M, self.Y = self._parse_input(ColCMY, *col)
        return self

    @cB.cancel_on(TypeError)
    def fromRGB(self, *col):
        """ RGB -> CMY conversion
        :param col: either RGB tuple or ColRGB class
        :return: CMY class """
        self.C, self.M, self.Y = RGBtoCMY(*self._parse_input(cRGB.ColRGB, *col))
        return self

    @cB.cancel_on(TypeError)
    def fromCMYK(self, *col):
        """ CMYK -> CMY conversion
        :param col: either CMYK tuple or ColCMYK class
        :return: CMY class """
        self.C, self.M, self.Y = CMYKtoCMY(*self._parse_input(cCMYK.ColCMYK, *col))
        return self
   

if __name__ == "__main__":
    col_CMY = ColCMY(0.5, 0.2, 0.1)
    print(col_CMY)
    print(str(col_CMY))
