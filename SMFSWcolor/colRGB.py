# -*- coding: utf-8 -*-
"""
colRGB.py
Author: SMFSW
Copyright (c) 2016-2018 SMFSW
Description: RGB color space class
"""

from colorConv import *
from colorConvTemperature import TEMPtoRGB
from colBase import ColBase as cB
import colRGBW as cRGBW
import colRGBDim as cRGBDim
import colHEX as cHEX
import colHSL as cHSL
import colHSV as cHSV
import colHWB as cHWB
import colCMY as cCMY
import colYCoCg as cYCoCg
import colYCbCr as cYCbCr
import colYDbDr as cYDbDr
import colYIQ as cYIQ
import colYUV as cYUV
import colYCC as cYCC
import colXYZ as cXYZ


class ColRGB(cB):
    """ RGB color class
    Inherits from ColBase """
    lfields = ['R', 'G', 'B']

    def __init__(self, R=0, G=0, B=0, *args, **kwargs):  # default: Black
        """ Init self with R (Red), G (Green), B (Blue) """
        cB.__init__(self, *args, **kwargs)
        self.type = 'RGB'   # can be used instead of isinstance on an object

        if R in range(256) and G in range(256) and B in range(256):
            self.R, self.G, self.B = R, G, B
        else:
            self.R = self.G = self.B = 0

    def __hex__(self):
        """ :return: hex representing R, G, B values of tuple from self """
        r = hex(self.R)[2:].zfill(2)
        g = hex(self.G)[2:].zfill(2)
        b = hex(self.B)[2:].zfill(2)
        return "#{}{}{}".format(r, g, b)

    # TO COLOR SPACE (DIRECT)
    def toRGB(self):
        """ :return: RGB class from self """
        return self

    def toRGBW(self):
        """ :return: RGBW class from self """
        return cRGBW.ColRGBW(*RGBtoRGBW(*self.refs()))

    def toRGBDim(self):
        """ :return: RGBDim class from self """
        return cRGBDim.ColRGBDim(*RGBtoRGBDim(*self.refs()))

    def toHEX(self):
        """ :return: HEX class from self """
        return cHEX.ColHEX(*RGBtoHEX(*self.refs()))

    def toHSL(self):
        """ :return: HSL class from self """
        return cHSL.ColHSL(*RGBtoHSL(*self.refs()))

    def toHSV(self):
        """ :return: HSV class from self """
        return cHSV.ColHSV(*RGBtoHSV(*self.refs()))

    def toHWB(self):
        """ :return: HWB class from self """
        return cHWB.ColHWB(*RGBtoHWB(*self.refs()))

    def toNCS(self):
        """ :return: NCS class from self """
        return cHWB.ColHWB(*RGBtoHWB(*self.refs()))

    def toCMY(self):
        """ :return: CMY class from self """
        return cCMY.ColCMY(*RGBtoCMY(*self.refs()))

    def toYCoCg(self):
        """ :return: YCoCg class from self """
        return cYCoCg.ColYCoCg(*RGBtoYCoCg(*self.refs()))

    def toYCbCr(self):
        """ :return: YCbCr class from self """
        return cYCbCr.ColYCbCr(*RGBtoYCbCr(*self.refs()))

    def toYDbDr(self):
        """ :return: YDbDr class from self """
        return cYDbDr.ColYDbDr(*RGBtoYDbDr(*self.refs()))

    def toYIQ(self):
        """ :return: YIQ class from self """
        return cYIQ.ColYIQ(*RGBtoYIQ(*self.refs()))

    def toYUV(self):
        """ :return: YUV class from self """
        return cYUV.ColYUV(*RGBtoYUV(*self.refs()))

    def toYCC(self):
        """ :return: YCC class from self """
        return cYCC.ColYCC(*RGBtoYCC(*self.refs()))

    def toXYZ(self):
        """ :return: XYZ class from self """
        return cXYZ.ColXYZ(*RGBtoXYZ(*self.refs(), rgb_space=self.RGBSpace))

    # FROM COLOR SPACE (DIRECT)
    @cB.cancel_on(TypeError)
    def fromRGB(self, *col):
        """ RGB -> RGB conversion
        :param col: either RGB tuple or ColRGB class
        :return: RGB class """
        self.R, self.G, self.B = self._parse_input(ColRGB, *col)
        return self

    @cB.cancel_on(TypeError)
    def fromRGBW(self, *col):
        """ RGBW -> RGB conversion
        :param col: either RGBW tuple or ColRGBW class
        :return: RGB class """
        self.R, self.G, self.B = RGBWtoRGB(*self._parse_input(cRGBW.ColRGBW, *col))
        return self

    @cB.cancel_on(TypeError)
    def fromRGBDim(self, *col):
        """ RGBDim -> RGB conversion
        :param col: either RGBDim tuple or ColRGBDim class
        :return: RGB class """
        self.R, self.G, self.B = RGBDimtoRGB(*self._parse_input(cRGBDim.ColRGBDim, *col))
        return self

    @cB.cancel_on(TypeError)
    def fromHSL(self, *col):
        """ HSL -> RGB conversion
        :param col: either HSL tuple or ColHSL class
        :return: RGB class """
        self.R, self.G, self.B = HSLtoRGB(*self._parse_input(cHSL.ColHSL, *col))
        return self

    @cB.cancel_on(TypeError)
    def fromHSV(self, *col):
        """ HSV -> RGB conversion
        :param col: either HSV tuple or ColHSL class
        :return: RGB class """
        self.R, self.G, self.B = HSVtoRGB(*self._parse_input(cHSV.ColHSV, *col))
        return self

    def fromHWB(self, *col):
        """ HWB -> RGB conversion
        :param col: either HWB tuple or ColHWB class
        :return: RGB class """
        if isinstance(col[0], cHWB.ColHWB):
            fields = [vars(col[0])[var] for var in cHWB.ColHWB.lfields_HWB]
        elif len(col) == 3:
            fields = col
        else:
            return

        self.R, self.G, self.B = HWBtoRGB(*fields)
        return self

    @cB.cancel_on(TypeError)
    def fromCMY(self, *col):
        """ CMY -> RGB conversion
        :param col: either CMY tuple or ColCMY class
        :return: RGB class """
        self.R, self.G, self.B = CMYtoRGB(*self._parse_input(cCMY.ColCMY, *col))
        return self

    @cB.cancel_on(TypeError)
    def fromYCoCg(self, *col):
        """ YCoCg -> RGB conversion
        :param col: either YCoCg tuple or ColYCoCg class
        :return: RGB class """
        self.R, self.G, self.B = YCoCgtoRGB(*self._parse_input(cYCoCg.ColYCoCg, *col))
        return self

    @cB.cancel_on(TypeError)
    def fromYCbCr(self, *col):
        """ YCbCr -> RGB conversion
        :param col: either YCbCr tuple or ColYCbCr class
        :return: RGB class """
        self.R, self.G, self.B = YCbCrtoRGB(*self._parse_input(cYCbCr.ColYCbCr, *col))
        return self

    @cB.cancel_on(TypeError)
    def fromYDbDr(self, *col):
        """ YDbDr -> RGB conversion
        :param col: either YDbDr tuple or ColYDbDr class
        :return: RGB class """
        self.R, self.G, self.B = YDbDrtoRGB(*self._parse_input(cYDbDr.ColYDbDr, *col))
        return self

    @cB.cancel_on(TypeError)
    def fromYIQ(self, *col):
        """ YIQ -> RGB conversion
        :param col: either YIQ tuple or ColYIQ class
        :return: RGB class """
        self.R, self.G, self.B = YIQtoRGB(*self._parse_input(cYIQ.ColYIQ, *col))
        return self

    @cB.cancel_on(TypeError)
    def fromYUV(self, *col):
        """ YUV -> RGB conversion
        :param col: either YUV tuple or ColYUV class
        :return: RGB class """
        self.R, self.G, self.B = YUVtoRGB(*self._parse_input(cYUV.ColYUV, *col))
        return self

    @cB.cancel_on(TypeError)
    def fromYCC(self, *col):
        """ YCC -> RGB conversion
        :param col: either YCC tuple or ColYCC class
        :return: RGB class """
        self.R, self.G, self.B = YCCtoRGB(*self._parse_input(cYCC.ColYCC, *col))
        return self

    def fromHEX(self, *col):
        """ HEX -> RGB conversion
        :param col: either HEX string or ColHEX class
        :return: RGB class """
        if isinstance(col[0], cHEX.ColHEX):
            field = col[0].HEX
        elif isinstance(col[0], str):
            field = col[0]
        else:
            return

        self.R, self.G, self.B = HEXtoRGB(field)
        return self

    @cB.cancel_on(TypeError)
    def fromXYZ(self, *col):
        """ XYZ -> RGB conversion
        :param col: either XYZ tuple or ColXYZ class
        :return: RGB class """
        self.R, self.G, self.B = XYZtoRGB(*self._parse_input(cXYZ.ColXYZ, *col), rgb_space=self.RGBSpace)
        return self

    def fromTemp(self, Temp):
        """ Temperature -> RGB conversion
        :param Temp: White temperature in Kelvins
        :return: RGB class """
        if isinstance(Temp, int):
            self.R, self.G, self.B = TEMPtoRGB(Temp)
            return self
        else:
            return

    # FROM COLOR SPACE (INDIRECT)
    def fromNCS(self, *col):
        """ NCS -> RGB conversion
        :param col: either NCS tuple or ColHWB class
        :return: RGB class """
        if isinstance(col[0], cHWB.ColHWB):
            fields = [vars(col[0])[var] for var in cHWB.ColHWB.lfields_NCS]
        elif len(col) == 3:
            fields = col
        else:
            return

        self.R, self.G, self.B = HWBtoRGB(*NCStoHWB(*fields))
        return self


if __name__ == "__main__":
    col_RGB = ColRGB(10, 150, 20, RGBspace='sRGB', var='CIE1964', illum='F11')
    print(col_RGB)
    print(str(col_RGB))
    print(col_RGB.toRGBW())
    print(col_RGB.fromHEX('#505050'))

    col_RGB2 = ColRGB()
    print(str(col_RGB2.fromRGBDim(10, 150, 20, 25.0)))
    print(str(col_RGB2.fromRGBDim(10, 150, 20, 125.0)))  # test over 100% brightness

    col_RGBDim = cRGBDim.ColRGBDim(10, 150, 20, 125.0)
    print(str(col_RGB2.fromRGBDim(col_RGBDim)))

    print(str(col_RGB.fromRGB(col_RGB2)))
    print(str(col_RGB.fromRGB(50, 20, 10)))
    print(repr(col_RGB))

    # test ColBase __setitem__ and __getitem__
    col_RGB[0] = 115
    col_RGB['B'] = 69
    print(col_RGB[0], col_RGB['G'], col_RGB['B'])
