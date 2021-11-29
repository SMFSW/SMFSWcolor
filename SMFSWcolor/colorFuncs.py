# -*- coding:utf-8 -*-
"""
colorFuncs.py
Author: SMFSW
Copyright (c) 2016-2021 SMFSW
Description: Low level transformations, manipulations
"""

from math import sqrt

import colorConv as cCV
from CIEobs import CIEObs as rObs


# noinspection PyMethodParameters
# noinspection PyTypeChecker
# noinspection PyArgumentList
class Harmonies(object):
    """ Common color harmonies calculation & check class
    note: only for classes handling Hue parameter"""
    # TODO: check why isinstance(self, (as)ColXXX) doesn't work

    def is_type(pattern):
        """ Check color type & prepare variables for Harmonies treatment
        :param pattern: pattern or list to search for 
        :return: decorated function """
        from functools import wraps
        from re import search

        def decor(fct):
            """ decorator
            :param fct: function to be wrapped
            :return: wrapper """
            @wraps(fct)
            def wrapper(self):
                """ wrapper function
                :param self: object instance
                :return: wrapped function """
                try:
                    for i in pattern:
                        if search(i, (self.type or '')):    # TODO: check if or '' should be removed
                            refs = getattr(self, 'refs')
                            return fct(self, self.type, refs())
                    raise TypeError('Type not directly compatible with Harmonies. (Convert to a HUE based color space first)')
                except TypeError:
                    raise
            return wrapper
        return decor

    @is_type(['HSV', 'HSL', 'HWB', 'CIELCHab', 'CIELCHuv'])
    def complement(self, t, col):
        """ Complement (hue change 180°)
        This is the opposite color on the wheel
        :param t: color type (from decorator)
        :param col: color as a list of values (from decorator)
        :return: complemented color tuple (in original color space) """
        if t in ['HSV', 'HSL']:
            col[0] = (col[0] + 0.5) % 1.0
        elif t == 'HWB':
            col[0] = (col[0] + 180) % 360
            col[3] = cCV.HUEtoNCOL(col[0])
        elif t == 'CIELCHab' or t == 'CIELCHuv':
            col[2] = (col[2] + 180) % 360

        return tuple(col)

    @is_type(['HSV', 'HSL', 'HWB', 'CIELCHab', 'CIELCHuv'])
    def split_complement(self, t, col):
        """ Split complements (hue change +/-150°)
        This color scheme combines the two colors on either side of a color's complement
        :param t: color type (from decorator)
        :param col: color as a list of values (from decorator)
        :return: tuple of split complements color tuples (in original color space) """
        return self.symmetrical_hue_calc(t, col, 150)

    @is_type(['HSV', 'HSL', 'HWB', 'CIELCHab', 'CIELCHuv'])
    def triadic(self, t, col):
        """ Triadic (hue change +/-120°)
        This is the typical configuration of 3 colors equally spaced from each other on the wheel
        :param t: color type (from decorator)
        :param col: color as a list of values (from decorator)
        :return: tuple of triadic color tuples (in original color space) """
        return self.symmetrical_hue_calc(t, col, 120)

    @is_type(['HSV', 'HSL', 'HWB', 'CIELCHab', 'CIELCHuv'])
    def analogous(self, t, col):
        """ Analogous (hue change +/-30°)
        Uses the colors of the same color temperature near each other on the wheel
        :param t: color type (from decorator)
        :param col: color as a list of values (from decorator)
        :return: tuple of analogous color tuples (in original color space) """
        return self.symmetrical_hue_calc(t, col, 30)

    @staticmethod
    def symmetrical_hue_calc(t, col, angle):
        """ Symmetrical hue calculation (+/-)
        :param t: color type
        :param col: color as a list of values
        :param angle: angle (in degrees)
        :return: tuple of symmetrical color tuples (in original color space) """
        t1 = list(col)
        t2 = list(col)
        if t in ['HSV', 'HSL']:
            t1[0] = (col[0] + (angle / 360.0)) % 1.0

            t2[0] = (col[0] - (angle / 360.0))
            if t2[0] < 0.0:
                t2[0] += 1.0
        elif t == 'HWB':
            t1[0] = (col[0] + angle) % 360
            t1[3] = cCV.HUEtoNCOL(t1[0])

            t2[0] = (col[0] - angle)
            if t2[0] < 0:
                t2[0] += 180
            t2[3] = cCV.HUEtoNCOL(t2[0])
        elif t == 'CIELCHab' or t == 'CIELCHuv':
            t1[2] = (col[2] + angle) % 360

            t2[2] = (col[2] - angle)
            if t2[2] < 0:
                t2[2] += 180

        return tuple(t1), tuple(t2)


class ColorChecker(object):
    # TODO: needs a fix for observer & comments (not corresponding)
    """ Original Munsell Notation CIE-L*ab, D50 2° """
    lfields_GretagMcBeth = ['Name', 'Hue', 'Value', 'Chroma', 'Yxy', 'CIE-L*ab']

    dGretagMcBeth_ColorChecker = {
        'Dark skin'    : ('3.05 YR', 3.69, 3.20, [10.1, 0.400, 0.350], [39.07, 13.70, 14.37]),
        'Light skin'   : ('2.2 YR', 6.47, 4.10, [35.8, 0.377, 0.345], [66.36, 18.08, 18.56]),
        'Blue sky'     : ('4.3 PB', 4.95, 5.55, [19.3, 0.247, 0.251], [50.66, -4.84, -21.44]),
        'Foliage'      : ('6.65 GY', 4.19, 4.15, [13.3, 0.337, 0.422], [44.03, -13.01, 22.34]),
        'Blue flower'  : ('9.65 PB', 5.47, 6.70, [24.3, 0.265, 0.240], [55.87, 8.88, -24.79]),
        'Bluish green' : ('2.5 BG', 7, 6, [43.1, 0.261, 0.343], [71.47, -32.98, 0.65]),
        'Orange'       : ('5 YR', 6, 11, [30.1, 0.506, 0.407], [62.37, 36.05, 56.58]),
        'Purplish blue': ('7.5 PB', 4, 10.7, [12.0, 0.211, 0.175], [40.77, 9.18, -43.58]),
        'Moderate red' : ('2.5 R', 5, 10, [19.8, 0.453, 0.306], [51.68, 48.21, 16.75]),
        'Purple'       : ('5 P', 3, 7, [6.6, 0.285, 0.202], [31.27, 20.00, -20.83]),
        'Yellow green' : ('5 GY', 7.08, 9.1, [44.3, 0.380, 0.489], [72.74, -22.60, 57.15]),
        'Orange yellow': ('10 YR', 7, 10.5, [43.1, 0.473, 0.438], [72.35, 19.57, 68.76]),
        'Blue'         : ('7.5 PB', 2.90, 12.75, [6.1, 0.187, 0.129], [29.61, 13.63, -49.65]),
        'Green'        : ('0.1 G', 5.38, 9.65, [23.4, 0.305, 0.478], [55.61, -37.19, 31.81]),
        'Red'          : ('5 R', 4, 12, [12.0, 0.539, 0.313], [42.23, 55.32, 27.45]),
        'Yellow'       : ('5 Y', 8, 11.1, [59.1, 0.448, 0.470], [82.65, 4.44, 80.52]),
        'Magenta'      : ('2.5 RP', 5, 12, [19.8, 0.364, 0.233], [52.55, 49.33, -14.42]),
        'Cyan'         : ('5 B', 5, 8, [19.8, 0.196, 0.252], [52.24, -28.24, -27.14]),
        'White'        : ('N', 9.5, '', [90.0, 0.310, 0.316], [96.37, -0.30, 3.26]),
        'Neutral 8'    : ('N', 8, '', [59.1, 0.310, 0.316], [81.70, -0.56, 0.25]),
        'Neutral 6.5'  : ('N', 6.5, '', [36.2, 0.310, 0.316], [66.49, -0.33, 0.03]),
        'Neutral 5'    : ('N', 5, '', [19.8, 0.310, 0.316], [50.67, -1.06, -0.19]),
        'Neutral 3.5'  : ('N', 3.5, '', [9.0, 0.310, 0.316], [36.23, -0.48, -0.26]),
        'Black'        : ('N', 2, '', [3.1, 0.310, 0.316], [20.68, 0.17, -0.55])
    }

    def __init__(self, *args, **kwargs):
        """ Init CIEObs as 2° observer with D50 illuminant """
        self.ColCheckerObs = rObs(variant='CIE1931', illum='D50')


def hsv_complement_color(h, s, v):
    """ get the complement of a rgb color
    :param h: Hue value (0-360)
    :param s: Saturation value (0-255)
    :param v: Value value (0-255)
    :return: HSV tuple """
    # perform 180° hue change
    tmp = 180
    if h > 180:
        tmp = -tmp

    return h + tmp, s, v


def rgG_to_RGB(r, g, G):
    """ Convert rg chromacity to RGB
    :param r: Red chromacity
    :param g: Green chromacity
    :param G: Green Value
    :return: RGB tuple """
    R = (r * G) / g
    B = ((1 - r - g) * G) / g
    return R, G, B


def rgb_tristimulus_to_chromacity(r, g, b, neg=True):
    """ Convert RGB tristimulus to chromacity coordinates
    :param r: Red value
    :param g: Green value
    :param b: Blue value
    :param neg: Allows keeping negative values in result
    :return: RGB chromacity coordinate """
    if min(r, g, b) < 0.0:
        print("RGB outside used gamut!")
        # return None

    # rgb values standardization
    r /= 3.78204
    g /= 3.78202
    b /= 3.78200

    # Determining chromacity (2D)
    l_rgb = r + g + b
    i_rgb = [i / l_rgb for i in (r, g, b)]

    if neg is not True:
        i_rgb = [max(0, i) for i in i_rgb]

    # returning ratio values
    return tuple(i_rgb)


def rgb_maximize(r, g, b, scale=255):
    """ Calculates full luminosity RGB values from rgb chromacity coordinates
    :param r: Red ratio
    :param g: Green ratio
    :param b: Blue ratio
    :param scale: Output R,G,B values scale
    :return: RGB tuple
    """
    ratio = scale / max(r, g, b)
    return tuple(int(i * ratio) for i in (r, g, b))


def rgb_complement_color(r, g, b):
    """ get the complement of a rgb color
    :param r: red value (0-255)
    :param g: green value (0-255)
    :param b: blue value (0-255)
    :return: RGB tuple """
    hsv = cCV.RGBtoHSV(r, g, b)
    hsv = hsv_complement_color(*hsv)
    return cCV.HSVtoRGB(*hsv)


def rgb_mix_colors(rgb_scale=255, *colors):
    # TODO: following received type
    """ color mix
    :param rgb_scale: scale of values
    :param colors: list of colors (tuple of rgb values)
    :return: relative mix of rgb colors """
    r = g = b = 0

    for item in colors:
        try:
            if not isinstance(item, tuple):
                raise TypeError
            if item[0] > rgb_scale or item[1] > rgb_scale or item[2] > rgb_scale:
                raise ValueError
        except (TypeError, ValueError):
            print("WARNING: Value is outside range or unhandled parameter given as function argument!")
        else:
            r += item[0]    # add red value from item
            g += item[1]    # add green value from item
            b += item[2]    # add blue value from item

    ratio = max(r, g, b)
    if ratio > rgb_scale:
        ratio = float(rgb_scale) / ratio
        r *= ratio
        g *= ratio
        b *= ratio

    return int(r), int(g), int(b)


def rgb_mix_colors2(c1, c2):
    """ color mix
    :param c1: color 1 (tuple of rgb values)
    :param c2: color 2 (tuple of rgb values)
    :return: relative mix of c1 & c2 """
    r1 = c1[0]
    g1 = c1[1]
    b1 = c1[2]

    r2 = c2[0]
    g2 = c2[1]
    b2 = c2[2]

    # remove white before mixing
    w1 = min(r1, g1, b1)
    w2 = min(r2, g2, b2)
    r1 -= w1
    g1 -= w1
    b1 -= w1
    r2 -= w2
    g2 -= w2
    b2 -= w2

    m1 = max(r1, g1, b1)
    m2 = max(r2, g2, b2)
    br = (m1 + m2) / (2 * 255.0)
    r3 = (r1 + r2) * br
    g3 = (g1 + g2) * br
    b3 = (b1 + b2) * br

    # average whiteness and add into final color
    w3 = (w1 + w2) / 2
    r3 += w3
    g3 += w3
    b3 += w3

    return int(r3), int(g3), int(b3)


def get_sat(x, y, sat_scale=255):
    """ Get saturation
    :param x: vect x coord
    :param y: vect y coord
    :param sat_scale: map x, y to scale
    :return: computed saturation of x, y, scale (from vect) proportionally mapped to scale """
    try:
        if x > sat_scale or y > sat_scale:
            raise ValueError
    except ValueError:
        print("Given x or y value is greater than range")
    else:
        return int(sqrt((((x * 255) / sat_scale) ** 2) + (((y * 255) / sat_scale) ** 2)))


# test des differentes fonctions de SMFSWcolor
if __name__ == "__main__":
    col_list = [(512, 10, 256),
                (30, 120, 50),
                (50, 40, 512),
                "exception",        # should raise TypeError when mixing
                (3800, 20, 50),     # should raise ValueError when mixing
                (512, 10, 512)]

    # example with a scale defined at 1024 instead of default, providing list of tuples as params already packed as list
    print("2 warning messages should be displayed on the next line:")
    print(rgb_mix_colors(1024, *col_list))
    print(rgb_mix_colors(255, (0, 255, 0), (0, 32, 255)))
    print(rgb_mix_colors2((0, 255, 0), (0, 32, 255)))

    print(rgb_mix_colors(255, (120, 255, 20), (60, 32, 255)))
    print(rgb_mix_colors2((120, 255, 20), (60, 32, 255)))

    print(get_sat(235, 100, 255))
    print(get_sat(5, 155, 255))

    print(rgb_complement_color(12, 50, 200))
    print(rgb_complement_color(200, 162, 11))

    # for i in range(1, 10):
    print("")
