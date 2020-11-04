# -*- coding: utf-8 -*-
"""
colYCbCr.py
Author: SMFSW
Copyright (c) 2016-2018 SMFSW
Description: YCbCr color space class
"""

from colorConv import *
from colBase import ColBase as cB
import colRGB as cRGB


class ColYCbCr(cB):
    """ YUV color class
    Inherits from ColBase """
    lfields = ['Y', 'Cb', 'Cr']

    def __init__(self, Y=0.0, Cb=0.0, Cr=0.0, *args, **kwargs):     # default: Black
        """ Init with Y, Cb, Cr values """
        cB.__init__(self, *args, **kwargs)
        self.type = 'YCbCr'     # can be used instead of isinstance on an object
        self.Y, self.Cb, self.Cr = Y, Cb, Cr

    # TO COLOR SPACE (DIRECT)
    def toYCbCr(self):
        """ :return: YCbCr class from self """
        return self

    def toRGB(self):
        """ :return: RGB class from self """
        return cRGB.ColRGB(*YCbCrtoRGB(*self.refs()))

    # FROM COLOR SPACE (DIRECT)
    @cB.cancel_on(TypeError)
    def fromYCbCr(self, *col):
        """ YCbCr -> YCbCr conversion
        :param col: either YCbCr tuple or ColYCbCr class
        :return: YCbCr class """
        self.Y, self.Cb, self.Cr = self._parse_input(ColYCbCr, *col)
        return self

    @cB.cancel_on(TypeError)
    def fromRGB(self, *col):
        """ RGB -> YCbCr conversion
        :param col: either RGB tuple or ColRGB class
        :return: YCbCr class """
        self.Y, self.Cb, self.Cr = RGBtoYCbCr(*self._parse_input(cRGB.ColRGB, *col))
        return self


if __name__ == "__main__":
    col_YCbCr = ColYCbCr()
    print(col_YCbCr)
    print(str(col_YCbCr))

