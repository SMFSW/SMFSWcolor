# -*- coding:utf-8 -*-
"""
__init__.py (SMFSWcolor)
Author: SMFSW
Copyright (c) 2016-2018 SMFSW

SMFSWcolor package init
"""

# __all__ = ["colorConv", "colorConvGamma", "colorConvTemperature",
#            "colorFuncs", "colorScenarios",
#            "refsTools", "CIEObs",
#            "colRGB", "colRGBW", "colRGBDim",
#            "colHSL", "colHSV", "colHWB",
#            "colXYZ", "colYxy", "colBlackBody",
#            "colHunterLab", "colCIELab",
#            "colCIELab", "colCIELCHab",
#            "colCIELuv", "colCIELCHuv",
#            "colCMY", "colCMYK",
#            "colHEX", "colNamedColours", "colWebSafe",
#            "colYUV", "colYCbCr",
#            "colRAL", "colPantone",
#            "colMulti"]

from .colorConv import *                # methods for color conversion
from .colorConvGamma import *           # methods for color gamma handling
from .colorConvTemperature import *     # methods for color temperature conversion
from .colorFuncs import *
from .colorScenarios import *

from .refsTools import *

from .CIEobs import *        # CIE observer class

from .colRGB import *
from .colRGBW import *
from .colRGBDim import *
from .colHSL import *
from .colHSV import *
from .colHWB import *
from .colXYZ import *
from .colYxy import *
from .colHunterLab import *
from .colCIELab import *
from .colCIELuv import *
from .colCIELCHab import *
from .colCIELCHuv import *
from .colCMY import *
from .colCMYK import *
from .colHEX import *
from .colYUV import *
from .colYCbCr import *
from .colNamedColours import *
from .colWebSafe import *
from .colBlackBody import *
from .colRAL import *
from .colPantone import *
from .colMulti import *
