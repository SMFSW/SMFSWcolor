# -*- coding: utf-8 -*-
"""
ColYCC.py
Author: SMFSW
Copyright (c) 2016-2025 SMFSW
Description: YCC color space class
"""

from colorConv import *
from colBase import ColBase as cB
import colRGB as cRGB


class ColYCC(cB):
    """ YUV color class
    Inherits from ColBase """
    lfields = ['Y', 'C1', 'C2']

    def __init__(self, Y=0.0, C1=0.0, C2=0.0, *args, **kwargs):  # default: Black
        """ Init with Y, C1, C2 values """
        cB.__init__(self, *args, **kwargs)
        self.type = 'YCC'   # can be used instead of isinstance on an object
        self.Y, self.C1, self.C2 = Y, C1, C2

    # TO COLOR SPACE (DIRECT)
    def toYCC(self):
        """ :return: YCC class from self """
        return self

    def toRGB(self):
        """ :return: RGB class from self """
        return cRGB.ColRGB(*YCCtoRGB(*self.refs()))

    # FROM COLOR SPACE (DIRECT)
    @cB.cancel_on(TypeError)
    def fromYCC(self, *col):
        """ YC1C2 -> YC1C2 conversion
        :param col: either YCC tuple or ColYCC class
        :return: YCC class """
        self.Y, self.C1, self.C2 = self._parse_input(ColYCC, *col)
        return self

    @cB.cancel_on(TypeError)
    def fromRGB(self, *col):
        """ RGB -> YCC conversion
        :param col: either RGB tuple or ColRGB class
        :return: YCC class """
        self.Y, self.C1, self.C2 = RGBtoYCC(*self._parse_input(cRGB.ColRGB, *col))
        return self


if __name__ == "__main__":
    col_YCC = ColYCC()
    print(col_YCC)
    print(str(col_YCC))

