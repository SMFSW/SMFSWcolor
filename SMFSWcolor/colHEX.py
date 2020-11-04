# -*- coding: utf-8 -*-
"""
colHEX.py
Author: SMFSW
Copyright (c) 2016-2018 SMFSW
Description: HEX color space class
"""

from colorConv import *
from colBase import ColBase as cB
import colRGB as cRGB


class ColHEX(cB):
    """ HTML color class
    Inherits from ColBase """
    # TODO: may inherit cRGB.ColRGB?
    lfields = ['R', 'G', 'B', 'HEX']
    lfields_RGB = ['R', 'G', 'B']
    lfields_HEX = ['HEX']

    def __init__(self, htm='#000000', *args, **kwargs):  # default: Black
        """ Init HTML color """
        cB.__init__(self, *args, **kwargs)
        self.type = 'HEX'   # can be used instead of isinstance on an object

        self.R = self.G = self.B = 0
        self.HEX = ''
        self.HEX_int = lambda: int(self.HEX[1:], 16)    # returns integer base 16 of HEX member

        self.dfields_RGB = dict(zip(range(len(self.lfields_RGB)), self.lfields_RGB))
        self.dfields_HEX = dict(zip(range(len(self.lfields_HEX)), self.lfields_HEX))

        self.refs_RGB = lambda: [vars(self)[var] for var in self.lfields_RGB]
        self.refs_HEX = lambda: [vars(self)[var] for var in self.lfields_HEX]

        self.update(htm)

    def __str__(self):
        """ :return: color string from self """
        return self.HEX

    def __setitem__(self, key, val):
        # TODO: see if this __setitem__ can be reduced
        """ Set key in self """
        try:
            assert key < 4
        except AssertionError:
            return
        else:
            if key == 0:
                self.R = val
                self.HEX = RGBtoHEX(*self.refs_RGB())
            elif key == 1:
                self.G = val
                self.HEX = RGBtoHEX(*self.refs_RGB())
            elif key == 2:
                self.B = val
                self.HEX = RGBtoHEX(*self.refs_RGB())
            else:
                self.HEX = val
                self.R, self.G, self.B = HEXtoRGB(*self.refs_HEX())
            return val

    def update(self, htm):
        """ update class from HTML representation
        :param htm: HTML color (as integer or string)
        :return: none if something went wrong, self otherwise
        """
        if isinstance(htm, str):
            self.HEX = htm
        elif isinstance(htm, int):
            self.HEX = '#' + hex(htm)[2:].zfill(6)
        else:
            return

        self.R, self.G, self.B = HEXtoRGB(self.HEX)
        return self

    # TO COLOR SPACE (DIRECT)
    def toHEX(self):
        """ :return: HEX class from self """
        return self

    def toRGB(self):
        """ :return: RGB class from self """
        return cRGB.ColRGB(*HEXtoRGB(self.HEX))

    # FROM COLOR SPACE (DIRECT)
    def fromHEX(self, *col):
        """ HEX -> HEX conversion
        :param col: either HEX string or ColHEX class
        :return: HEX class """
        if isinstance(col[0], ColHEX):
            field = [vars(col[0])[var] for var in ColHEX.lfields_HEX]
        elif isinstance(col[0], str):
            field = col
        else:
            return

        self.update(field)
        return self

    @cB.cancel_on(TypeError)
    def fromRGB(self, *col):
        """ RGB -> HEX conversion
        :param col: either RGB tuple or ColRGB class
        :return: HEX class """
        self.HEX = RGBtoHEX(*self._parse_input(cRGB.ColRGB, *col))
        self.update(self.HEX)
        return self


if __name__ == "__main__":
    # noinspection PyTypeChecker
    col_hex = ColHEX(0x021050)  # HEX on purpose
    print(col_hex)
    print(str(col_hex))
    print(col_hex.fromRGB(0x20, 0x10, 0x50))

