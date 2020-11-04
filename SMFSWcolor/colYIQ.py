# -*- coding: utf-8 -*-
"""
colYIQ.py
Author: SMFSW
Copyright (c) 2016-2018 SMFSW
Description: YIQ (NTSC) color space class
"""

from colorConv import *
from colBase import ColBase as cB
import colRGB as cRGB


class ColYIQ(cB):
    """ YUV color class
    Inherits from ColBase """
    lfields = ['Y', 'I', 'Q']

    def __init__(self, Y=0.0, I=0.0, Q=0.0, *args, **kwargs):   # default: Black
        """ Init with Y, I, Q values """
        cB.__init__(self, *args, **kwargs)
        self.type = 'YIQ'   # can be used instead of isinstance on an object
        self.Y, self.I, self.Q = Y, I, Q

    # TO COLOR SPACE (DIRECT)
    def toYIQ(self):
        """ :return: YIQ class from self """
        return self

    def toRGB(self):
        """ :return: RGB class from self """
        return cRGB.ColRGB(*YIQtoRGB(*self.refs()))

    # FROM COLOR SPACE (DIRECT)
    @cB.cancel_on(TypeError)
    def fromYIQ(self, *col):
        """ YIQ -> YIQ conversion
        :param col: either YIQ tuple or ColYIQ class
        :return: YIQ class """
        self.Y, self.I, self.Q = self._parse_input(ColYIQ, *col)
        return self

    @cB.cancel_on(TypeError)
    def fromRGB(self, *col):
        """ RGB -> YIQ conversion
        :param col: either RGB tuple or ColRGB class
        :return: YIQ class """
        self.Y, self.I, self.Q = RGBtoYIQ(*self._parse_input(cRGB.ColRGB, *col))
        return self


if __name__ == "__main__":
    col_YIQ = ColYIQ()
    print(col_YIQ)
    print(str(col_YIQ))

