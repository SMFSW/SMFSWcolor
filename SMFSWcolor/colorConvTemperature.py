# -*- coding: utf-8 -*-
"""
colorConvTemperature.py
Author: SMFSW
Copyright (c) 2016-2021 SMFSW
Description: Conversions of to/from White Point temperature
"""

from math import pow, log


def TEMPtoYxy(TempK):
    """ convert white temperature between 1000K & 25000K to xy chromacity
    :param TempK: temperature (in Kelvin)
    :return: Yxy tuple """
    if TempK > 25000 or TempK < 1000:
        raise ValueError
    elif TempK >= 4000:
        if TempK > 7000:
            x = (-2.0064e9 / pow(TempK, 3)) + (1.9018e6 / pow(TempK, 2)) + (0.24748e3 / TempK) + 0.237040
        else:
            x = (-4.6070e9 / pow(TempK, 3)) + (2.9678e6 / pow(TempK, 2)) + (0.09911e3 / TempK) + 0.244063

        y = (-3 * pow(x, 2)) + (2.87 * x) - 0.275
    else:
        x = (1.7791e-8 * pow(TempK, 2)) - (1.7931e-4 * TempK) + 0.81443
        y = (1.0042e-11 * pow(TempK, 3)) - (9.863e-8 * pow(TempK, 2)) + (2.9347e-4 * TempK) + 0.14033

    return 100.0, x, y


def TEMPtoRGB(TempK):
    """ convert white temperature to RGB color (precise between 1000K & 40000K)
    :param TempK: temperature (in Kelvin)
    :return: RGB tuple """
    min_max = lambda x: min(255, max(0, int(x)))
    temp = TempK / 100

    # Red calc
    if temp <= 66:
        R = 255
    else:
        # Note: the R-squared value for this approximation is .988
        calc = 329.698727446 * pow(temp - 60, -0.1332047592)
        R = min_max(calc)

    # Green calc
    if temp <= 66:
        # Note: the R-squared value for this approximation is .996
        calc = 99.4708025861 * log(temp) - 161.1195681661
    else:
        # Note: the R-squared value for this approximation is .987
        calc = 288.1221695283 * pow(temp - 60, -0.0755148492)
    G = min_max(calc)

    # Blue calc
    if temp >= 66:
        B = 255
    elif temp <= 19:
        B = 0
    else:
        # Note: the R-squared value for this approximation is .998
        calc = (138.5177312231 * log(temp - 10)) - 305.0447927307
        B = min_max(calc)

    return int(R), int(G), int(B)


def getTempXYZ(X, Y, Z):
    """ get color temperature from XYZ
    :param X: X value
    :param Y: Y value (luminance)
    :param Z: Z value
    :return: color temperature in Kelvin """
    XYZ = [i / 100.0 for i in (X, Y, Z)]
    tmp = sum(XYZ)

    if tmp == 0.0:
        return None
    else:
        # Calculate chromaticity co-ordinates
        xy = [XYZ[i] / tmp for i in range(2)]
        return getTempxy(*xy)


def getTempxy(x, y):
    """ get color temperature from Yxy
    :param x: x value
    :param y: y value
    :return: color temperature in Kelvin """
    try:
        # McCamy's formula to determine CCT
        tmp = (x - 0.3320) / (0.1858 - y)
        cct = (449.0 * pow(tmp, 3)) + (3525.0 * pow(tmp, 2)) + (6823.3 * tmp) + 5520.33
    except ZeroDivisionError:
        # Div by 0, returns None
        return None
    else:
        return int(cct)


if __name__ == "__main__":
    from refsTools import RefWhitePoint

    for (key, ([X, Y, Z], t, name)) in RefWhitePoint.dWhitePoint.items():
        print("{} illum: expected:{}K computed:{}  ref: {}".format(key, t, getTempXYZ(X, Y, Z), name))

    print("")
    for t in range(4000, 25000, 1000):
        print("{}K temperature xy chromacity coordinates {}".format(t, TEMPtoYxy(t)))

