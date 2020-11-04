# -*- coding: utf-8 -*-
"""
colYDbDr.py
Author: SMFSW
Copyright (c) 2016-2018 SMFSW
Description: YDbDr (SECAM & PAL-N) color space class
"""

from colorConv import *
from colBase import ColBase as cB
import colYUV as cYUV
import colRGB as cRGB


class ColYDbDr(cB):
    """ YUV color class
    Inherits from ColBase """
    lfields = ['Y', 'Db', 'Dr']

    def __init__(self, Y=0.0, Db=0.0, Dr=0.0, *args, **kwargs):     # default: Black
        """ Init with Y, Db, Dr values """
        cB.__init__(self, *args, **kwargs)
        self.type = 'YDbDr'     # can be used instead of isinstance on an object
        self.Y, self.Db, self.Dr = Y, Db, Dr

    # TO COLOR SPACE (DIRECT)
    def toYDbDr(self):
        """ :return: YDbDr class from self """
        return self

    def toYUV(self):
        """ :return: YUV class from self """
        return cYUV.ColYUV(*YDbDrtoYUV(*self.refs()))

    def toRGB(self):
        """ :return: RGB class from self """
        return cRGB.ColRGB(*YDbDrtoRGB(*self.refs()))

    # FROM COLOR SPACE (DIRECT)
    @cB.cancel_on(TypeError)
    def fromYDbDr(self, *col):
        """ YDbDr -> YDbDr conversion
        :param col: either YDbDr tuple or ColYDbDr class
        :return: YDbDr class """
        self.Y, self.Db, self.Dr = self._parse_input(ColYDbDr, *col)
        return self

    @cB.cancel_on(TypeError)
    def fromYUV(self, *col):
        """ YUV -> YDbDr conversion
        :param col: either YUV tuple or ColYUV class
        :return: YDbDr class """
        self.Y, self.Db, self.Dr = YUVtoYDbDr(*self._parse_input(cYUV.ColYUV, *col))
        return self

    @cB.cancel_on(TypeError)
    def fromRGB(self, *col):
        """ RGB -> YDbDr conversion
        :param col: either RGB tuple or ColRGB class
        :return: YDbDr class """
        self.Y, self.Db, self.Dr = RGBtoYDbDr(*self._parse_input(cRGB.ColRGB, *col))
        return self


if __name__ == "__main__":
    col_YDbDr = ColYDbDr()
    print(col_YDbDr)
    print(str(col_YDbDr))

