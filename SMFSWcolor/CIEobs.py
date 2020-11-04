# -*- coding: utf-8 -*-
"""
CIEobs.py
Author: SMFSW
Copyright (c) 2016-2018 SMFSW
Description: CIE observer reference & class
"""

from refsTools import RefColorSet


class RefObserver_xy(object):
    """ Observer reference dicts & methods
    https://en.wikipedia.org/wiki/Standard_illuminant """

    lfields_variant = ['CIE1931', 'CIE1964']
    lfields_illuminant = ['A', 'B', 'C', 'D50', 'D55', 'D65', 'D75', 'E',
                          'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F1', 'F12']
    dfields_variant = dict(zip(range(len(lfields_variant)), lfields_variant))
    dfields_illuminant = dict(zip(range(len(lfields_illuminant)), lfields_illuminant))

    # id: (Temperature (K), Description)
    infosIlluminant = {'A'  : (2856, "Incandescent / Tungsten"),
                       'B'  : (4874, "Direct sun at noon (Obsolete)"),
                       'C'  : (6774, "Average / North sky daylight (Obsolete)"),
                       'D50': (5003, "Horizon Light. ICC profile PCS"),
                       'D55': (5503, "Mid-morning / Mid-afternoon Daylight"),
                       'D65': (6504, "Noon Daylight: Television, sRGB color space"),
                       'D75': (7504, "North sky Daylight"),
                       'E'  : (5454, "Equal energy"),
                       'F1' : (6430, "Daylight Fluorescent"),
                       'F2' : (4230, "Cool White Fluorescent"),
                       'F3' : (3450, "White Fluorescent"),
                       'F4' : (2940, "Warm White Fluorescent"),
                       'F5' : (6350, "Daylight Fluorescent"),
                       'F6' : (4150, "Lite White Fluorescent"),
                       'F7' : (6500, "D65 simulator, Daylight simulator"),
                       'F8' : (5000, "D50 simulator, Sylvania F40 Design 50"),
                       'F9' : (4150, "Cool White Deluxe Fluorescent"),
                       'F10': (5000, "Philips TL85, Ultralume 50"),
                       'F11': (4000, "Philips TL84, Ultralume 40"),
                       'F12': (3000, "Philips TL83, Ultralume 30"),
                       # TODO: add known others
                       }

    # reference for Observer 2° (CIE1931)
    refObsCIE1931 = {
        'A'  : (0.44757, 0.40745),
        'B'  : (0.34842, 0.35161),
        'C'  : (0.31006, 0.31616),
        'D50': (0.34567, 0.35850),
        'D55': (0.33242, 0.34743),
        'D65': (0.31271, 0.32902),
        'D75': (0.29902, 0.31485),
        'E'  : (1.0 / 3.0, 1.0 / 3.0),
        'F1' : (0.31310, 0.33727),
        'F2' : (0.37208, 0.37529),
        'F3' : (0.40910, 0.39430),
        'F4' : (0.44018, 0.40329),
        'F5' : (0.31379, 0.34531),
        'F6' : (0.37790, 0.38835),
        'F7' : (0.31292, 0.32933),
        'F8' : (0.34588, 0.35875),
        'F9' : (0.37417, 0.37281),
        'F10': (0.34609, 0.35986),
        'F11': (0.38052, 0.37713),
        'F12': (0.43695, 0.40441),
    }

    # reference for Observer 10° (CIE1964)
    refObsCIE1964 = {
        'A'  : (0.45117, 0.40594),
        'B'  : (0.34980, 0.35270),
        'C'  : (0.31039, 0.31905),
        'D50': (0.34773, 0.35952),
        'D55': (0.33411, 0.34877),
        'D65': (0.31382, 0.33100),
        'D75': (0.29968, 0.31740),
        'E'  : (1.0 / 3.0, 1.0 / 3.0),
        'F1' : (0.31811, 0.33559),
        'F2' : (0.37925, 0.36733),
        'F3' : (0.41761, 0.38324),
        'F4' : (0.44920, 0.39074),
        'F5' : (0.31975, 0.34246),
        'F6' : (0.38660, 0.37847),
        'F7' : (0.31569, 0.32960),
        'F8' : (0.34902, 0.35939),
        'F9' : (0.37829, 0.37045),
        'F10': (0.35090, 0.35444),
        'F11': (0.38541, 0.37123),
        'F12': (0.44256, 0.39717),
    }

    @classmethod
    def get_cie2(cls, srch):
        """ :return: coefs tuple from srch in refObsCIE1931 (observer 2°) dict """
        return cls.refObsCIE1931.get(srch)

    @classmethod
    def get_cie10(cls, srch):
        """ :return: coefs tuple from srch in refObsCIE1964 (observer 10°) dict """
        return cls.refObsCIE1964.get(srch)


class RefObserver_XYZ(object):
    """ Observer reference dicts & methods """
    lfields_variant = ['CIE1931', 'CIE1964']
    lfields_illuminant = ['A', 'B', 'C', 'D50', 'D55', 'D65', 'D75', 'E', 'F2', 'F7', 'F8', 'F11']
    dfields_variant = dict(zip(range(len(lfields_variant)), lfields_variant))
    dfields_illuminant = dict(zip(range(len(lfields_illuminant)), lfields_illuminant))

    # id: (Temperature (K), Description)
    infosIlluminant = {'A'  : (2856, "Incandescent Tungsten"),
                       'B'  : (4871, "Deprecated"),
                       'C'  : (6769, "1931 Daylight north sky (NTSC)"),
                       'D50': (5000, "Warm Daylight or Flash (-UV)"),
                       'D55': (5502, "Noon Summer Daylight"),
                       'D65': (6503, "Cool Summer Daylight (+UV)"),
                       'D75': (7503, "Summer Shade"),
                       'E'  : (5454, "CIE Equal energy light source"),
                       'F2' : (4200, "Cool White Fluorescent"),
                       'F7' : (6500, "Daylight Fluorescent"),
                       'F8' : (5000, "Sylvania D50 Fluorescent F8"),
                       'F11': (7503, "TL84 Sp41 Ultralume 40 Fluorescent"),
                       # TODO: add known others
                       }

    # reference for Observer 2° (CIE1931)
    refObsCIE1931 = {
        'A'  : (109.850, 100.0, 35.585),    # Incancompris entrescent
        'B'  : (109.828, 100.0, 35.547),
        'C'  : (98.074, 100.0, 118.232),
        'D50': (96.422, 100.0, 82.521),
        'D55': (95.682, 100.0, 92.149),
        'D65': (95.047, 100.0, 108.883),    # Daylight
        'D75': (94.972, 100.0, 122.638),
        'E'  : (100.0, 100.0, 100.0),
        'F2' : (99.187, 100.0, 67.395),     # Fluorescent
        'F7' : (95.044, 100.0, 108.755),
        'F8' : (96.431, 100.0, 82.432),
        'F11': (100.966, 100.0, 64.370),
    }

    # reference for Observer 10° (CIE1964)
    refObsCIE1964 = {
        'A'  : (111.144, 100.0, 35.200),     # Incancompris entrescent
        # 'B'  : (0.00000, 100.0, 0.00000),
        'C'  : (97.285, 100.0, 116.145),
        'D50': (96.720, 100.0, 81.427),
        'D55': (95.799, 100.0, 90.926),
        'D65': (94.811, 100.0, 107.304),     # Daylight
        'D75': (94.416, 100.0, 120.641),
        'E'  : (100.0, 100.0, 100.0),
        'F2' : (103.280, 100.0, 69.026),     # Fluorescent
        'F7' : (95.792, 100.0, 107.687),
        # 'F8' : (0.00000, 100.0, 0.00000),
        'F11': (103.866, 100.0, 65.627),
    }

    @classmethod
    def get_cie2(cls, srch):
        """ :return: coefs tuple from srch in refObsCIE1931 (observer 2°) dict """
        return cls.refObsCIE1931.get(srch)

    @classmethod
    def get_cie10(cls, srch):
        """ :return: coefs tuple from srch in refObsCIE1964 (observer 10°) dict """
        return cls.refObsCIE1964.get(srch)


class CIEObs(object):
    """ CIE Observer class """
    def __init__(self, *args, **kwargs):
        """ Init with variant & illumination values
        :param kwargs:
        **variant (str): CIE reference used
        **rgb_space (str): RGB working space (provided by rgb_space or illuminant)
        **illuminant (str): Illuminant (provided by rgb_space or illuminant) """
        self.ref_variant = kwargs['variant'] if 'variant' in kwargs and isinstance(kwargs['variant'], str) \
            else 'CIE1931'    # defaults to 2° observer

        if 'illum' in kwargs and isinstance(kwargs['illum'], str):
            self.ref_illum = kwargs['illum']
        elif 'rgb_space' in kwargs and isinstance(kwargs['rgb_space'], str):
            self.ref_illum = RefColorSet.ref_ColorSet.get(kwargs['rgb_space'])[12]
        else:
            self.ref_illum = 'D65'  # D65 daylight

        self.ref_X, self.ref_Y, self.ref_Z = 0.0, 0.0, 0.0
        self.set_xyz_ref(self.ref_variant, self.ref_illum)

        self.ref_U, self.ref_V = 0.0, 0.0
        self.set_uv_ref()

    def get_info_illum(self, srch, info):
        """ :return: color temperature from srch in infosIlluminant """
        if info > 1:
            return None
        return RefObserver_XYZ.infosIlluminant.get(srch)[info]

    def set_xyz_ref(self, variant, illum):
        """ Compute X, Y, Z references for XYZ conversions
        :param variant: variant (from variant list)
        :param illum: illuminant (from illuminant list) """
        self.ref_X, self.ref_Y, self.ref_Z = {'CIE1931': RefObserver_XYZ.get_cie2,
                                              'CIE1964': RefObserver_XYZ.get_cie10}[variant](illum)

    def set_uv_ref(self):
        """ Compute u, v references for L*uv conversions """
        tmp_ref_X, tmp_ref_Y, tmp_ref_Z = self.ref_X / 100.0, self.ref_Y / 100.0, self.ref_Z / 100.0
        denom = (tmp_ref_X + (15 * tmp_ref_Y) + (3 * tmp_ref_Z))
        self.ref_U = (4 * tmp_ref_X) / denom
        self.ref_V = (9 * tmp_ref_Y) / denom
        del tmp_ref_X, tmp_ref_Y, tmp_ref_Z


if __name__ == "__main__":
    Obs = CIEObs('CIE1964', 'A')

    # for i, obs in enumerate(Obs.illuminant):
    # print("illuminant {} is: {}".format(i, obs))

    print("Observer reference: {} ({} -> {} ({}K))".format(Obs.ref_variant, Obs.ref_illum,
                                                           Obs.get_info_illum(Obs.ref_illum, 1), Obs.get_info_illum(Obs.ref_illum, 0)))
    print("XYZ reference: {}, {}, {}".format(Obs.ref_X, Obs.ref_Y, Obs.ref_Z))
    print("uv reference: {}, {}".format(Obs.ref_U, Obs.ref_V))
