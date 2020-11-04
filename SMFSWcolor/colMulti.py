# -*- coding: utf-8 -*-
"""
colMulti.py
Author: SMFSW
Copyright (c) 2016-2018 SMFSW

"""

from colorConv import *
from colorConvTemperature import TEMPtoYxy

from CIEobs import *        # CIE parameters class

from colRGB import ColRGB
from colRGBW import ColRGBW
from colRGBDim import ColRGBDim
from colHSL import ColHSL
from colHSV import ColHSV
from colHWB import ColHWB
from colXYZ import ColXYZ
from colYxy import ColYxy
from colHunterLab import ColHunterLab
from colCIELab import ColCIELab
from colCIELCHab import ColCIELCHab
from colCIELuv import ColCIELuv
from colCIELCHuv import ColCIELCHuv
from colCMY import ColCMY
from colCMYK import ColCMYK
from colHEX import ColHEX
from colYUV import ColYUV
from colYIQ import ColYIQ
from colYCbCr import ColYCbCr
from colYDbDr import ColYDbDr
from colYCoCg import ColYCoCg
from colYCC import ColYCC

from colNamedColours import ColHTMLrestricted, ColCSS
from colWebSafe import ColWebSafe

from colBlackBody import ColBlackBody
from colRAL import ColRAL
from colPantone import ColPantone
# TODO: find how to use colNamedColours, ColWebSafe, ColRAL & colPantone imports

from refsTools import RefColorSet


class Color(object):
    """ Color class """
    # TODO: reconstruct list at init getting method names and removing _from
    lcolspace_type = ['RGB', 'RGBW', 'RGBDim',
                      'HSL', 'HSV', 'HWB', 'NCS',
                      'CMY', 'CMYK',
                      'HEX',
                      'YUV', 'YIQ', 'YCbCr', 'YDbDr',
                      'YCoCg', 'YCC',
                      'XYZ', 'Yxy', 'RAL',
                      'CIELab', 'CIELCHab', 'CIELuv', 'CIELCHuv', 'HunterLab',
                      'Pantone', 'HTMLrestricted', 'CSS', 'WebSafe',
                      'Ncol', 'Temp', 'BlackBody']
    lGamma = ['1.0', '1.8', '2.2', 'sRGB', 'L*']

    def __init__(self, ctype='RGB', *col, **kwargs):
        """ Init self following type """
        self.RGBSpace = kwargs['rgb_space'] if 'rgb_space' in kwargs and isinstance(kwargs['rgb_space'], str) else 'sRGB'

        self.type = 'Multi'
        # self.args = ctype, col                      # keep former type & args for reference

        self.RGB = ColRGB(**kwargs)                 # RGB instance
        self.RGBW = ColRGBW(**kwargs)               # RGBW instance
        self.RGBDim = ColRGBDim(**kwargs)           # RGBDim instance
        
        self.HSL = ColHSL(**kwargs)                 # HSL instance
        self.HSV = ColHSV(**kwargs)                 # HSV instance
        self.HWB = ColHWB(**kwargs)                 # HWB instance (can represent NCS space)

        self.CMY = ColCMY(**kwargs)                 # CMY instance
        self.CMYK = ColCMYK(**kwargs)               # CMYK instance

        self.HEX = ColHEX(**kwargs)                 # HEX instance

        self.YUV = ColYUV(**kwargs)                 # YUV instance
        self.YIQ = ColYIQ(**kwargs)                 # YIQ instance
        self.YCbCr = ColYCbCr(**kwargs)             # YCbCr instance
        self.YDbDr = ColYDbDr(**kwargs)             # YDbDr instance
        self.YCoCg = ColYCoCg(**kwargs)             # YCoCg instance
        self.YCC = ColYCC(**kwargs)                 # YCC instance

        self.XYZ = ColXYZ(**kwargs)                 # XYZ instance

        self.CIELab = ColCIELab(**kwargs)           # CIE-L*ab instance
        self.CIELCHab = ColCIELCHab(**kwargs)       # CIE-L*CH°ab instance
        self.CIELuv = ColCIELuv(**kwargs)           # CIE-L*uv instance
        self.CIELCHuv = ColCIELCHuv(**kwargs)       # CIE-L*CH°ab instance
        self.HunterLab = ColHunterLab(**kwargs)     # Hunter-L*ab instance

        self.Yxy = ColYxy(**kwargs)                 # Yxy instance
        self.RAL = None                             # reserved for RAL instance (includes Yxy space)
        self.BlackBody = None                       # reserved for BlackBody instance (includes Yxy space)

        self.Pantone = None                         # reserved for Pantone instance (includes RGB space)
        self.HTMLrestricted = None                  # reserved for HTMLrestricted instance (includes HEX space)
        self.CSS = None                             # reserved for CSS instance (includes HEX space)
        self.WebSafe = None                         # reserved for WebSafe instance (includes HEX space)

        # some other params as hue,dim,Ncol can be added in class
        self.Temp = 0
        self.Ncol = ''

        self.WhiteRef = RefColorSet.ref_ColorSet.get(self.RGBSpace)[12]
        self.Gamma = RefColorSet.ref_ColorSet.get(self.RGBSpace)[11]
        self.Adaptation = 'None'

        self.observer = CIEObs(illum=self.WhiteRef)
        # TODO: add a class function to change observer if default observer doesn't fit
        # print("Observer reference: {}, {}".format(self.observer.ref_variant, self.observer.ref_illum))
        # print("XYZ reference: {}, {}, {}".format(self.observer.ref_X, self.observer.ref_Y, self.observer.ref_Z))
        # print("uv reference: {}, {}".format(self.observer.ref_U, self.observer.ref_V))
        # print("")

        self.dcolspace_type = dict(zip(range(len(self.lcolspace_type)), self.lcolspace_type))   # make dict from fields list
        self.refs = lambda: [vars(self)[var] for var in self.lcolspace_type]                    # make list from color space members

        try:
            self._set(ctype, *col, **kwargs)  # init with given params
        except ValueError:
            self._set('RGB', 0, 0, 0, **kwargs)

    def get(self, ctype='RGB'):
        """ Get color following type """
        if ctype in self.lcolspace_type:
            if ctype == 'NCS':          # special case as Natural Color is included in HWB space
                return self.Ncol, self.HWB.W, self.HWB.B

            return vars(self)[ctype]    # return desired space from self

    def set(self, ctype, *col, **kwargs):
        """ Set a new color following type and convert to other different spaces
        :param ctype: color type (string)
        :param col:
        *col: Values for color type
        :param kwargs:
        **rgb_space (str): RGB working space """
        if 'rgb_space' in kwargs and isinstance(kwargs['rgb_space'], str):
            self.__init__(ctype, *col, **kwargs)
        else:
            self._set(ctype, *col, **kwargs)

    def _set(self, ctype, *col, **kwargs):
        """ Internal method to set a new color following type and convert to other different spaces """
        self._rst_isolated_spaces()
        if ctype in self.lcolspace_type:
            method = getattr(self, '_from' + ctype)     # get attribute from reconstructed method name
            method(*col, **kwargs)                      # launch method passing color arguments
        else:
            print("Type given not recognized: {}".format(self.type))

    def _rst_isolated_spaces(self):
        self.RAL = None                     # reserved for RAL instance
        self.BlackBody = None               # reserved for BlackBody instance
        self.Pantone = None                 # reserved for Pantone instance
        self.HTMLrestricted = None          # reserved for HTMLrestricted instance
        self.CSS = None                     # reserved for CSS instance
        self.WebSafe = None                 # reserved for WebSafe instance

    # Internal commmon isolated conversions
    def _toRGBDerivedStandards(self, *args, **kwargs):
        """ update color spaces from RGB space datas to Derived standards spaces
        :return: updated self """
        self.RGBW.fromRGB(self.RGB)
        self.RGBDim.fromRGB(self.RGB)
        self.HSL.fromRGB(self.RGB)
        self.HSV.fromRGB(self.RGB)
        self.HWB.fromRGB(self.RGB)
        self.Ncol = self.HWB.Ncol
        self.HEX.fromRGB(self.RGB)

    def _toCIEStandards(self, *args, **kwargs):
        """ update color spaces from RGB space datas to CIE standards
        :return: updated self """
        self.XYZ.fromRGB(self.RGB)
        self.Temp = self.XYZ.colorTemp
        self.Yxy.fromXYZ(self.XYZ)
        self.CIELab.fromXYZ(self.XYZ)
        self.CIELCHab.fromCIELab(self.CIELab)
        self.CIELuv.fromXYZ(self.XYZ)
        self.CIELCHuv.fromCIELuv(self.CIELuv)
        self.HunterLab.fromXYZ(self.XYZ)

    def _toTVStandards(self, *args, **kwargs):
        """ update color spaces from RGB space datas to TV standards spaces
        :return: updated self """
        self.YUV.fromRGB(self.RGB)
        self.YIQ.fromRGB(self.RGB)
        self.YCbCr.fromRGB(self.RGB)
        self.YDbDr.fromRGB(self.RGB)
        self.YCoCg.fromRGB(self.RGB)
        self.YCC.fromRGB(self.RGB)

    def _toPrintersStandards(self, *args, **kwargs):
        """ update color spaces from RGB space datas to Printers standards spaces
        :return: updated self """
        self.CMY.fromRGB(self.RGB)
        self.CMYK.fromCMY(self.CMY)

    # Conversions
    def _fromRGB(self, *col, **kwargs):
        """ update color spaces from RGB space datas
        :param col: either RGB tuple or ColRGB class
        :return: updated self """
        self.RGB = ColRGB(*col, **kwargs)

        self._toRGBDerivedStandards(self)
        self._toCIEStandards(self)
        self._toTVStandards(self)
        self._toPrintersStandards(self)
        return self

    def _fromRGBW(self, *col, **kwargs):
        """ update color spaces from RGBW space datas
        :param col: either RGBW tuple or ColRGBW class
        :return: updated self """
        self.RGBW = ColRGBW(*col, **kwargs)

        self.RGB.fromRGBW(self.RGBW)
        self.RGBDim.fromRGB(self.RGB)
        self.HSL.fromRGB(self.RGB)
        self.HSV.fromRGB(self.RGB)
        self.HWB.fromRGB(self.RGB)
        self.Ncol = self.HWB.Ncol
        self.HEX.fromRGB(self.RGB)
        self._toCIEStandards(self)
        self._toTVStandards(self)
        self._toPrintersStandards(self)
        return self

    def _fromRGBDim(self, *col, **kwargs):
        """ update color spaces from RGBDim space datas
        :param col: either RGBDim tuple or ColRGBDim class
        :return: updated self """
        self.RGBDim = ColRGBDim(*col, **kwargs)
        self.HSV.fromRGBDim(self.RGBDim)
        self.RGB.fromHSV(self.HSV)

        self.RGBW.fromRGB(self.RGB)
        self.HSL.fromRGB(self.RGB)
        self.HWB.fromRGB(self.RGB)
        self.Ncol = self.HWB.Ncol
        self.HEX.fromRGB(self.RGB)
        self._toCIEStandards(self)
        self._toTVStandards(self)
        self._toPrintersStandards(self)
        return self

    def _fromHSL(self, *col, **kwargs):
        """ update color spaces from HSL space datas
        :param col: either HSL tuple or ColHSL class
        :return: updated self """
        self.HSL = ColHSL(*col, **kwargs)
        self.RGB.fromHSL(self.HSL)

        self.RGBW.fromRGB(self.RGB)
        self.RGBDim.fromRGB(self.RGB)
        self.HSV.fromRGB(self.RGB)
        self.HWB.fromRGB(self.RGB)
        self.Ncol = self.HWB.Ncol
        self.HEX.fromRGB(self.RGB)
        self._toCIEStandards(self)
        self._toTVStandards(self)
        self._toPrintersStandards(self)
        return self

    def _fromHSV(self, *col, **kwargs):
        """ update color spaces from HSV space datas
        :param col: either HSV tuple or ColHSL class
        :return: updated self """
        self.HSV = ColHSV(*col, **kwargs)
        self.RGB.fromHSV(self.RGB)

        self.RGBW.fromRGB(self.RGB)
        self.RGBDim.fromRGB(self.RGB)
        self.HSL.fromRGB(self.RGB)
        self.HWB.fromRGB(self.RGB)
        self.Ncol = self.HWB.Ncol
        self.HEX.fromRGB(self.RGB)
        self._toCIEStandards(self)
        self._toTVStandards(self)
        self._toPrintersStandards(self)
        return self

    def _fromHWB(self, *col, **kwargs):
        """ update color spaces from HWB space datas
        :param col: either HWB tuple or ColHWB class
        :return: updated self """
        self.HWB = ColHWB(*col, **kwargs)

        self.Ncol = HUEtoNCOL(self.HWB.H)
        self.RGB.fromHWB(self.HWB)
        self.RGBW.fromRGB(self.RGB)
        self.RGBDim.fromRGB(self.RGB)
        self.HSL.fromRGB(self.RGB)
        self.HSV.fromRGB(self.RGB)
        self.Ncol = self.HWB.Ncol
        self.HEX.fromRGB(self.RGB)
        self._toCIEStandards(self)
        self._toTVStandards(self)
        self._toPrintersStandards(self)
        return self

    def _fromNCS(self, *col, **kwargs):
        """ update color spaces from NCS space datas
        :param col: either NCS tuple or ColHWB class
        :return: updated self """
        self.HWB.Ncol, self.HWB.W, self.HWB.B = col

        self.Ncol = self.HWB.Ncol
        self.HWB.fromNCS(self.HWB)
        self.RGB.fromHWB(self.HWB)
        self.RGBW.fromRGB(self.RGB)
        self.RGBDim.fromRGB(self.RGB)
        self.HSL.fromRGB(self.RGB)
        self.HSV.fromRGB(self.RGB)
        self.HEX.fromRGB(self.RGB)
        self._toCIEStandards(self)
        self._toTVStandards(self)
        self._toPrintersStandards(self)
        return self

    def _fromHEX(self, *col, **kwargs):
        """ update color spaces from HEX space datas
        :param col: either HEX string or ColHEX class
        :return: updated self """
        self.HEX = ColHEX(*col, **kwargs)
        self.RGB.fromHEX(self.HEX)

        self.RGBW.fromRGB(self.RGB)
        self.RGBDim.fromRGB(self.RGB)
        self.HSL.fromRGB(self.RGB)
        self.HSV.fromRGB(self.RGB)
        self.HWB.fromRGB(self.RGB)
        self.Ncol = self.HWB.Ncol
        self._toCIEStandards(self)
        self._toTVStandards(self)
        self._toPrintersStandards(self)
        return self

    def _fromCMY(self, *col, **kwargs):
        """ update color spaces from CMY space datas
        :param col: either CMY tuple or ColCMY class
        :return: updated self """
        self.CMY = ColCMY(*col, **kwargs)
        self.CMYK.fromCMY(self.CMY)
        self.RGB.fromCMY(self.CMY)

        self._toRGBDerivedStandards(self)
        self._toCIEStandards(self)
        self._toTVStandards(self)
        return self

    def _fromCMYK(self, *col, **kwargs):
        """ update color spaces from CMYK space datas
        :param col: either CMYK tuple or ColCMYK class
        :return: updated self """
        self.CMYK = ColCMYK(*col, **kwargs)
        self.CMY.fromCMYK(self.CMYK)
        self.RGB.fromCMY(self.CMY)

        self._toRGBDerivedStandards(self)
        self._toCIEStandards(self)
        self._toTVStandards(self)
        return self

    def _fromYUV(self, *col, **kwargs):
        """ update color spaces from YUV space datas
        :param col: either YUV tuple or ColYUV class
        :return: updated self """
        self.YUV = ColYUV(*col, **kwargs)
        self.RGB.fromYUV(self.YUV)
        self.YDbDr.fromYUV(self.YUV)

        self.YIQ.fromRGB(self.RGB)
        self.YCbCr.fromRGB(self.RGB)
        self.YCoCg.fromRGB(self.RGB)
        self.YCC.fromRGB(self.RGB)
        self._toRGBDerivedStandards(self)
        self._toCIEStandards(self)
        self._toPrintersStandards(self)
        return self

    def _fromYIQ(self, *col, **kwargs):
        """ update color spaces from YIQ space datas
        :param col: either YIQ tuple or ColYIQ class
        :return: updated self """
        self.YIQ = ColYIQ(*col, **kwargs)
        self.RGB.fromYIQ(self.YIQ)

        self.YUV.fromRGB(self.RGB)
        self.YCbCr.fromRGB(self.RGB)
        self.YDbDr.fromRGB(self.RGB)
        self.YCoCg.fromRGB(self.RGB)
        self.YCC.fromRGB(self.RGB)
        self._toRGBDerivedStandards(self)
        self._toCIEStandards(self)
        self._toPrintersStandards(self)
        return self

    def _fromYCbCr(self, *col, **kwargs):
        """ update color spaces from YCbCr space datas
        :param col: either YCbCr tuple or ColYCbCr class
        :return: updated self """
        self.YCbCr = ColYCbCr(*col, **kwargs)
        self.RGB.fromYCbCr(self.YCbCr)

        self.YUV.fromRGB(self.RGB)
        self.YIQ.fromRGB(self.RGB)
        self.YDbDr.fromRGB(self.RGB)
        self.YCoCg.fromRGB(self.RGB)
        self.YCC.fromRGB(self.RGB)
        self._toRGBDerivedStandards(self)
        self._toCIEStandards(self)
        self._toPrintersStandards(self)
        return self

    def _fromYDbDr(self, *col, **kwargs):
        """ update color spaces from YDbDr space datas
        :param col: either YDbDr tuple or ColYDbDr class
        :return: updated self """
        self.YDbDr = ColYDbDr(*col, **kwargs)
        self.RGB.fromYDbDr(self.YDbDr)
        self.YUV.fromYDbDr(self.YDbDr)

        self.YIQ.fromRGB(self.RGB)
        self.YCbCr.fromRGB(self.RGB)
        self.YCoCg.fromRGB(self.RGB)
        self.YCC.fromRGB(self.RGB)
        self._toRGBDerivedStandards(self)
        self._toCIEStandards(self)
        self._toPrintersStandards(self)
        return self

    def _fromYCoCg(self, *col, **kwargs):
        """ update color spaces from YCoCg space datas
        :param col: either YCoCg tuple or ColYCoCg class
        :return: updated self """
        self.YCoCg = ColYCoCg(*col, **kwargs)
        self.RGB.fromYCoCg(self.YCoCg)

        self.YUV.fromRGB(self.RGB)
        self.YIQ.fromRGB(self.RGB)
        self.YCbCr.fromRGB(self.RGB)
        self.YDbDr.fromRGB(self.RGB)
        self.YCC.fromRGB(self.RGB)
        self._toRGBDerivedStandards(self)
        self._toCIEStandards(self)
        self._toPrintersStandards(self)
        return self

    def _fromYCC(self, *col, **kwargs):
        """ update color spaces from YCC space datas
        :param col: either YCC tuple or ColYCC class
        :return: updated self """
        self.YCC = ColYCC(*col, **kwargs)
        self.RGB.fromYCC(self.YCC)

        self.YUV.fromRGB(self.RGB)
        self.YIQ.fromRGB(self.RGB)
        self.YCbCr.fromRGB(self.RGB)
        self.YDbDr.fromRGB(self.RGB)
        self.YCoCg.fromRGB(self.RGB)
        self._toRGBDerivedStandards(self)
        self._toCIEStandards(self)
        self._toPrintersStandards(self)
        return self

    def _fromXYZ(self, *col, **kwargs):
        """ update color spaces from XYZ space datas
        :param col: either XYZ tuple or ColXYZ class
        :return: updated self """
        self.XYZ = ColXYZ(*col, **kwargs)

        self.Temp = self.XYZ.colorTemp
        self.Yxy.fromXYZ(self.XYZ)
        self.CIELab.fromXYZ(self.XYZ)
        self.CIELCHab.fromCIELab(self.CIELab)
        self.CIELuv.fromXYZ(self.XYZ)
        self.CIELCHuv.fromCIELuv(self.CIELuv)
        self.HunterLab.fromXYZ(self.XYZ)
        self.RGB.fromXYZ(self.XYZ)
        self._toRGBDerivedStandards(self)
        self._toTVStandards(self)
        self._toPrintersStandards(self)
        return self

    def _fromYxy(self, *col, **kwargs):
        """ update color spaces from Yxy space datas
        :param col: either Yxy tuple or ColYxy class
        :return: updated self """
        self.Yxy = ColYxy(*col, **kwargs)
        self.XYZ.fromYxy(self.Yxy)

        self.Temp = self.XYZ.colorTemp
        self.CIELab.fromXYZ(self.XYZ)
        self.CIELCHab.fromCIELab(self.CIELab)
        self.CIELuv.fromXYZ(self.XYZ)
        self.CIELCHuv.fromCIELuv(self.CIELuv)
        self.HunterLab.fromXYZ(self.XYZ)
        self.RGB.fromXYZ(self.XYZ)
        self._toRGBDerivedStandards(self)
        self._toTVStandards(self)
        self._toPrintersStandards(self)
        return self

    def _fromHunterLab(self, *col, **kwargs):
        """ update color spaces from Hunter-L*ab space datas
        :param col: either Hunter-L*ab tuple or ColHunterLab class
        :return: updated self """
        self.HunterLab = ColHunterLab(*col, **kwargs)
        self.XYZ.fromHunterLab(self.HunterLab)

        self.Temp = self.XYZ.colorTemp
        self.Yxy.fromXYZ(self.XYZ)
        self.CIELab.fromXYZ(self.XYZ)
        self.CIELCHab.fromCIELab(self.CIELab)
        self.CIELuv.fromXYZ(self.XYZ)
        self.CIELCHuv.fromCIELuv(self.CIELuv)
        self.RGB.fromXYZ(self.XYZ)
        self._toRGBDerivedStandards(self)
        self._toTVStandards(self)
        self._toPrintersStandards(self)
        return self

    def _fromCIELab(self, *col, **kwargs):
        """ update color spaces from CIE-L*ab space datas
        :param col: either CIE-L*ab tuple or ColCIELab class
        :return: updated self """
        self.CIELab = ColCIELab(*col, **kwargs)
        self.XYZ.fromCIELab(self.CIELab)

        self.Temp = self.XYZ.colorTemp
        self.Yxy.fromXYZ(self.XYZ)
        self.CIELCHab.fromCIELab(self.CIELab)
        self.CIELuv.fromXYZ(self.XYZ)
        self.CIELCHuv.fromCIELuv(self.CIELuv)
        self.HunterLab.fromXYZ(self.XYZ)
        self.RGB.fromXYZ(self.XYZ)
        self._toRGBDerivedStandards(self)
        self._toTVStandards(self)
        self._toPrintersStandards(self)
        return self

    def _fromCIELuv(self, *col, **kwargs):
        """ update color spaces from CIE-L*uv space datas
        :param col: either CIE-L*uv tuple or ColCIELuv class
        :return: updated self """
        self.CIELuv = ColCIELuv(*col, **kwargs)
        self.XYZ.fromCIELuv(self.CIELuv)

        self.Temp = self.XYZ.colorTemp
        self.Yxy.fromXYZ(self.XYZ)
        self.CIELab.fromXYZ(self.XYZ)
        self.CIELCHab.fromCIELab(self.CIELab)
        self.CIELCHuv.fromCIELuv(self.CIELuv)
        self.HunterLab.fromXYZ(self.XYZ)
        self.RGB.fromXYZ(self.XYZ)
        self._toRGBDerivedStandards(self)
        self._toTVStandards(self)
        self._toPrintersStandards(self)
        return self

    def _fromCIELCHab(self, *col, **kwargs):
        """ update color spaces from CIE-L*CH°ab space datas
        :param col: either CIE-L*CH°ab tuple or ColCIELCHab class
        :return: updated self """
        self.CIELCHab = ColCIELCHab(*col, **kwargs)
        self.CIELab.fromCIELCHab(self.CIELCHab)
        self.XYZ.fromCIELab(self.CIELab)

        self.Temp = self.XYZ.colorTemp
        self.Yxy.fromXYZ(self.XYZ)
        self.CIELuv.fromXYZ(self.XYZ)
        self.CIELCHuv.fromCIELuv(self.CIELuv)
        self.HunterLab.fromXYZ(self.XYZ)
        self.RGB.fromXYZ(self.XYZ)
        self._toRGBDerivedStandards(self)
        self._toTVStandards(self)
        self._toPrintersStandards(self)
        return self

    def _fromCIELCHuv(self, *col, **kwargs):
        """ update color spaces from CIE-L*CH°ab space datas
        :param col: either CIE-L*CH°ab tuple or ColCIELCHab class
        :return: updated self """
        self.CIELCHuv = ColCIELCHuv(*col, **kwargs)
        self.CIELuv.fromCIELCHuv(self.CIELCHuv)
        self.XYZ.fromCIELuv(self.CIELuv)

        self.Temp = self.XYZ.colorTemp
        self.Yxy.fromXYZ(self.XYZ)
        self.CIELab.fromXYZ(self.XYZ)
        self.CIELCHab.fromCIELab(self.CIELab)
        self.HunterLab.fromXYZ(self.XYZ)
        self.RGB.fromXYZ(self.XYZ)
        self._toRGBDerivedStandards(self)
        self._toTVStandards(self)
        self._toPrintersStandards(self)
        return self

    # Isolated conversions
    def _fromBlackBody(self, *col, **kwargs):
        """ update color spaces from Black Body temperature datas
        :param col: Black Body temperature in Kelvins
        :return: updated self """
        self.BlackBody = ColBlackBody(*col, **kwargs)
        self._fromYxy(*self.BlackBody.refs())     # refs is inherited from Yxy class and should return Yxy list
        # TODO: update WebSafe from other spaces (if applicable)
        return self

    def _fromTemp(self, *col, **kwargs):
        """ update color spaces from Temperature in kelvins
        :param col: White temperature in Kelvins
        :return: updated self """
        # TODO: handle exception when Temperature is outside range?
        self._fromYxy(*TEMPtoYxy(col[0]))   # Col is usually a Tuple
        return self

    def _fromRAL(self, *col, **kwargs):
        """ update color spaces from HEX space datas
        :param col: either RAL string or ColRAL class
        :return: updated self """
        self.RAL = ColRAL(*col, **kwargs)
        self._fromCIELab(self.RAL)
        # TODO: update RAL from other spaces (if applicable)
        return self

    def _fromPantone(self, *col, **kwargs):
        """ update color spaces from Pantone space datas
        :param col: either Pantone color code string or ColPantone class
        :return: updated self """
        self.Pantone = ColPantone(*col, **kwargs)
        self._fromRGB(*self.Pantone.refs())     # refs is inherited from RGB class and should return RGB list
        # TODO: update Pantone from other spaces (if applicable)
        return self

    def _fromHTMLrestricted(self, *col, **kwargs):
        """ update color spaces from HEX space datas
        :param col: either HTMLrestricted color name string or ColHTMLrestricted class
        :return: updated self """
        self.HTMLrestricted = ColHTMLrestricted(*col, **kwargs)
        self._fromHEX(self.HTMLrestricted.HEX)
        # TODO: update HTMLrestricted from other spaces (if applicable)
        return self

    def _fromCSS(self, *col, **kwargs):
        """ update color spaces from HEX space datas
        :param col: either CSS color name string or ColCSS class
        :return: updated self """
        self.CSS = ColCSS(*col, **kwargs)
        self._fromHEX(self.CSS.HEX)
        # TODO: update CSS from other spaces (if applicable)
        return self

    def _fromWebSafe(self, *col, **kwargs):
        """ update color spaces from HEX space datas
        :param col: either WebSafe string or ColWebSafe class
        :return: updated self """
        self.WebSafe = ColWebSafe(*col, **kwargs)
        self._fromHEX(self.WebSafe.HEX)
        # TODO: update WebSafe from other spaces (if applicable)
        return self

    # Common methods
    def print_all(self):
        """ print all color spaces from class in a human readable form """
        print("RGB\t\t\t{}".format(self.get('RGB')))
        print("RGBW\t\t{}".format(self.get('RGBW')))
        print("RGBDim\t\t{}".format(self.get('RGBDim')))
        print("HSL\t\t\t{}".format(self.get('HSL')))
        print("HSV\t\t\t{}".format(self.get('HSV')))
        print("HWB\t\t\t{} {}".format(self.get('HWB'), self.get('Ncol')))
        print("CMY\t\t\t{}".format(self.get('CMY')))
        print("CMYK\t\t{}".format(self.get('CMYK')))
        print("HEX\t\t\t{}".format(self.get('HEX')))
        print("YUV\t\t\t{}".format(self.get('YUV')))
        print("YIQ\t\t\t{}".format(self.get('YIQ')))
        print("YCbCr\t\t{}".format(self.get('YCbCr')))
        print("YDbDr\t\t{}".format(self.get('YDbDr')))
        print("YCoCg\t\t{}".format(self.get('YCoCg')))
        print("YCC\t\t\t{}".format(self.get('YCC')))
        print("XYZ\t\t\t{} {}K".format(self.get('XYZ'), self.get('Temp')))
        print("Yxy\t\t\t{}".format(self.get('Yxy')))
        print("CIELuv\t\t{}".format(self.get('CIELuv')))
        print("CIELCHuv\t{}".format(self.get('CIELCHuv')))
        print("CIELab\t\t{}".format(self.get('CIELab')))
        print("CIELCHab\t{}".format(self.get('CIELCHab')))
        print("HunterLab\t{}".format(self.get('HunterLab')))
        print("")


if __name__ == "__main__":
    c = Color()
    # c.set('RGB', 10, 150, 20)
    # c.print_all()

    print("6504K temperature conversion:")
    c.set('Temp', 6504)
    c.print_all()

    print("6504K XYZ conversion (taken from XYZ conversion value from previous test):")
    c.set('XYZ', 93.93442544360434, 99.04590353038346, 104.59307451742508)
    c.print_all()

    print("5000K temperature conversion:")
    c.set('Temp', 5000)
    c.print_all()

    print("RGB White conversion:")
    c.set('RGB', 255, 255, 255)
    c.print_all()

    c.set('NCS', 'G6', 4, 41)
    print(c.get('RGB'))
    print(c.get('NCS'))
