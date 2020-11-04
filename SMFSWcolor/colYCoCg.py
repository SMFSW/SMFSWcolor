# -*- coding: utf-8 -*-
"""
ColYCoCg.py
Author: SMFSW
Copyright (c) 2016-2018 SMFSW
Description: YCoCg color space class
"""

from colorConv import *
from colBase import ColBase as cB
import colRGB as cRGB


class ColYCoCg(cB):
    """ YUV color class
    Inherits from ColBase """
    lfields = ['Y', 'Co', 'Cg']

    def __init__(self, Y=0.0, Co=0.0, Cg=0.0, *args, **kwargs):  # default: Black
        """ Init with Y, Co, Cg values """
        cB.__init__(self, *args, **kwargs)
        self.type = 'YCoCg'     # can be used instead of isinstance on an object
        self.Y, self.Co, self.Cg = Y, Co, Cg

    # TO COLOR SPACE (DIRECT)
    def toYCoCg(self):
        """ :return: YCoCg class from self """
        return self

    def toRGB(self):
        """ :return: RGB class from self """
        return cRGB.ColRGB(*YCoCgtoRGB(*self.refs()))

    # FROM COLOR SPACE (DIRECT)
    @cB.cancel_on(TypeError)
    def fromYCoCg(self, *col):
        """ YCoCg -> YCoCg conversion
        :param col: either YCoCg tuple or ColYCoCg class
        :return: YCoCg class """
        self.Y, self.Co, self.Cg = self._parse_input(ColYCoCg, *col)
        return self

    @cB.cancel_on(TypeError)
    def fromRGB(self, *col):
        """ RGB -> YCoCg conversion
        :param col: either RGB tuple or ColRGB class
        :return: YCoCg class """
        self.Y, self.Co, self.Cg = RGBtoYCoCg(*self._parse_input(cRGB.ColRGB, *col))
        return self


if __name__ == "__main__":
    col_YCoCg = ColYCoCg()
    print(col_YCoCg)
    print(str(col_YCoCg))

