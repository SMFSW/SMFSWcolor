# -*- coding: utf-8 -*-
"""
colCMYK.py
Author: SMFSW
Copyright (c) 2016-2025 SMFSW
Description: CMYK color space class
"""

from colorConv import *
from colBase import ColBase as cB
import colCMY as cCMY


class ColCMYK(cB):
    """ CMYK color class
    Inherits from ColBase """
    lfields = ['C', 'M', 'Y', 'K']

    def __init__(self, C=0.0, M=0.0, Y=0.0, K=1.0, *args, **kwargs):     # default: Black
        """ Init with C, M, Y, K values """
        cB.__init__(self, *args, **kwargs)
        self.type = 'CMYK'  # can be used instead of isinstance on an object
        self.C, self.M, self.Y, self.K = C, M, Y, K

    # TO COLOR SPACE (DIRECT)
    def toCMYK(self):
        """ :return: CMYK class from self """
        return self

    def toCMY(self):
        """ :return: CMY class from self """
        return cCMY.ColCMY(*CMYKtoCMY(*self.refs()))

    # FROM COLOR SPACE (DIRECT)
    @cB.cancel_on(TypeError)
    def fromCMYK(self, *col):
        """ CMYK -> CMYK conversion
        :param col: either CMYK tuple or ColCMYK class
        :return: CMYK class """
        self.C, self.M, self.Y, self.K = self._parse_input(ColCMYK, *col)
        return self

    @cB.cancel_on(TypeError)
    def fromCMY(self, *col):
        """ CMY -> CMYK conversion
        :param col: either CMY tuple or ColCMY class
        :return: CMYK class """
        self.C, self.M, self.Y, self.K = CMYtoCMYK(*self._parse_input(cCMY.ColCMY, *col))
        return self


if __name__ == "__main__":
    col_CMYK = ColCMYK(0.44, 0.11, 0.0, 0.1)
    print(col_CMYK)
    print(str(col_CMYK))
