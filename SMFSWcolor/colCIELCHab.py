# -*- coding: utf-8 -*-
"""
colCIELCHab.py
Author: SMFSW
Copyright (c) 2016-2025 SMFSW
Description: CIE-L*CH°ab color space class
"""

from colorConv import *
from colBase import ColBase as cB
from colorFuncs import Harmonies
import colCIELab as cCIELab


class ColCIELCHab(cB, Harmonies):
    """ CIE-L*CH°ab color class
    Inherits from ColBase, Harmonies """
    lfields = ['L', 'C', 'H']

    def __init__(self, L=0.0, C=0.0, H=0.0, *args, **kwargs):    # default: Black
        """ Init with L*, C, H° values """
        cB.__init__(self, *args, **kwargs)
        self.type = 'CIELCHab'  # can be used instead of isinstance on an object
        self.L, self.C, self.H = L, C, H

    # TO COLOR SPACE (DIRECT)
    def toCIELCHab(self):
        """ :return: CIE-L*CH°ab class from self """
        return self

    def toCIELab(self):
        """ :return: CIE-L*ab class from self """
        return cCIELab.ColCIELab(*CIELCHxxtoCIELxx(*self.refs()))

    # FROM COLOR SPACE (DIRECT)
    @cB.cancel_on(TypeError)
    def fromCIELCHab(self, *col):
        """ CIE-L*CH°ab -> CIE-L*CH°ab conversion
        :param col: either CIE-L*CH°ab tuple or ColCIELCHab class
        :return: CIE-L*CH°ab class """
        self.L, self.C, self.H = self._parse_input(ColCIELCHab, *col)
        return self

    @cB.cancel_on(TypeError)
    def fromCIELab(self, *col):
        """ CIE-L*ab -> CIE-L*CH°ab conversion
        :param col: either CIE-L*ab tuple or ColCIELab class
        :return: CIE-L*CH°ab class """
        self.L, self.C, self.H = CIELxxtoCIELCHxx(*self._parse_input(cCIELab.ColCIELab, *col))
        return self


if __name__ == "__main__":
    col_LCHab = ColCIELCHab()
    print(col_LCHab)
    print(str(col_LCHab))
