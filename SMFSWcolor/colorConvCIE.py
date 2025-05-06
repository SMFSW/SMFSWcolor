# -*- coding: utf-8 -*-
"""
colorConvCIE.py
Author: SMFSW
Copyright (c) 2016-2025 SMFSW
Description: Conversions between CIE standards
"""


def XYZ_to_uv76(X, Y, Z):
    """ convert XYZ to CIE1976 u'v' coordinates
    :param X: X value
    :param Y: Y value (luminance)
    :param Z: Z value
    :return: u', v' in CIE1976 """
    denominator = (X + (15 * Y) + (3 * Z))
    
    if denominator == 0.0:
        u76, v76 = 0.0, 0.0
    else:
        u76 = (4 * X) / denominator
        v76 = (9 * Y) / denominator
    
    return u76, v76     # u', v' in CIE1976


def xy_to_uv60(x, y):           # CIE1931 to CIE1960
    """ convert CIE1931 xy to CIE1960 uv coordinates
    :param x: x value (CIE1931)
    :param y: y value (CIE1931)
    :return: CIE1960 u, v """
    denominator = ((-2 * x) + (12 * y) + 3)

    if denominator == 0.0:
        u60, v60 = 0.0, 0.0
    else:
        u60 = (4 * x) / denominator
        v60 = (6 * y) / denominator

    return u60, v60  # CIE1960 u, v


def xy_to_uv76(x, y):           # CIE1931 to CIE1976
    """ convert CIE1931 xy to CIE1976 u'v' coordinates
    :param x: x value (CIE1931)
    :param y: y value (CIE1931)
    :return: CIE1976 u', v' """
    denominator = ((-2 * x) + (12 * y) + 3)

    if denominator == 0.0:
        u76, v76 = 0.0, 0.0
    else:
        u76 = (4 * x) / denominator
        v76 = (9 * y) / denominator

    return u76, v76     # CIE1976 u', v'


def uv60_to_xy(u60, v60):       # CIE1960 to CIE1931
    """ convert CIE1960 uv to CIE1931 xy coordinates
    :param u60: u value (CIE1960)
    :param v60: v value (CIE1960)
    :return: CIE1931 x, y """
    denominator = (((6 * u60) / 2) - (12 * v60) + 6)

    if denominator == 0.0:
        x, y = 0.0, 0.0
    else:
        x = ((18 * u60) / 4) / denominator
        y = (3 * v60) / denominator

    return x, y  # CIE1931 x, y


def uv60_to_uv76(u60, v60):     # CIE1960 to CIE1976
    """ convert CIE1960 uv to CIE1976 u"v" coordinates
    :param u60: u value (CIE1960)
    :param v60: v value (CIE1960)
    :return: CIE1976 u', v' """

    v76 = (3 * v60) / 2

    return u60, v76     # CIE1976 u', v'


def uv76_to_uv60(u76, v76):     # CIE1976 to CIE1960
    """ convert CIE1976 u'v' to CIE1960 uv coordinates
    :param u76: u' value (CIE1976)
    :param v76: v' value (CIE1976)
    :return: CIE1960 u, v """

    v60 = (2 * v76) / 3

    return u76, v60  # CIE1960 u, v


def uv76_to_xy(u76, v76):       # CIE1976 to CIE1931
    """ convert CIE1976 u'v' to CIE1931 xy coordinates
    :param u76: u' value (CIE1976)
    :param v76: v' value (CIE1976)
    :return: CIE1931 x, y """
    denominator = (((9 * u76) / 2) - (12 * v76) + 9)
    
    if denominator == 0.0:
        x, y = 0.0, 0.0
    else:
        x = ((27 * u76) / 4) / denominator
        y = (3 * v76) / denominator

    return x, y     # CIE1931 x, y


class CIE1931(object):
    @staticmethod
    def fromCIE1931(x, y):
        """ convert CIE1931 xy to CIE1931 xy coordinates
        :param x: x value (CIE1931)
        :param y: y value (CIE1931)
        :return: CIE1931 xy """
        return x, y

    @staticmethod
    def fromCIE1960(u60, v60):
        """ convert CIE1960 uv to CIE1931 xy coordinates
        :param u60: u value (CIE1960)
        :param v60: v value (CIE1960)
        :return: CIE1931 x, y """
        return uv60_to_xy(u60, v60)

    @staticmethod
    def fromCIE1976(u76, v76):
        """ convert CIE1976 u'v' to CIE1931 xy coordinates
        :param u76: u' value (CIE1976)
        :param v76: v' value (CIE1976)
        :return: CIE1931 x, y """
        return uv76_to_xy(u76, v76)

    @staticmethod
    def toCIE1931(x, y):
        """ convert CIE1931 xy to CIE1931 xy coordinates
        :param x: x value (CIE1931)
        :param y: y value (CIE1931)
        :return: CIE1931 xy """
        return x, y

    @staticmethod
    def toCIE1960(x, y):
        """ convert CIE1931 xy to CIE1960 uv coordinates
        :param x: x value (CIE1931)
        :param y: y value (CIE1931)
        :return: CIE1960 u, v """
        return xy_to_uv60(x, y)

    @staticmethod
    def toCIE1976(x, y):
        """ convert CIE1931 xy to CIE1976 u'v' coordinates
        :param x: x value (CIE1931)
        :param y: y value (CIE1931)
        :return: CIE1976 u', v' """
        return xy_to_uv76(x, y)


class CIE1960(object):
    @staticmethod
    def fromCIE1931(x, y):
        """ convert CIE1931 xy to CIE1960 uv coordinates
        :param x: x value (CIE1931)
        :param y: y value (CIE1931)
        :return: CIE1960 u, v """
        return xy_to_uv60(x, y)

    @staticmethod
    def fromCIE1960(u60, v60):
        """ convert CIE1960 uv to CIE1960 uv coordinates
        :param u60: u value (CIE1960)
        :param v60: v value (CIE1960)
        :return: CIE1960 u, v """
        return u60, v60

    @staticmethod
    def fromCIE1976(u76, v76):
        """ convert CIE1976 u'v' to CIE1960 uv coordinates
        :param u76: u' value (CIE1976)
        :param v76: v' value (CIE1976)
        :return: CIE1960 u, v """
        return uv76_to_uv60(u76, v76)

    @staticmethod
    def toCIE1931(u60, v60):
        """ convert CIE1960 uv to CIE1931 xy coordinates
        :param u60: u value (CIE1960)
        :param v60: v value (CIE1960)
        :return: CIE1931 xy """
        return uv60_to_xy(u60, v60)

    @staticmethod
    def toCIE1960(u60, v60):
        """ convert CIE1960 uv to CIE1960 uv coordinates
        :param u60: u value (CIE1960)
        :param v60: v value (CIE1960)
        :return: CIE1960 u, v """
        return u60, v60

    @staticmethod
    def toCIE1976(u60, v60):
        """ convert CIE1960 uv to CIE1976 u'v' coordinates
        :param u60: u value (CIE1960)
        :param v60: v value (CIE1960)
        :return: CIE1976 u', v' """
        return uv60_to_uv76(u60, v60)


class CIE1976(object):
    @staticmethod
    def fromCIE1931(x, y):
        """ convert CIE1931 xy to CIE1976 u'v' coordinates
        :param x: x value (CIE1931)
        :param y: y value (CIE1931)
        :return: CIE1976 u', v' """
        return xy_to_uv76(x, y)

    @staticmethod
    def fromCIE1960(u60, v60):
        """ convert CIE1960 uv to CIE1976 u'v' coordinates
        :param u60: u value (CIE1960)
        :param v60: v value (CIE1960)
        :return: CIE1976 u', v' """
        return uv60_to_uv76(u60, v60)

    @staticmethod
    def fromCIE1976(u76, v76):
        """ convert CIE1976 u'v' to CIE1976 u'v' coordinates
        :param u76: u' value (CIE1976)
        :param v76: v' value (CIE1976)
        :return: CIE1976 u', v' """
        return u76, v76

    @staticmethod
    def toCIE1931(u76, v76):
        """ convert CIE1976 u'v' to CIE1931 xy coordinates
        :param u76: u' value (CIE1976)
        :param v76: v' value (CIE1976)
        :return: CIE1931 xy """
        return uv76_to_xy(u76, v76)

    @staticmethod
    def toCIE1960(u76, v76):
        """ convert CIE1976 u'v' to CIE1960 uv coordinates
        :param u76: u' value (CIE1976)
        :param v76: v' value (CIE1976)
        :return: CIE1960 u, v """
        return uv76_to_uv60(u76, v76)

    @staticmethod
    def toCIE1976(u76, v76):
        """ convert CIE1976 u'v' to CIE1976 u'v' coordinates
        :param u76: u' value (CIE1976)
        :param v76: v' value (CIE1976)
        :return: CIE1976 u', v' """
        return u76, v76


if __name__ == "__main__":
    xy = (0.23, 0.56)
    print("CIE1931 x{} y{}".format(xy[0], xy[1]))
    uv60 = xy_to_uv60(*xy)
    print("CIE1960 u{} v{}".format(uv60[0], uv60[1]))
    xy = uv60_to_xy(*uv60)
    print("CIE1931 x{} y{}".format(xy[0], xy[1]))
    print()
    xy = (0.5, 0.43)
    print("CIE1931 x{} y{}".format(xy[0], xy[1]))
    uv60 = xy_to_uv60(*xy)
    print("CIE1960 u{} v{}".format(uv60[0], uv60[1]))
    uv76 = uv60_to_uv76(*uv60)
    print("CIE1976 u'{} v'{}".format(uv76[0], uv76[1]))
    uv60 = uv76_to_uv60(*uv76)
    print("CIE1960 u{} v{}".format(uv60[0], uv60[1]))
    xy = uv60_to_xy(*uv60)
    print("CIE1931 x{} y{}".format(xy[0], xy[1]))
