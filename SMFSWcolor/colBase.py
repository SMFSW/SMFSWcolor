# -*- coding: utf-8 -*-
"""
colBase.py
Author: SMFSW
Copyright (c) 2016-2025 SMFSW
Description: Base class for colXXX
"""

from functools import wraps

from refsTools import RefRGBWorkingSpace, RefColorSet, RefAdaptation, RefWhitePoint
from CIEobs import CIEObs as rObs


class ColBase(rObs):
    """ Color base object containing static methods
    Inherits from CIEObs """
    global lfields

    def __init__(self, *args, **kwargs):
        """ Init Color Base
        :param kwargs:
        **rgb_space (str): RGB working space (provided by rgb_space or illuminant)
        **adaptation (str): Name of adaptation type """
        rObs.__init__(self, *args, **kwargs)

        self.dfields = dict(zip(range(len(self.lfields)), self.lfields))    # make dict from fields list
        self.refs = lambda: [vars(self)[var] for var in self.lfields]       # make list from color space members

        self.RGBSpace = kwargs['rgb_space'] if 'rgb_space' in kwargs and isinstance(kwargs['rgb_space'], str) else 'sRGB'
        self.Adaptation = kwargs['adaptation'] if 'adaptation' in kwargs and isinstance(kwargs['adaptation'], str) else 'None'

        try:
            self.WhitePoint = RefWhitePoint.dWhitePoint.get(self.ref_illum)[0]
        except TypeError:
            self.WhitePoint = None

        try:
            self.Gamma = RefColorSet.ref_ColorSet.get(self.RGBSpace)[11]
            self.GamutEfficiency = RefColorSet.ref_ColorSet.get(self.RGBSpace)[14]
            self.CodingEfficiency = RefColorSet.ref_ColorSet.get(self.RGBSpace)[15]
        except TypeError:
            # print("Model name not recognised. Applying a Gamma of 2.2 by default")
            self.GamutEfficiency = None
            self.CodingEfficiency = None
            self.Gamma = 2.2

    def __str__(self):
        """ :return: string representing values of tuple from self """
        return str(tuple(vars(self)[var] for var in self.lfields))

    def __parse(self, key):
        """ parse given parameter and return key if exists """
        try:
            if key in self.lfields:
                return key
            else:
                assert key < len(self.lfields)
                return self.dfields.get(key)
        except AssertionError:
            return None

    def __getitem__(self, key):
        """ :return: key from self """
        if self.__parse(key) is not None:
            return vars(self)[key]

    def __setitem__(self, key, val):
        """ :return: key from self """
        if self.__parse(key) is not None:
            vars(self)[key] = val
            return val

    @staticmethod
    def cancel_on(err):
        @wraps(err)
        def decorator(fct):
            def wrapper(self, *args, **kwargs):
                try:
                    return fct(self, *args, **kwargs)
                except err:
                    return
            return wrapper
        return decorator

    @staticmethod
    def copy_refs(cls):
        @wraps(cls)
        def decorator(fct):
            def wrapper(self, *args, **kwargs):
                return cls(fct(self, *args, **kwargs), adaptation=self.Adaptation, rgb_space=self.RGBSpace,
                           variant=self.ref_variant, illum=self.ref_illum)
            return wrapper
        return decorator

    @staticmethod
    def _parse_input(cls, *col):
        """ Wraps color argument(s) for low level conversion functions needs
        :param cls: color class to test against
        :param col: color represented as colXXX instance or tuple of values representing desired instance
        :return: wrapped parameters ready to be fed into low level conversion functions """
        if isinstance(col[0], cls):
            return [vars(col[0])[var] for var in cls.lfields]
        elif isinstance(col[0], tuple):
            return col[0]
        elif len(col) == len(cls.lfields):
            return col
        else:
            raise TypeError

    def setAdaptation(self, adapt):
        """ Changes Adaptation matrix with adapt """
        self.Adaptation = adapt if adapt in RefAdaptation.lAdaptation else 'None'

    def setRGBmodel(self, rgb_space):
        """ Changes RGBmodel with model """
        self.RGBSpace = rgb_space if rgb_space in RefRGBWorkingSpace.lRGBWorkingSpace else 'sRGB'
