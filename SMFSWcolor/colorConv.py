# -*- coding: utf-8 -*-
"""
colorConv.py
Author: SMFSW
Copyright (c) 2016-2025 SMFSW
Description: Low level conversion algorithms
"""
# TODO: see if round should be used before converting into integer (search int)

from math import *
import numpy as np

from colorConvGamma import *
from refsTools import RefRGBWorkingSpace


def RGBtoHEX(R, G, B):
    """ convert RGB to HEX color
    :param R: red value (0;255)
    :param G: green value (0;255)
    :param B: blue value (0;255)
    :return: HEX color string """
    rgb = tuple(int(i) for i in (R, G, B))
    return '#%02x%02x%02x' % rgb


def HEXtoRGB(Hex):
    """ convert HEX to RGB color
    :param Hex: HEX color integer or string
    :return: RGB tuple """
    if isinstance(Hex, str):
        Hex = int(Hex[1:], 16)

    R = (Hex >> 16) & 255
    G = (Hex >> 8) & 255
    B = Hex & 255

    return R, G, B


def XYZtoRGB(X, Y, Z, **kwargs):
    """ convert XYZ to RGB color
    :param X: X value
    :param Y: Y value (luminance)
    :param Z: Z value
    :param kwargs:
    **matrix (matrix): Given conversion matrix as keyword argument (will take precedence over rgb_space)
    **gamma: Gamma value if no rgb_space furnished (no gamma correction will be used as default if no rgb_space defined when using matrix)
    **rgb_space: RGB model name used for conversion from RefRGBWorkingSpace (sRGB is default)
    :return: RGB tuple (0;255) """
    if 'matrix' in kwargs and isinstance(kwargs['matrix'], np.matrix):
        m = kwargs['matrix']
        g = kwargs['gamma'] if 'gamma' in kwargs else 0.0
    else:
        rgb_space = kwargs['rgb_space'] if 'rgb_space' in kwargs and isinstance(kwargs['rgb_space'], str) else 'sRGB'
        m = RefRGBWorkingSpace.get_RGBWorkingSpace(rgb_space, to='RGB')
        g = rgb_space

    xyz = np.matrix([X, Y, Z])
    xyz = xyz / 100.0
    rgb = np.dot(m, xyz.T)

    for i in range(rgb.size):
        rgb[i] = int(gamma_compress(rgb[i], gamma=g) * 255.0)

    return tuple(float(rgb[i]) for i in range(rgb.size))


def RGBtoXYZ(R, G, B, **kwargs):
    """ convert RGB to XYZ color
    :param R: red value (0;255)
    :param G: green value (0;255)
    :param B: blue value (0;255)
    :param kwargs:
    **matrix (matrix): Given conversion matrix as keyword argument (will take precedence over rgb_space)
    **gamma: Gamma value if no rgb_space furnished (no gamma correction will be used as default if no rgb_space defined when using matrix)
    **rgb_space (str): RGB model name used for conversion from RefRGBWorkingSpace (sRGB is default)
    :return: XYZ tuple """
    if 'matrix' in kwargs and isinstance(kwargs['matrix'], np.matrix):
        m = kwargs['matrix']
        g = kwargs['gamma'] if 'gamma' in kwargs else 0.0
    else:
        rgb_space = kwargs['rgb_space'] if 'rgb_space' in kwargs and isinstance(kwargs['rgb_space'], str) else 'sRGB'
        m = RefRGBWorkingSpace.get_RGBWorkingSpace(rgb_space, to='XYZ')
        g = rgb_space

    rgb = np.matrix([gamma_expand(R / 255.0, gamma=g),
                     gamma_expand(G / 255.0, gamma=g),
                     gamma_expand(B / 255.0, gamma=g)])
    xyz = np.dot(m, rgb.T)

    return tuple(float(xyz[i] * 100.0) for i in range(xyz.size))


def XYZtoYxy(X, Y, Z):
    """ convert XYZ to Yxy color
    :param X: X value
    :param Y: Y value (luminance)
    :param Z: Z value
    :return: Yxy tuple """
    tmp_sum = X + Y + Z

    if tmp_sum == 0.0:
        x, y = 0.0, 0.0
    else:
        # Y = Y     # not needed
        x = X / tmp_sum
        y = Y / tmp_sum

    return Y, x, y


def YxytoXYZ(Y, x, y):
    """ convert Yxy to XYZ color
    :param Y: Y value (luminance)
    :param x: x value (0;1)
    :param y: y value (0;1)
    :return: XYZ tuple """

    if y == 0.0:
        X, Y, Z = 0.0, 0.0, 0.0
    else:
        tmp_cal = Y / y
        X = x * tmp_cal
        Y = Y
        Z = (1.0 - x - y) * tmp_cal

    return X, Y, Z


def XYZtoHunterLab(X, Y, Z, obs):
    """ convert XYZ to Hunter L*ab color
    :param X: X value
    :param Y: Y value (luminance)
    :param Z: Z value
    :param obs: Observer (CIEObs class or class inheriting from it)
    :return: Hunter L*ab tuple """
    Ka = (175.0 / 198.04) * (obs.ref_Y + obs.ref_X)
    Kb = (70.0 / 218.11) * (obs.ref_Y + obs.ref_Z)
    y = Y / obs.ref_Y

    if y == 0.0:
        HL, Ha, Hb = 0.0, 0.0, 0.0
    else:
        HL = 100.0 * sqrt(y)
        Ha = Ka * (((X / obs.ref_X) - y) / sqrt(y))
        Hb = Kb * ((y - (Z / obs.ref_Z)) / sqrt(y))

    return HL, Ha, Hb


def HunterLabtoXYZ(HL, Ha, Hb, obs):
    """ convert Hunter L*ab to XYZ color
    :param HL: L* value
    :param Ha: a value
    :param Hb: b value
    :param obs: Observer (CIEObs class or class inheriting from it)
    :return: XYZ tuple """
    Ka = (175.0 / 198.04) * (obs.ref_Y + obs.ref_X)
    Kb = (70.0 / 218.11) * (obs.ref_Y + obs.ref_Z)

    Y = ((HL / obs.ref_Y) ** 2) * 100.0
    X = (Ha / Ka * sqrt(Y / obs.ref_Y) + (Y / obs.ref_Y)) * obs.ref_X
    Z = -(Hb / Kb * sqrt(Y / obs.ref_Y) - (Y / obs.ref_Y)) * obs.ref_Z

    return X, Y, Z


def XYZtoCIELab(X, Y, Z, obs):  # XYZ - Lab
    """ convert XYZ to CIE-L*ab color
    :param X: X value
    :param Y: Y value (luminance)
    :param Z: Z value
    :param obs: Observer (CIEObs class or class inheriting from it)
    :return: CIE-L*ab tuple """
    xyz = [X / obs.ref_X, Y / obs.ref_Y, Z / obs.ref_Z]

    for i in range(len(xyz)):
        if xyz[i] > 0.008856:
            xyz[i] = pow(xyz[i], (1.0 / 3.0))
        else:
            xyz[i] = (7.787 * xyz[i]) + (16.0 / 116.0)

    CL = (116.0 * xyz[1]) - 16.0
    Ca = 500.0 * (xyz[0] - xyz[1])
    Cb = 200.0 * (xyz[1] - xyz[2])

    return CL, Ca, Cb


def CIELabtoXYZ(CL, Ca, Cb, obs):   # Lab - XYZ
    """ convert CIE-L*ab to XYZ color
    :param CL: L* value
    :param Ca: a value
    :param Cb: b value
    :param obs: observer (CIEObs class or class inheriting from it)
    :return: XYZ tuple """
    Y = (CL + 16.0) / 116.0
    xyz = [Ca / (500.0 + Y), Y, (Y - Cb) / 200.0]

    for i in range(len(xyz)):
        if pow(xyz[i], 3) > 0.008856:
            xyz[i] = pow(xyz[i], 3)
        else:
            xyz[i] = ((xyz[i] - 16.0) / 116.0) / 7.787

    xyz[0] *= obs.ref_X
    xyz[1] *= obs.ref_Y
    xyz[2] *= obs.ref_Z

    return tuple(xyz)


def CIELxxtoCIELCHxx(CL, Ca_u, Cb_v):   # L(ab)(uv) - LCH(ab)(uv)
    """ convert CIE-L*(ab/uv) to CIE-L*CH°(ab/uv) color LCH
    :param CL: L* value
    :param Ca_u: CIE-L*(ab/uv) a/u value
    :param Cb_v: CIE-L*(ab/uv) b/v value
    :return: CIE-L*CH°(ab/uv) tuple """
    CH = atan2(Cb_v, Ca_u)

    if CH > 0:
        CH = (CH / pi) * 180.0
    else:
        CH = 360.0 - ((abs(CH) / pi) * 180.0)

    CC = sqrt((Ca_u ** 2) + (Cb_v ** 2))

    return CL, CC, CH


def CIELCHxxtoCIELxx(CL, CC, CH):  # LCH(ab)(uv) - L(ab)(uv)
    """ convert CIE-L*CH°(ab/uv) to CIE-L*(ab/uv) color
    :param CL: L* value
    :param CC: C value
    :param CH: H° value (0 - 360°)
    :return: CIE-L*(ab/uv) tuple """
    Ca_u = cos(radians(CH)) * CC
    Cb_v = sin(radians(CH)) * CC

    return CL, Ca_u, Cb_v


def CIELxxtoHUE(Ca_u, Cb_v):
    """ convert CIE-L*(ab/uv) (ab/uv values) to Hue
    :param Ca_u: CIE-L*(ab/uv) a/u value
    :param Cb_v: CIE-L*(ab/uv) b/v value
    :return: returns CIE-H° value (0-360) """
    return degrees(atan2(Cb_v, Ca_u))


def XYZtoCIELuv(X, Y, Z, obs):
    """ convert XYZ to CIE-L*uv color
    :param X: X value
    :param Y: Y value (luminance)
    :param Z: Z value
    :param obs: observer
    :return: CIE-L*uv tuple """
    xyz = [i / 100.0 for i in (X, Y, Z)]
    denom = xyz[0] + (15.0 * xyz[1]) + (3.0 * xyz[2])

    if denom == 0.0:
        tmp_U, tmp_V = 0.0, 0.0
    else:
        tmp_U = (4.0 * xyz[0]) / denom
        tmp_V = (9.0 * xyz[1]) / denom

    # xyz[1] /= 100.0
    if xyz[1] > 0.008856:
        xyz[1] = pow(xyz[1], (1.0 / 3.0))
    else:
        xyz[1] = (7.787 * xyz[1]) + (16.0 / 116.0)

    CL = (116.0 * xyz[1]) - 16.0
    Cu = 13.0 * CL * (tmp_U - obs.ref_U)
    Cv = 13.0 * CL * (tmp_V - obs.ref_V)

    return CL, Cu, Cv


def CIELuvtoXYZ(CL, Cu, Cv, obs):
    """ convert CIE-L*uv to XYZ color
    :param CL: L* value
    :param Cu: u value
    :param Cv: v value
    :param obs: observer
    :return: CIE-L*uv tuple """
    Y = (CL + 16.0) / 116.0

    if pow(Y, 3) > 0.008856:
        Y = pow(Y, 3)
    else:
        Y = ((Y - 16.0) / 116.0) / 7.787

    tmp_U = Cu / (13.0 * CL) + obs.ref_U
    tmp_V = Cv / (13.0 * CL) + obs.ref_V

    X = -(9.0 * Y * tmp_U) / ((tmp_U - 4.0) * tmp_V - tmp_U * tmp_V)
    Z = (9.0 * Y - (15.0 * tmp_V * Y) - (tmp_V * X)) / (3.0 * tmp_V)

    return tuple(i * 100.0 for i in (X, Y, Z))


def YUVtoYDbDr(Y, U, V):
    """ convert YUV (PAL) to RGB color
    :param Y: Y value (0;1)
    :param U: U value (-0.436-0.436)
    :param V: V value (-0.615-0.615)
    :return: YDbDr tuple (Y0;1 D-1.333-1.333) """
    Db = 3.059 * U
    Dr = -2.169 * V
    return Y, Db, Dr


def YDbDrtoYUV(Y, Db, Dr):
    """ convert RGB to YUV color
    :param Y: Y value (0;1)
    :param Db: Db value (-1.333-1.333)
    :param Dr: Dr value (-1.333-1.333)
    :return: YUV (PAL) tuple (Y0;1 U-0.436-0.436 V-0.615-0.615) """
    U = Db / 3.059
    V = Dr / -2.169
    return Y, U, V


def RGBtoYUV(R, G, B):
    """ convert RGB to YUV (PAL) color
    :param R: red value (0;255)
    :param G: green value (0;255)
    :param B: blue value (0;255)
    :return: YUV tuple (Y0;1 U-0.436-0.436 V-0.615-0.615) """
    rgb = np.matrix([R, G, B]) / 255.0  # Scale RGB
    m = np.matrix([[0.299, 0.587, 0.114],
                   [-0.14713, -0.28886, 0.436],
                   [0.615, -0.51498, -0.10001]])

    YUV = np.dot(m, rgb.T)

    return tuple(float(YUV[i]) for i in range(YUV.size))


def YUVtoRGB(Y, U, V):
    """ convert YUV (PAL) to RGB color
    :param Y: Y value (0;1)
    :param U: U value (-0.436;0.436)
    :param V: V value (-0.615;0.615)
    :return: RGB tuple (0;255) """
    YUV = np.matrix([Y, U, V])
    m = np.matrix([[1.0, 0.0, 1.13983],
                   [1.0, -0.39465, -0.58060],
                   [1.0, 2.03211, 0.0]])

    rgb = np.dot(m, YUV.T)

    return tuple(int(rgb[i] * 255.0) for i in range(rgb.size))


def RGBtoYIQ(R, G, B):
    """ convert RGB to YIQ (NTSC) color
    :param R: red value (0;255)
    :param G: green value (0;255)
    :param B: blue value (0;255)
    :return: YIQ tuple (Y0;1 IQ-1;1) """
    rgb = np.matrix([R, G, B]) / 255.0  # Scale RGB
    m = np.matrix([[0.299, 0.587, 0.114],
                   [0.595716, -0.274453, -0.321263],
                   [0.211456, -0.522591, 0.311135]])

    YIQ = np.dot(m, rgb.T)

    return tuple(float(YIQ[i]) for i in range(YIQ.size))


def YIQtoRGB(Y, I, Q):
    """ convert YIQ (NTSC) to RGB color
    :param Y: Y value (0;1)
    :param I: I value (-1;1)
    :param Q: Q value (-1;1)
    :return: RGB tuple (0;255) """
    YIQ = np.matrix([Y, I, Q])
    m = np.matrix([[1.0, 0.9563, 0.6210],
                   [1.0, -0.2721, -0.6474],
                   [1.00, -1.1070, 1.7046]])

    rgb = np.dot(m, YIQ.T)

    return tuple(int(rgb[i] * 255.0) for i in range(rgb.size))


def RGBtoYCbCr(R, G, B):
    """ convert RGB to YCbCr color
    :param R: red value (0;255)
    :param G: green value (0;255)
    :param B: blue value (0;255)
    :return: YCbCr tuple (0;255) """
    Y = (R * 0.299) + (G * 0.587) + (B * 0.114)
    Cb = (R * -0.1687) + (G * -0.3313) + (B * 0.5) + 128.0
    Cr = (R * 0.5) + (G * -0.4187) + (B * -0.0813) + 128.0
    
    return tuple(int(i) for i in (Y, Cb, Cr))


def YCbCrtoRGB(Y, Cb, Cr):
    """ convert YUV to RGB color
    :param Y: Y value (0;255)
    :param Cb: Cb value (0;255)
    :param Cr: Cr value (0;255)
    :return: RGB tuple (0;255) """
    cb = Cb - 128.0
    cr = Cr - 128.0

    R = Y + (1.402 * cr)
    G = Y - (0.34414 * cb) - (0.71414 * cr)
    B = Y + (1.772 * cb)

    return tuple(int(i) for i in (R, G, B))


def RGBtoYDbDr(R, G, B):
    """ convert RGB to YDbDr (SECAM & PAL-N) color
    :param R: red value (0;255)
    :param G: green value (0;255)
    :param B: blue value (0;255)
    :return: YDbDr tuple (Y0;1 Dx-1.333;1.333) """
    rgb = np.matrix([R, G, B]) / 255.0  # Scale RGB
    m = np.matrix([[0.299, 0.587, 0.114],
                   [-0.450, -0.883, 1.333],
                   [-1.333, 1.116, 0.217]])

    YDbDr = np.dot(m, rgb.T)

    return tuple(float(YDbDr[i]) for i in range(YDbDr.size))


def YDbDrtoRGB(Y, Db, Dr):
    """ convert YDbDr (SECAM & PAL-N) to RGB color
    :param Y: Y value (0;1)
    :param Db: Db value (-1.333;1.333)
    :param Dr: Dr value (-1.333;1.333)
    :return: RGB tuple (0;255) """
    YDbDr = np.matrix([Y, Db, Dr])
    m = np.matrix([[1.0, 0.000092303716148, -0.525912630661865],
                   [1.0, -0.129132898890509, 0.267899328207599],
                   [1.00, 0.664679059978955, -0.000079202543533]])

    rgb = np.dot(m, YDbDr.T)

    return tuple(int(rgb[i] * 255.0) for i in range(rgb.size))


def YCoCgtoRGB(Y, Co, Cg):
    """ convert YCoCg to RGB color
    The YCoCg color model was developed to increase the effectiveness of the image compression.
    This color model comprises the luminance (Y) and two color difference components
    (Co - offset orange, Cg - offset green).
    :param Y: Y value (0;255)
    :param Co: Co value (0;255)
    :param Cg: Cg value (0;255)
    :return: RGB tuple (0;255) """
    R = Y + Co - Cg
    G = Y + Cg
    B = Y - Co - Cg

    return R, G, B


def RGBtoYCoCg(R, G, B):
    """ convert RGB to YCoCg color
    The YCoCg color model was developed to increase the effectiveness of the image compression.
    This color model comprises the luminance (Y) and two color difference components
    (Co - offset orange, Cg - offset green).
    :param R: red value (0;255)
    :param G: green value (0;255)
    :param B: blue value (0;255)
    :return: YCoCg tuple (0;255) """
    Y = (R / 4.0) + (G / 2.0) + (B / 4.0)
    Co = (R / 2.0) - (B / 2.0)
    Cg = (G / 2.0) - (R / 4.0) - (B / 4.0)

    return tuple(int(i) for i in (Y, Co, Cg))


def YCCtoRGB(Y, C1, C2):
    """ convert YCC to RGB color
    The Kodak* PhotoYCC* was developed for encoding Photo CD* image data.
    This model comprises luminance (Y) and two color difference, or chrominance (C1, C2) components.
    The PhotoYCC is optimized for the color photographic material,
    and provides a color gamut that is greater than the one that can currently be displayed.
    Warning: Converting YCC to RGB then back doesn't necessarily give the same result
    :param Y: Y value (0;1)
    :param C1: Co value (0;1)
    :param C2: Cg value (0;1)
    :return: RGB tuple (0;255) """
    y = 0.981 * Y

    R = y + (1.315 * (C2 - 0.537))
    G = y - (0.311 * (C1 - 0.612)) - (0.669 * (C2 - 0.537))
    B = y + (1.601 * (C1 - 0.612))

    return tuple(int(i * 255.0) for i in (R, G, B))


def RGBtoYCC(R, G, B):
    """ convert RGB to YCC color
    The Kodak* PhotoYCC* was developed for encoding Photo CD* image data.
    This model comprises luminance (Y) and two color difference, or chrominance (C1, C2) components.
    The PhotoYCC is optimized for the color photographic material,
    and provides a color gamut that is greater than the one that can currently be displayed.
    Warning: Converting RGB to YCC then back doesn't necessarily give the same result
    :param R: red value (0;255)
    :param G: green value (0;255)
    :param B: blue value (0;255)
    :return: YCC tuple (0;1) """
    rgb = [i / 255.0 for i in (R, G, B)]

    Y = (0.213 * rgb[0]) + (0.419 * rgb[1]) + (0.081 * rgb[2])
    C1 = (-0.131 * rgb[0]) - (0.256 * rgb[1]) + (0.387 * rgb[2]) + 0.612
    C2 = (0.373 * rgb[0]) - (0.312 * rgb[1]) - (0.061 * rgb[2]) + 0.537

    return Y, C1, C2


def RGBtoHSL(R, G, B):
    """ convert RGB to HSL color
    :param R: red value (0;255)
    :param G: green value (0;255)
    :param B: blue value (0;255)
    :return: HSL (TSL) tuple """
    rgb = [i / 255.0 for i in (R, G, B)]    # scale 8bits values to float 0;1

    maxi, mini = max(rgb), min(rgb)
    delta = maxi - mini                     # Delta RGB

    L = (maxi + mini) / 2.0

    if delta == 0.0:  # No chroma
        H, S = 0.0, 0.0
    else:               # Chromatic data
        if L < 0.5:
            S = delta / (maxi + mini)
        else:
            S = delta / (2.0 - maxi - mini)

        deltas = [(((maxi - i) / 6.0) + (delta / 2.0)) / delta for i in rgb]

        if rgb[0] == maxi:
            H = deltas[2] - deltas[1]
        elif rgb[1] == maxi:
            H = (1.0 / 3.0) + deltas[0] - deltas[2]
        else:
            H = (2.0 / 3.0) + deltas[1] - deltas[0]

        if H < 0.0:
            H += 1.0
        elif H > 1.0:
            H -= 1.0

    return H, S, L


def HSLtoRGB(H, S, L):
    """ convert HSL (TSL) to RGB color
    :param H: H value (0;1)
    :param S: S value (0;1)
    :param L: L value (0;1)
    :return: RGB tuple (0;255) """
    hsl = [H, S, L]

    if hsl[1] == 0.0:
        R = G = B = hsl[2]
    else:
        if hsl[2] < 0.5:
            tmp_2 = hsl[2] * (1.0 + hsl[1])
        else:
            tmp_2 = (hsl[2] + hsl[1]) - (hsl[1] * hsl[2])

        tmp_1 = (2.0 * hsl[2]) - tmp_2

        R = _hue2RGB(tmp_1, tmp_2, hsl[0] + (1.0 / 3.0))
        G = _hue2RGB(tmp_1, tmp_2, hsl[0])
        B = _hue2RGB(tmp_1, tmp_2, hsl[0] - (1.0 / 3.0))

    return tuple(int(i * 255.0) for i in (R, G, B))


def _hue2RGB(v1, v2, vH):
    """ convert hue to color component (0;1)
    :param v1: v1 value (0;1)
    :param v2: v2 value (0;1)
    :param vH: vH value (0;1)
    :return: component value for R, G or B """
    if vH < 0.0:
        vH += 1.0
    if vH > 1.0:
        vH -= 1.0

    if (6.0 * vH) < 1.0:
        return v1 + (v2 - v1) * 6.0 * vH
    if (2.0 * vH) < 1.0:
        return v2
    if (3.0 * vH) < 2.0:
        return v1 + (v2 - v1) * ((2.0 / 3.0) - vH) * 6.0

    return v1


def RGBtoHSV(R, G, B):
    """ convert RGB to HSV color
    :param R: red value (0;255)
    :param G: green value (0;255)
    :param B: blue value (0;255)
    :return: HSV (HSB) tuple """
    rgb = [i / 255.0 for i in (R, G, B)]    # scale 8bits values to float 0;1

    maxi, mini = max(rgb), min(rgb)
    delta = maxi - mini     # Delta RGB

    V = maxi

    if delta == 0.0:    # No chroma
        H, S = 0.0, 0.0
    else:               # Chromatic data
        S = delta / maxi

        if rgb[0] == maxi:
            H = (rgb[1] - rgb[2]) / delta
        elif rgb[1] == maxi:
            H = 2.0 + ((rgb[2] - rgb[0]) / delta)
        else:
            H = 4.0 + ((rgb[0] - rgb[1]) / delta)

        H /= 6.0

        if H < 0.0:
            H += 1.0
        # elif H > 1.0:
        #     H -= 1.0

    return round(H * 360.0, 2), int(S * 255.0), int(V * 255.0)


def HSVtoRGB(H, S, V):
    """ convert HSV (HSB) to RGB color
    :param H: Hue value (0;360)
    :param S: Saturation value (0;255)
    :param V: Value value (0;255)
    :return: RGB tuple (0;255) """
    H /= 360.0
    S /= 255.0
    V /= 255.0

    if S == 0.0:
        tmp_r = tmp_g = tmp_b = V
    else:
        tmp_h = H * 6.0

        if tmp_h == 6.0:
            tmp_h = 0.0   # H shall be < 1

        tmp_i = floor(tmp_h)
        tmp_1 = V * (1.0 - S)
        tmp_2 = V * (1.0 - S * (tmp_h - tmp_i))
        tmp_3 = V * (1.0 - S * (1.0 - (tmp_h - tmp_i)))

        if tmp_i == 0.0:
            tmp_r, tmp_g, tmp_b = V, tmp_3, tmp_1
        elif tmp_i == 1.0:
            tmp_r, tmp_g, tmp_b = tmp_2, V, tmp_1
        elif tmp_i == 2.0:
            tmp_r, tmp_g, tmp_b = tmp_1, V, tmp_3
        elif tmp_i == 3.0:
            tmp_r, tmp_g, tmp_b = tmp_1, tmp_2, V
        elif tmp_i == 4.0:
            tmp_r, tmp_g, tmp_b = tmp_3, tmp_1, V
        else:
            tmp_r, tmp_g, tmp_b = V, tmp_1, tmp_2

    return tuple(int(i * 255.0) for i in (tmp_r, tmp_g, tmp_b))


def RGBtoRGBW(R, G, B):
    """ convert RGB to RGBW color
    :param R: red value (0;255)
    :param G: green value (0;255)
    :param B: blue value (0;255)
    :return: RGBW tuple (0;255) """
    W = min(R, G, B)
    R -= W
    G -= W
    B -= W

    return R, G, B, W


def RGBWtoRGB(R, G, B, W):
    """ convert RGBW to RGB color
    :param R: red value (0;255)
    :param G: green value (0;255)
    :param B: blue value (0;255)
    :param W: white value (0;255)
    :return: RGB tuple (0;255) """
    if _testRGBW(R, G, B, W) is True:  # Constistancy test of RGBW color
        R += W
        G += W
        B += W

    return R, G, B


def _testRGBW(R, G, B, W):
    """ RGBW coherence color test
    :param R: red value (0;255)
    :param G: green value (0;255)
    :param B: blue value (0;255)
    :param W: white value (0;255)
    :return: True if coherent / False otherwise """
    try:
        if (R != 0) and (G != 0) and (B != 0):
            raise ValueError
    except ValueError:
        print("Incoherent RGBW value: more than 2 color components")
        return False

    try:
        if (R + W) not in range(256) or (G + W) not in range(256) or (B + W) not in range(256):
            raise ValueError
    except ValueError:
        print("Incoherent RGBW value: at least one op overflows")
        return False

    return True


def RGBDimtoRGB(R, G, B, Dim):
    """ convert RGBDim to RGB color
    :warning: When Dim is 0, no more color component information encoded
    :warning: Prefer RGBDimtoHSV function
    :param R: red value (0;255)
    :param G: green value (0;255)
    :param B: blue value (0;255)
    :param Dim: brightness value (0.0;100) -> can be specified over 100% if needed (beware of saturation)
    :return: RGB tuple (0;255) """
    bright = Dim / 100.0
    return tuple(int(i * bright) for i in (R, G, B))


def RGBtoRGBDim(R, G, B, adapt=True):
    """ convert RGB to RGBDim color
    :param R: red value (0;255)
    :param G: green value (0;255)
    :param B: blue value (0;255)
    :param adapt: adapt Dim & RGB (maximize color values) if set to True
    :return: RGBDim tuple (RGB0;255 Dim0;100) """
    # Dim assumed to be 100% by default
    Dim = 100.0

    if adapt is True:
        tmp = max(R, G, B)
        if tmp == 0:
            R, G, B = 0, 0, 0
        else:
            tmp = 255.0 / tmp
            R *= tmp
            G *= tmp
            B *= tmp
            Dim /= tmp

    return int(R), int(G), int(B), Dim


def RGBDimtoHSV(R, G, B, Dim):
    """ convert RGBDim to HSV color
    :param R: red value (0;255)
    :param G: green value (0;255)
    :param B: blue value (0;255)
    :param Dim: brightness value (0;100) -> can be specified over 100% if needed (beware of saturation)
    :return: HSV tuple """
    H, S, V = RGBtoHSV(R, G, B)
    V = Dim / 100.0

    return H, S, V


def HSVtoRGBDim(H, S, V):
    """ convert HSV to RGBDim color
    :param H: Hue value (0;1)
    :param S: Saturation value (0;1)
    :param V: Value value (0;1)
    :return: RGBDim tuple (0;255 Dim0;100) """
    R, G, B = HSVtoRGB(H, S, V)
    Dim = V * 100.0

    return int(R), int(G), int(B), Dim


def RGBtoCMY(R, G, B):
    """ convert RGB to CMY color
    :param R: red value (0;255)
    :param G: green value (0;255)
    :param B: blue value (0;255)
    :return: CMY tuple (0;1) """
    CMY = [1.0 - (i / 255.0) for i in (R, G, B)]
    return tuple(CMY)


def CMYtoRGB(C, M, Y):
    """ convert CMY to RGB color
    :param C: C value (0;1)
    :param M: M value (0;1)
    :param Y: Y value (0;1)
    :return: RGB tuple (0;255) """
    RGB = [(1.0 - i) * 255.0 for i in (C, M, Y)]
    return tuple(RGB)


def CMYtoCMYK(C, M, Y):
    """ convert CMY to CMYK color
    :param C: C value (0;1)
    :param M: M value (0;1)
    :param Y: Y value (0;1)
    :return: CMYK tuple (0;1) """
    tmp_K = 1.0

    for i in (C, M, Y):
        if i < tmp_K:
            tmp_K = i

    if tmp_K == 1.0:  # Black
        CMYK = [0.0, 0.0, 0.0]
    else:
        CMYK = [(i - tmp_K) / (1.0 - tmp_K) for i in (C, M, Y)]

    CMYK.append(tmp_K)

    return tuple(CMYK)


def CMYKtoCMY(C, M, Y, K):
    """ convert CMYK to CMY color
    :param C: C value (0;1)
    :param M: M value (0;1)
    :param Y: Y value (0;1)
    :param K: K value (0;1)
    :return: CMY tuple (0;1) """
    CMY = [(i * (1.0 - K)) + K for i in (C, M, Y)]
    return tuple(CMY)


def RGBtoHWB(R, G, B):
    """ convert RGB to HWB color
    :param R: red value (0;255)
    :param G: green value (0;255)
    :param B: blue value (0;255)
    :return: HWB tuple (H0;360, WB0;100) """
    rgb = [i / 255.0 for i in (R, G, B)]
    maxi, mini = max(rgb), min(rgb)

    b = 1.0 - maxi

    if mini == maxi:
        h = -1.0
    else:
        if mini == rgb[0]:
            f = rgb[1] - rgb[2]
            i = 3
        elif mini == rgb[1]:
            f = rgb[2] - rgb[0]
            i = 5
        else:
            f = rgb[0] - rgb[1]
            i = 1

        h = int(round((i - f / (maxi - mini)) * 60))

    return h, int(round(mini * 100)), int(round(b * 100))


def HWBtoRGB(H, WH, BL):
    """ convert HWB to RGB color
    :param H: hue value (0;360)
    :param WH: white value (0;100)
    :param BL: black value (0;100)
    :return: RGB tuple (0;255) """
    WH /= 100.0
    BL /= 100.0

    v = 1.0 - BL

    if H == -1.0:   # if hue is undefined
        v = int(v * 255)
        return v, v, v

    H /= 60.0

    i = int(H)
    f = H - i

    if i % 2 == 1:  # if i is odd
        f = 1.0 - f

    n = WH + f * (v - WH)   # linear interpolation between WH and v

    if i == 1:
        rgb = [n, v, WH]
    elif i == 2:
        rgb = [WH, v, n]
    elif i == 3:
        rgb = [WH, n, v]
    elif i == 4:
        rgb = [n, WH, v]
    elif i == 5:
        rgb = [v, WH, n]
    else:
        rgb = [v, n, WH]

    return tuple(int(i * 255.0) for i in rgb)


def NCStoHWB(Ncol, WH, BL):
    """ convert RGB to HWB color
    :param Ncol: Natural color value (str)
    :param WH: white value (0;100)
    :param BL: black value (0;100)
    :return: HWB tuple (H0;360, WB0;100) """
    try:
        if not isinstance(Ncol, str):
            raise TypeError
    except TypeError:
        return
    else:
        let = Ncol[0:1]
        perc = Ncol[1:3]

    try:
        let.capitalize()
        if perc == "":
            perc = 0
        perc = int(perc)
    except:
        return

    if let == "R":
        h = perc * 0.6
    elif let == "Y":
        h = 60 + (perc * 0.6)
    elif let == "G":
        h = 120 + (perc * 0.6)
    elif let == "C":
        h = 180 + (perc * 0.6)
    elif let == "B":
        h = 240 + (perc * 0.6)
    elif let == "M":
        h = 300 + (perc * 0.6)
    elif let == "W":    # R0 case for the moment
        h = 0
        WH = 100 - perc
        BL = perc
    else:
        return

    return int(round(h)), WH, BL


def HUEtoNCOL(H):
    """ convert Hue to Natural color
    :param H: hue value (0;360)
    :return: Natural color (str) """

    if H == -1.0:
        return "R0"

    H %= 360

    if H < 60:
        return "R" + str(int(H / 0.6))
    elif H < 120:
        return "Y" + str(int((H - 60) / 0.6))
    elif H < 180:
        return "G" + str(int((H - 120) / 0.6))
    elif H < 240:
        return "C" + str(int((H - 180) / 0.6))
    elif H < 300:
        return "B" + str(int((H - 240) / 0.6))
    elif H < 360:
        return "M" + str(int((H - 300) / 0.6))


if __name__ == "__main__":
    from sys import version_info

    if version_info > (3,):
        raw_input = input

    generate_rep = raw_input("Conversions trial by typing 'y'? (may take a while): ")
    if generate_rep == 'y' or generate_rep == 'Y':
        from colorConv_trial import *
        cc_trial_report()

    col_XYZ = RGBtoXYZ(36, 19, 9)
    print(col_XYZ)

    col_RGB = XYZtoRGB(*col_XYZ)
    print(col_RGB)

    RGBtoHWB(1, 3, 2)

    # col_sRGB = RGBtosRGB(20, 255, 60)
    # print(col_sRGB)
    # print(sRGBtoRGB(*col_sRGB))
