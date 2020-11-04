# -*- coding: utf-8 -*-
"""
colCIELuv.py
Author: SMFSW
Copyright (c) 2016-2018 SMFSW
Description: CIE-L*uv color space class
"""

from colorConv import *
from colBase import ColBase as cB
import colCIELCHuv as cCIELCHuv
import colXYZ as cXYZ


class ColCIELuv(cB):
    """ CIE-L*uv color class
    Inherits from ColBase """
    lfields = ['L', 'u', 'v']

    def __init__(self, L=0.0, u=0.0, v=0.0, *args, **kwargs):    # default: Black
        """ Init with L*, u, v values """
        cB.__init__(self, *args, **kwargs)
        self.type = 'CIELuv'    # can be used instead of isinstance on an object
        self.L, self.u, self.v = L, u, v

    # TO COLOR SPACE (DIRECT)
    def toCIELuv(self):
        """ :return: CIE-L*uv class from self """
        return self

    def toXYZ(self):
        """ :return: XYZ class from self """
        tmp = self.refs(), self
        return cXYZ.ColXYZ(*CIELuvtoXYZ(*tmp))

    def toCIELCHuv(self):
        """ :return: CIE-L*CH°uv class from self """
        return cCIELCHuv.ColCIELCHuv(*CIELxxtoCIELCHxx(*self.refs()))

    # FROM COLOR SPACE (DIRECT)
    @cB.cancel_on(TypeError)
    def fromCIELuv(self, *col):
        """ CIE-L*uv -> CIE-L*uv conversion
        :param col: either CIE-L*uv tuple or ColCIELuv class
        :return: CIE-L*uv class """
        self.L, self.u, self.v = self._parse_input(ColCIELuv, *col)
        return self

    @cB.cancel_on(TypeError)
    def fromXYZ(self, *col):
        """ XYZ -> CIE-L*uv conversion
        :param col: either XYZ tuple or ColXYZ class
        :return: CIE-L*uv class """
        tmp = self._parse_input(cXYZ.ColXYZ, *col)
        tmp.append(self)    # append self for observer reference
        self.L, self.u, self.v = XYZtoCIELuv(*tmp)
        return self

    @cB.cancel_on(TypeError)
    def fromCIELCHuv(self, *col):
        """ CIE-L*CH°uv -> CIE-L*uv conversion
        :param col: either CIE-L*CH°uv tuple or ColCIELCHuv class
        :return: CIE-L*uv class """
        self.L, self.u, self.v = CIELCHxxtoCIELxx(*self._parse_input(cCIELCHuv.ColCIELCHuv, *col))
        return self

    # CLASS ADDITIONAL METHODS
    def getHue(self):
        """ get Hue angle (in degrees)
        :param self: ColCIELuv object
        :return: Hue in degrees """
        return CIELxxtoHUE(self.u, self.v)


if __name__ == "__main__":
    col_Luv = ColCIELuv()
    print(col_Luv)
    print(str(col_Luv))
