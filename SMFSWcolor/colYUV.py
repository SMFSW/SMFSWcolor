# -*- coding: utf-8 -*-
"""
colYUV.py
Author: SMFSW
Copyright (c) 2016-2021 SMFSW
Description: YUV (PAL) color space class
"""

from colorConv import *
from colBase import ColBase as cB
import colYDbDr as cYDbDr
import colRGB as cRGB


class ColYUV(cB):
    """ YUV color class
    Inherits from ColBase """
    lfields = ['Y', 'U', 'V']

    def __init__(self, Y=0.0, U=0.0, V=0.0, *args, **kwargs):   # default: Black
        """ Init with Y, U, V values """
        cB.__init__(self, *args, **kwargs)
        self.type = 'YUV'   # can be used instead of isinstance on an object
        self.Y, self.U, self.V = Y, U, V

    # TO COLOR SPACE (DIRECT)
    def toYUV(self):
        """ :return: YUV class from self """
        return self

    def toYDbDr(self):
        """ :return: YDbDr class from self """
        return cYDbDr.ColYDbDr(*YUVtoYDbDr(*self.refs()))

    def toRGB(self):
        """ :return: RGB class from self """
        return cRGB.ColRGB(*YUVtoRGB(*self.refs()))

    # FROM COLOR SPACE (DIRECT)
    @cB.cancel_on(TypeError)
    def fromYUV(self, *col):
        """ YUV -> YUV conversion
        :param col: either YUV tuple or ColYUV class
        :return: YUV class """
        self.Y, self.U, self.V = self._parse_input(ColYUV, *col)
        return self

    @cB.cancel_on(TypeError)
    def fromYDbDr(self, *col):
        """ YDbDr -> YUV conversion
        :param col: either YDbDr tuple or ColYDbDr class
        :return: YUV class """
        self.Y, self.U, self.V = YDbDrtoYUV(*self._parse_input(cYDbDr.ColYDbDr, *col))
        return self

    @cB.cancel_on(TypeError)
    def fromRGB(self, *col):
        """ RGB -> YUV conversion
        :param col: either RGB tuple or ColRGB class
        :return: YUV class """
        self.Y, self.U, self.V = RGBtoYUV(*self._parse_input(cRGB.ColRGB, *col))
        return self


if __name__ == "__main__":
    col_YUV = ColYUV()
    print(col_YUV)
    print(str(col_YUV))
