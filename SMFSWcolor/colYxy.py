# -*- coding: utf-8 -*-
"""
colYxy.py
Author: SMFSW
Copyright (c) 2016-2025 SMFSW
Description: Yxy color space class
"""

from colorConv import *
from colorConvTemperature import getTempxy
from colBase import ColBase as cB
from colorFuncs import ColorChecker
import colXYZ as cXYZ


class ColYxy(cB, ColorChecker):
    """ Yxy color class
    Inherits from ColBase, ColorChecker """
    lfields = ['Y', 'x', 'y']

    def __init__(self, Y=0.0, x=0.0, y=0.0, *args, **kwargs):    # default: Black
        """ Init self with Y, x, y """
        cB.__init__(self, *args, **kwargs)
        ColorChecker.__init__(self, *args, **kwargs)
        self.type = 'Yxy'   # can be used instead of isinstance on an object
        self.Y, self.x, self.y = Y, x, y

    # CLASS PROPERTIES (IMPLEMENTED AS METHODS)
    @property
    def colorTemp(self):
        """ get color temperature in Kelvin (from XYZ values)
        :param self: ColYxy object
        :return: Temperature in Kelvin """
        return getTempxy(self.x, self.y)

    @property
    def colorLum(self):
        """ get luminance from Y value
        :param self: ColYxy object
        :return: Luminance in cd/m2 """
        return self.Y

    # TO COLOR SPACE (DIRECT)
    def toYxy(self):
        """ :return: Yxy class from self """
        return self

    def toXYZ(self):
        """ :return: XYZ class from self """
        return cXYZ.ColXYZ(*YxytoXYZ(*self.refs()))

    # FROM COLOR SPACE (DIRECT)
    @cB.cancel_on(TypeError)
    def fromYxy(self, *col):
        """ Yxy -> Yxy conversion
        :param col: either Yxy tuple or ColYxy class
        :return: Yxy class """
        self.Y, self.x, self.y = self._parse_input(ColYxy, *col)
        return self

    @cB.cancel_on(TypeError)
    def fromXYZ(self, *col):
        """ XYZ -> Yxy conversion
        :param col: either XYZ tuple or ColXYZ class
        :return: Yxy class """
        self.Y, self.x, self.y = XYZtoYxy(*self._parse_input(cXYZ.ColXYZ, *col))
        return self


if __name__ == "__main__":
    col_Yxy = ColYxy(0.1, 0.415, 0.2)
    print(col_Yxy)
    print(str(col_Yxy))
    
    print(col_Yxy.colorTemp)
    print(col_Yxy.colorLum)

