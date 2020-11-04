# -*- coding: utf-8 -*-
"""
colHWB.py
Author: SMFSW
Copyright (c) 2016-2018 SMFSW
Description: HWB color space class
"""

from colorConv import *
from colBase import ColBase as cB
from colorFuncs import Harmonies
import colRGB as cRGB


class ColHWB(cB, Harmonies):
    """ HWB color class
    Inherits from ColBase, Harmonies """
    lfields = ['H', 'W', 'B', 'Ncol']
    lfields_HWB = ['H', 'W', 'B']
    lfields_NCS = ['Ncol', 'W', 'B']

    def __init__(self, H=0, W=0, B=100, *args, **kwargs):    # default: Black
        """ Init with H, W, B values """
        cB.__init__(self, *args, **kwargs)
        self.type = 'HWB'   # can be used instead of isinstance on an object

        self.H, self.W, self.B = H, W, B
        self.Ncol = HUEtoNCOL(self.H)

        self.dfields_HWB = dict(zip(range(len(self.lfields_HWB)), self.lfields_HWB))
        self.dfields_NCS = dict(zip(range(len(self.lfields_NCS)), self.lfields_NCS))

        self.refs_HWB = lambda: [vars(self)[var] for var in self.lfields_HWB]
        self.refs_NCS = lambda: [vars(self)[var] for var in self.lfields_NCS]

    def __str__(self):
        """ :return: string representing H, W, B values of tuple from self """
        return "({}, {}, {})".format(self.H, self.W, self.B)

    def __setitem__(self, key, val):
        """ Set key in self """
        try:
            assert key < 4
        except AssertionError:
            return
        else:
            if key == 0:
                self.H = val
                self.Ncol = HUEtoNCOL(self.H)
            elif key == 1:
                self.W = val
            elif key == 2:
                self.B = val
            else:
                self.Ncol = val
                self.fromNCS(*self.refs_NCS())
            return val

    # TO COLOR SPACE (DIRECT)
    def toHWB(self):
        """ :return: HWB class from self """
        return self

    def toNCS(self):
        """ :return: NCS class from self """
        return self

    def toRGB(self):
        """ :return: RGB class from self """
        return cRGB.ColRGB(*HWBtoRGB(*self.refs_HWB()))

    # FROM COLOR SPACE (DIRECT)
    def fromHWB(self, *col):
        """ HWB -> HWB conversion
        :param col: either HWB tuple or ColHWB class
        :return: HWB class """
        if isinstance(col[0], ColHWB):
            self.H, self.W, self.B = [vars(col[0])[var] for var in ColHWB.lfields_HWB]
            self.Ncol = HUEtoNCOL(self.H)
            return self
        elif len(col) == 3:
            self.H, self.W, self.B = col
            self.Ncol = HUEtoNCOL(self.H)
            return self
        else:
            return

    @cB.cancel_on(TypeError)
    def fromRGB(self, *col):
        """ RGB -> HWB conversion
        :param col: either RGB tuple or ColRGB class
        :return: HWB class """
        self.H, self.W, self.B = RGBtoHWB(*self._parse_input(cRGB.ColRGB, *col))
        self.Ncol = HUEtoNCOL(self.H)
        return self

    def fromNCS(self, *col):
        """ NCS -> HWB conversion
        :param col: either NCS tuple or ColHWB class
        :return: HWB class """
        if isinstance(col[0], ColHWB):
            self.Ncol, self.W, self.B = [vars(col[0])[var] for var in ColHWB.lfields_NCS]
            self.H = NCStoHWB(self.Ncol, self.W, self.B)[0]
            return self
        elif len(col) == 3:
            self.Ncol, self.W, self.B = col
            self.H = NCStoHWB(self.Ncol, self.W, self.B)[0]
            return self
        else:
            return


if __name__ == "__main__":
    col_HWB = ColHWB()
    col_HWB.fromRGB(10, 90, 20)
    print(col_HWB)
    print(str(col_HWB))

    col_NCS = col_HWB.toNCS()
    print(col_NCS)
    print(col_HWB.fromNCS(col_NCS))
    print(col_HWB.toRGB())

    print(col_HWB.complement())     # from Harmonies class
    print(col_HWB.split_complement())
    print(col_HWB.triadic())
    print(col_HWB.analogous())
