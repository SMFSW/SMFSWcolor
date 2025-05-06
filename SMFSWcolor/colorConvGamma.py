# -*- coding: utf-8 -*-
"""
colorConvGamma.py
Author: SMFSW
Copyright (c) 2016-2025 SMFSW
Description: Gamma handling
"""

from math import pow

from refsTools import RefColorSet


def gamma_compress(lin_val, **kwargs):
    """ compute value adapted with gamma from linear value
    :param lin_val: linear value
    :param kwargs:
    **gamma: gamma value (None type returns without value compression)
    :return: converted value """
    # TODO: lin_val should be RGB tuple or matrix & returning RGB

    if 'gamma' in kwargs:
        if isinstance(kwargs['gamma'], str):
            gamma = RefColorSet.ref_RGBSpecifications[0].get(kwargs['gamma'])[3]
        else:
            gamma = kwargs['gamma']
    else:
        gamma = -2.2  # sRGB

    if gamma is None:
        return lin_val

    if lin_val < 0.0:
        complement = True
        lin_val = -lin_val
    else:
        complement = False

    if gamma > 0.0:
        com_val = pow(lin_val, 1.0 / gamma)
    elif gamma < 0.0:   # sRGB
        if lin_val <= 0.0031308:
            com_val = lin_val * 12.92
        else:
            com_val = (1.055 * pow(lin_val, (1.0 / 2.4))) - 0.055
    else:               # L*
        if lin_val <= (216.0 / 24389.0):
            com_val = (lin_val * (24389.0 / 2700.0))
        else:
            com_val = (1.16 * pow(lin_val, 1.0 / 3.0)) - 0.16

    return -com_val if complement is True else com_val


def gamma_expand(com_val, **kwargs):
    """ compute adapted linear value from gamma
    :param com_val: value adapted with gamma
    :param kwargs:
    **gamma: gamma value (None type returns without value compression)
    :return: linear value """
    # TODO: com_val should be RGB tuple or matrix & returning RGB

    if 'gamma' in kwargs:
        if isinstance(kwargs['gamma'], str):
            gamma = RefColorSet.ref_RGBSpecifications[0].get(kwargs['gamma'])[3]
        else:
            gamma = kwargs['gamma']
    else:
        gamma = -2.2    # sRGB

    if gamma is None:
        return com_val

    if com_val < 0.0:
        complement = True
        com_val = -com_val
    else:
        complement = False

    if gamma > 0.0:
        lin_val = pow(com_val, gamma)
    elif gamma < 0.0:       # sRGB
        if com_val <= 0.04045:
            lin_val = com_val / 12.92
        else:
            lin_val = pow((com_val + 0.055) / 1.055, 2.4)
    else:               # L*
        if com_val <= 0.08:
            lin_val = 2700.0 * com_val / 24389.0
        else:
            lin_val = ((((1000000.0 * com_val + 480000.0) * com_val + 76800.0) * com_val + 4096.0) / 1560896.0)

    return -lin_val if complement is True else lin_val


# if __name__ == "__main__":
