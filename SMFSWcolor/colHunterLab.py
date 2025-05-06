# -*- coding: utf-8 -*-
"""
colHunterLab.py
Author: SMFSW
Copyright (c) 2016-2025 SMFSW
Description: Hunter-L*ab color space class
"""

from colorConv import *
from colBase import ColBase as cB
import colXYZ as cXYZ


class ColHunterLab(cB):
    """ Hunter-L*ab color class
    Inherits from ColBase """
    lfields = ['L', 'a', 'b']

    def __init__(self, L=0.0, a=0.0, b=0.0, *args, **kwargs):    # default: Black
        """ Init with L*, a, b values """
        cB.__init__(self, *args, **kwargs)
        self.type = 'HunterLab'     # can be used instead of isinstance on an object
        self.L, self.a, self.b = L, a, b

    # TO COLOR SPACE (DIRECT)
    def toHunterLab(self):
        """ :return: Hunter-L*ab class from self """
        return self

    def toXYZ(self):
        """ :return: XYZ class from self """
        tmp = self.refs(), self     # append self for observer reference
        return cXYZ.ColXYZ(*HunterLabtoXYZ(*tmp))

    # FROM COLOR SPACE (DIRECT)
    @cB.cancel_on(TypeError)
    def fromHunterLab(self, *col):
        """ Hunter-L*ab -> Hunter-L*ab conversion
        :param col: either Hunter-L*ab tuple or ColHunterLab class
        :return: Hunter-L*ab class """
        self.L, self.a, self.b = self._parse_input(ColHunterLab, *col)
        return self

    @cB.cancel_on(TypeError)
    def fromXYZ(self, *col):
        """ XYZ -> Hunter-L*ab conversion
        :param col: either XYZ tuple or ColXYZ class
        :return: Hunter-L*ab class """
        tmp = self._parse_input(cXYZ.ColXYZ, *col)
        tmp.append(self)    # append self for observer reference
        self.L, self.a, self.b = XYZtoHunterLab(*tmp)
        return self


if __name__ == "__main__":
    col_HLab = ColHunterLab()
    print(col_HLab)
    print(str(col_HLab))
