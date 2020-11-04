# -*- coding: utf-8 -*-
""" colCIEObsLab.py
Author: SMFSW
Copyright (c) 2016-2018 SMFSW
Description: CIE-L*ab color space class
"""

from math import *

from colorConv import *
from colBase import ColBase as cB
from colorFuncs import ColorChecker
import colCIELCHab as cCIELCHab
import colXYZ as cXYZ


class DeltasCIELab(object):
    """ Calculation of color differences (CIE-L*ab color space) """
    def deltaC(self, lab1, lab2='self'):
        if lab2 == 'self':
            lab2 = lab1
            lab1 = self

        if isinstance(lab1, ColCIELab) and isinstance(lab2, ColCIELab):
            return sqrt((lab2.a ** 2) + (lab2.b ** 2)) - sqrt((lab1.a ** 2) + (lab1.b ** 2))
        else:
            print("One of the params for deltaC is not given as a ColCIELab class")

    def deltaH(self, lab1, lab2='self'):
        # TODO: check why sum can be below 0 and raise mathDomainError
        if lab2 == 'self':
            lab2 = lab1
            lab1 = self

        if isinstance(lab1, ColCIELab) and isinstance(lab2, ColCIELab):
            xDE = self.deltaC(lab1, lab2)
            return sqrt(((lab2.a - lab1.a) ** 2) + ((lab2.b - lab1.b) ** 2) - (xDE ** 2))
        else:
            print("One of the params for deltaH is not given as a ColCIELab class")

    def deltaE(self, lab1, lab2='self'):
        if lab2 == 'self':
            lab2 = lab1
            lab1 = self

        if isinstance(lab1, ColCIELab) and isinstance(lab2, ColCIELab):
            return sqrt(((lab1.L - lab2.L) ** 2) + ((lab1.a - lab2.a) ** 2) + ((lab1.b - lab2.b) ** 2))
        else:
            print("One of the params for deltaE is not given as a ColCIELab class")

    def deltaE1994(self, lab1, lab2='self'):
        if lab2 == 'self':
            lab2 = lab1
            lab1 = self

        if isinstance(lab1, ColCIELab) and isinstance(lab2, ColCIELab):
            # Weighting factors depending on the application (1.0 = default)
            wht_L = 1.0
            wht_C = 1.0
            wht_H = 1.0

            xC1 = sqrt((lab1.a ** 2) + (lab1.b ** 2))
            xC2 = sqrt((lab2.a ** 2) + (lab2.b ** 2))
            xDL = lab2.L - lab1.L
            xDC = xC2 - xC1
            xDE = self.deltaE(lab1, lab2)

            if sqrt(xDE) > sqrt(abs(xDL)) + sqrt(abs(xDC)):
                xDH = sqrt((xDE ** 2) - (xDL ** 2) - (xDC ** 2))
            else:
                xDH = 0.0

            xSC = 1.0 + (0.045 * xC1)
            xSH = 1.0 + (0.015 * xC1)
            xDL /= wht_L
            xDC /= wht_C * xSC
            xDH /= wht_H * xSH
            return sqrt((xDL ** 2) + (xDC ** 2) + (xDH ** 2))
        else:
            print("One of the params for deltaE1194 is not given as a ColCIELab class")

    def deltaE2000(self, lab1, lab2='self'):
        if lab2 == 'self':
            lab2 = lab1
            lab1 = self

        if isinstance(lab1, ColCIELab) and isinstance(lab2, ColCIELab):
            # Weighting factors depending on the application (1.0 = default)
            wht_L = 1.0
            wht_C = 1.0
            wht_H = 1.0

            xC1 = sqrt((lab1.a ** 2) + (lab1.b ** 2))
            xC2 = sqrt((lab2.a ** 2) + (lab2.b ** 2))
            xCX = (xC1 + xC2) / 2
            xGX = 0.5 * (1.0 - sqrt((xCX ** 7) / ((xCX ** 7) + (25 ** 7))))
            xNN = (1.0 + xGX) * lab1.a
            xC1 = sqrt((xNN ** 2) + (lab1.b ** 2))
            xH1 = CIELxxtoHUE(xNN, lab1.b)
            xNN = (1.0 + xGX) * lab2.a
            xC2 = sqrt((xNN ** 2) + (lab2.b ** 2))
            xH2 = CIELxxtoHUE(xNN, lab2.b)
            xDL = lab2.L - lab1.L
            xDC = xC2 - xC1
            if xC1 * xC2 == 0.0:
                xDH = 0
            else:
                xNN = round(xH2 - xH1, 12)
                if abs(xNN) <= 180:
                    xDH = xH2 - xH1
                else:
                    xDH = xH2 - xH1
                    if xNN > 180:
                        xDH -= 360
                    else:
                        xDH += 360

            xDH = 2.0 * sqrt(xC1 * xC2) * sin(radians(xDH / 2))
            xLX = (lab1.L + lab2.L) / 2
            xCY = (xC1 + xC2) / 2
            if xC1 * xC2 == 0.0:
                xHX = xH1 + xH2
            else:
                xNN = abs(round(xH1 - xH2, 12))
                if xNN > 180:
                    xHX = xH1 + xH2
                    if xH2 + xH1 < 360:
                        xHX += 360
                    else:
                        xHX -= 360
                else:
                    xHX = xH1 + xH2
            xHX /= 2

            xTX = 0.83 * (cos(radians(xHX - 30)) + 0.24) * (cos(radians(2 * xHX)) + 0.32)\
                       * (cos(radians((3 * xHX) + 6.0)) - 0.20) * (cos(radians((4 * xHX) - 63.0)))
            xPH = 30.0 * exp(-((xHX - 275.0) / 25.0) * ((xHX - 275.0) / 25.0))
            xRC = 2.0 * sqrt((xCY ** 7) / ((xCY ** 7) + (25 ** 7)))
            xSL = 1.0 + ((0.015 * ((xLX - 50) * (xLX - 50))) / sqrt(20 + ((xLX - 50) * (xLX - 50))))
            xSC = 1.045 * xCY
            xSH = 1.015 * xCY * xTX
            xRT = -sin(radians(2 * xPH)) * xRC
            xDL /= (wht_L * xSL)
            xDC /= (wht_C * xSC)
            xDH /= (wht_H * xSH)
            return sqrt((xDL ** 2) + (xDC ** 2) + (xDH ** 2) + (xRT * xDC * xDH))
        else:
            print("One of the params for deltaE2000 is not given as a ColCIELab class")

    def deltaCMC(self, lab1, lab2='self'):
        # TODO: check why sum can be below 0 and raise mathDomainError
        if lab2 == 'self':
            lab2 = lab1
            lab1 = self

        if isinstance(lab1, ColCIELab) and isinstance(lab2, ColCIELab):
            # Weighting factors depending on the application (1.0 = default)
            wht_L = 1.0
            wht_C = 1.0

            xC1 = sqrt((lab1.a ** 2) + (lab1.b ** 2))
            xC2 = sqrt((lab2.a ** 2) + (lab2.b ** 2))
            xff = sqrt((xC1 ** 4) / ((xC1 ** 4) + 1900))
            xH1 = CIELxxtoHUE(lab1.a, lab1.b)

            if xH1 < 164 or xH1 > 345:
                xTT = 0.36 + abs(0.4 * cos(radians(35 + xH1)))
            else:
                xTT = 0.56 + abs(0.2 * cos(radians(168 + xH1)))

            if lab1.L < 16:
                xSL = 0.511
            else:
                xSL = (0.040975 * lab1.L) / (1.0 + (0.01765 * lab1.L))

            xSC = 0.638 + ((0.0638 * xC1) / (1.0 + (0.0131 * xC1)))
            xSH = ((xff * xTT) + 1.0 - xff) * xSC
            xDH = sqrt(((lab2.a - lab1.a) ** 2) + ((lab2.b - lab1.b) ** 2) - ((xC2 - xC1) ** 2))
            xSL = (lab2.L - lab1.L) * xSL / wht_L
            xSC = (xC2 - xC1) * xSC / wht_C
            xSH = xDH / xSH
            return sqrt((xSL ** 2) + (xSC ** 2) + (xSH ** 2))
        else:
            print("One of the params for deltaCMC is not given as a ColCIELab class")


class ColCIELab(cB, DeltasCIELab, ColorChecker):
    """ CIE-L*ab color class
    Inherits from ColBase, DeltasCIELab, ColorChecker """
    lfields = ['L', 'a', 'b']

    def __init__(self, L=0.0, a=0.0, b=0.0, *args, **kwargs):    # default: Black
        """ Init with L*, a, b values """
        cB.__init__(self, *args, **kwargs)
        ColorChecker.__init__(self, *args, **kwargs)
        self.type = 'CIELab'    # can be used instead of isinstance on an object
        self.L, self.a, self.b = L, a, b

    # TO COLOR SPACE (DIRECT)
    def toCIELab(self):
        """ :return: CIE-L*ab class from self """
        return self

    def toXYZ(self):
        """ :return: XYZ class from self """
        tmp = self.refs()
        tmp.append(self)    # append self for observer reference
        return cXYZ.ColXYZ(*CIELabtoXYZ(*tmp))

    def toCIELCHab(self):
        """ :return: CIE-L*CH°ab class from self """
        return cCIELCHab.ColCIELCHab(*CIELxxtoCIELCHxx(*self.refs()))

    # FROM COLOR SPACE (DIRECT)
    @cB.cancel_on(TypeError)
    def fromCIELab(self, *col):
        """ CIE-L*ab -> CIE-L*ab conversion
        :param col: either CIE-L*ab tuple or ColCIELab class
        :return: CIE-L*ab class """
        self.L, self.a, self.b = self._parse_input(ColCIELab, *col)
        return self

    @cB.cancel_on(TypeError)
    def fromXYZ(self, *col):
        """ XYZ -> CIE-L*ab conversion
        :param col: either XYZ tuple or ColXYZ class
        :return: CIE-L*ab class """
        tmp = self._parse_input(cXYZ.ColXYZ, *col)
        tmp.append(self)    # append self for observer reference
        self.L, self.a, self.b = XYZtoCIELab(*tmp)
        return self

    @cB.cancel_on(TypeError)
    def fromCIELCHab(self, *col):
        """ CIE-L*CH°ab -> CIE-L*ab conversion
        :param col: either CIE-L*CH°ab tuple or ColCIELCHab class
        :return: CIE-L*ab class """
        self.L, self.a, self.b = CIELCHxxtoCIELxx(*self._parse_input(cCIELCHab.ColCIELCHab, *col))
        return self

    # CLASS ADDITIONAL METHODS
    def getHue(self):
        """ get Hue angle (in degrees)
        :param self: ColCIELab object
        :return: Hue in degrees """
        return CIELxxtoHUE(self.a, self.b)


if __name__ == "__main__":
    col_Lab = ColCIELab()
    print(col_Lab)
    print(str(col_Lab))
    print(col_Lab.deltaC(ColCIELab(56.5591123536589, 20.6729849296238, 56.1249647776241)))  # R190 G120 B30
    # print(col_Lab.deltaH(ColCIELab(56.5591123536589, 20.6729849296238, 56.1249647776241)))  # R190 G120 B30
    print(col_Lab.deltaE(ColCIELab(56.5591123536589, 20.6729849296238, 56.1249647776241)))  # R190 G120 B30
    print(col_Lab.deltaE1994(ColCIELab(56.5591123536589, 20.6729849296238, 56.1249647776241)))  # R190 G120 B30
    print(col_Lab.deltaE2000(ColCIELab(56.5591123536589, 20.6729849296238, 56.1249647776241)))  # R190 G120 B30
    # print(col_Lab.deltaCMC(ColCIELab(56.5591123536589, 20.6729849296238, 56.1249647776241)))    # R190 G120 B30
