# -*- coding: utf-8 -*-
"""
colCIELCHuv.py
Author: SMFSW
Copyright (c) 2016-2018 SMFSW
Description: CIE-L*CH°uv color space class
"""

from colorConv import *
from colBase import ColBase as cB
from colorFuncs import Harmonies
import colCIELuv as cCIELuv


class ColCIELCHuv(cB, Harmonies):
    """ CIE-L*CH°uv color class
    Inherits from ColBase, Harmonies """
    lfields = ['L', 'C', 'H']

    def __init__(self, L=0.0, C=0.0, H=0.0, *args, **kwargs):    # default: Black
        """ Init with L*, C, H° values """
        cB.__init__(self, *args, **kwargs)
        self.type = 'CIELCHuv'  # can be used instead of isinstance on an object
        self.L, self.C, self.H = L, C, H

    # TO COLOR SPACE (DIRECT)
    def toCIELCHuv(self):
        """ :return: CIE-L*CH°uv class from self """
        return self

    def toCIELuv(self):
        """ :return: CIE-L*uv class from self """
        return cCIELuv.ColCIELuv(*CIELCHxxtoCIELxx(*self.refs()))

    # FROM COLOR SPACE (DIRECT)
    @cB.cancel_on(TypeError)
    def fromCIELCHuv(self, *col):
        """ CIE-L*CH°uv -> CIE-L*CH°uv conversion
        :param col: either CIE-L*CH°uv tuple or ColCIELCHuv class
        :return: CIE-L*CH°uv class """
        self.L, self.C, self.H = self._parse_input(ColCIELCHuv, *col)
        return self

    @cB.cancel_on(TypeError)
    def fromCIELuv(self, *col):
        """ CIE-L*uv -> CIE-L*CH°uv conversion
        :param col: either CIE-L*uv tuple or ColCIELuv class
        :return: CIE-L*CH°uv class """
        self.L, self.C, self.H = CIELxxtoCIELCHxx(*self._parse_input(cCIELuv.ColCIELuv, *col))
        return self


if __name__ == "__main__":
    col_LCHuv = ColCIELCHuv()
    print(col_LCHuv)
    print(str(col_LCHuv))
