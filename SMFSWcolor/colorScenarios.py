# -*- coding: utf-8 -*-
"""
colorScenarios.py
Author: SMFSW
Copyright (c) 2016-2025 SMFSW
Desc: color scenario & fader classes

"""

import os
import sys
import csv
import threading

from collections import OrderedDict
from copy import deepcopy

from colorConv import RGBtoHSV, HSVtoRGB, RGBtoXYZ, XYZtoRGB, XYZtoYxy, YxytoXYZ
from colorConvCIE import xy_to_uv76, uv76_to_xy


currentVersion = sys.version_info
if currentVersion[0] < 3 or currentVersion[1] < 3:     # till python 3.3
    from time import clock as get_clock
else:
    from time import process_time as get_clock


if sys.version_info > (3,):
    long = int


class Fader(object):
    """ Fader object """
    color_spaces = ['RGB', 'HSV', 'CIE1976']
    data_fields = (['Red', 'Green', 'Blue', 'Time'],        # RGB Scenario csv fields
                   ['Hue', 'Saturation', 'Value', 'Time'],  # HSV Scenario csv fields
                   ['Y', 'u\'', 'v\'', 'Time'])             # CIE1976 Scenario csv fields
    dfields = dict(zip(color_spaces, data_fields))

    def __init__(self, use_timer=False, **kwargs):
        """ Fader class initialization
        :param args:
        *use_timer (int): Set to True, uses timer for fading, otherwise needs to iterate manually
        :param kwargs:
        **on_period_elapsed (str): Callback function when period elapsed
        **on_fading_finished (str): Callback function when fading has finished
        **fading_space (str): Color space used for fading
        **input (str): Fading inputs color space
        **output (str): Fading outputs color space
        """
        self._fCbackPeriod = kwargs['on_period_elapsed'] if 'on_period_elapsed' in kwargs else None
        self._fCbackEnd = kwargs['on_fading_finished'] if 'on_fading_finished' in kwargs else None
        self._fTranisition = kwargs['fading_space'] if 'fading_space' in kwargs and kwargs['fading_space'] in self.color_spaces else 'RGB'
        self._fInput = kwargs['input'] if 'input' in kwargs and kwargs['input'] in self.color_spaces else 'RGB'
        self._fOutput = kwargs['output'] if 'output' in kwargs and kwargs['output'] in self.color_spaces else 'RGB'

        self.clamp_byte = lambda v: max(0.0, min(255.0, v))
        self.clamp_float = lambda v: max(0.0, min(1.0, v))

        self._fFields = Fader.dfields[self._fInput]

        self._fInc = [0, 0, 0]
        self._fCurrent = [0, 0, 0]

        self._fTimeCurrent, self._fTimeInc, self._fNbInc = 0, 0, 0

        self.fRun, self.fFinished = False, False

        self._fTimeUpdate = 0
        self._fHandler_en = False
        if use_timer is True:
            self._fHandler = threading.Thread(target=self.fade_inc)
            self._fHandler.daemon = True
            self._fHandler.start()

    def __iter__(self):
        return self

    def __next__(self):
        if self._fNbInc == 0:
            self.fFinished = True
            self._fCbackEnd() if self._fCbackEnd is not None else None
            raise StopIteration
        else:
            self._fNbInc -= 1

            self._fTimeCurrent += self._fTimeInc

            for i in range(len(self._fCurrent)):
                if self._fTranisition == 'RGB':
                    self._fCurrent[i] = self.clamp_byte(self._fCurrent[i] + self._fInc[i])
                elif self._fTranisition == 'HSV':
                    if i == 0:      # Hue
                        # TODO: for conversion, Hue can be coded on a float 0.0-1.0
                        self._fCurrent[i] = self.clamp_hue(self._fCurrent[i] + self._fInc[i])
                    else:
                        self._fCurrent[i] = self.clamp_byte(self._fCurrent[i] + self._fInc[i])
                elif self._fTranisition == 'CIE1976':
                    self._fCurrent[i] = self.clamp_float(self._fCurrent[i] + self._fInc[i])

            col = self.convert_space(self._fTranisition, self._fOutput, self._fCurrent)
            self._fCbackPeriod(col) if self._fCbackPeriod is not None else None

            return col, round(self._fTimeCurrent, 3)

    @staticmethod
    def clamp_hue(hue, scale=360.0):
        """ Start fading process
        :param hue: Hue value to clamp
        :param scale: Hue scale
        :return: Hue clamped value
        """
        if hue >= scale:
            return hue - scale
        elif hue < 0.0:
            return scale - hue
        else:
            return hue

    def fader_start(self, *args):
        """ Start fading process
        :param args:
        *args (OrderedDict or int x4): Arguments passed to fade_init """
        self.fRun, self.fFinished = True, False
        self.fade_init(*args)
        self._fTimeUpdate = get_clock()
        self.fHandler_start()

    def fader_stop(self):
        """ Stop fading process """
        self.fRun = False
        self.fHandler_stop()

    def fader_pause(self):
        """ Pause fading process """
        self.fRun = False
        self.fHandler_stop()

    def fader_resume(self):
        """ Resume fading process """
        self.fRun = True
        self._fTimeUpdate = get_clock()
        self.fHandler_start()

    def fHandler_start(self):
        """ Fader thread enable """
        self._fHandler_en = True

    def fHandler_stop(self):
        """ Fader thread disable """
        self._fHandler_en = False

    @staticmethod
    def convert_space(from_space, to_space, *args):
        col = args[0]
        if from_space == to_space:
            return col
        elif from_space == 'RGB':
            if to_space == 'HSV':
                return RGBtoHSV(*col)
            elif to_space == 'CIE1976':
                tmp = XYZtoYxy(*RGBtoXYZ(*col))
                uv = xy_to_uv76(tmp[1], tmp[2])
                return tmp[0], uv[0], uv[1]
        elif from_space == 'HSV':
            if to_space == 'RGB':
                return HSVtoRGB(*col)
            elif to_space == 'CIE1976':
                tmp = XYZtoYxy(*RGBtoXYZ(*HSVtoRGB(*col)))
                uv = xy_to_uv76(tmp[1], tmp[2])
                return tmp[0], uv[0], uv[1]
        elif from_space == 'CIE1976':
            xy = uv76_to_xy(col[1], col[2])
            if to_space == 'RGB':
                return XYZtoRGB(*YxytoXYZ(col[0], xy[0], xy[1]))
            elif to_space == 'HSV':
                return RGBtoHSV(*XYZtoRGB(*YxytoXYZ(col[0], xy[0], xy[1])))
        return col

    def fade_init(self, *args):
        """ Fading process init and launch
        :param args:
        *args[0] (OrderedDict): Comprising Red, Green, Blue, Time
        *args[0-3] (int): of the form Red, Green, Blue, Time """
        if isinstance(args[0], OrderedDict) or isinstance(args[0], dict):
            # TODO: get params as HSV & u'v' too
            col, tim = [int(args[0][self._fFields[0]]), int(args[0][self._fFields[1]]),
                        int(args[0][self._fFields[2]])], long(args[0][self._fFields[3]])
        else:
            col, tim = [args[0], args[1], args[2]], args[3]

        col = list(self.convert_space(self._fInput, self._fTranisition, col))

        if self._fTranisition == 'HSV':
            if self.convert_space('HSV', 'RGB', self._fCurrent) == (0, 0, 0):
                # Position Hue & Saturation, only increase value
                self._fCurrent[0] = col[0]
                self._fCurrent[1] = col[1]
            elif self.convert_space('HSV', 'RGB', col) == (0, 0, 0):
                # No change of Hue & Saturation, only decrease value
                col[0] = self._fCurrent[0]
                col[1] = self._fCurrent[1]

        delta = [0, 0, 0]
        for i in range(len(delta)):
            delta[i] = col[i] - self._fCurrent[i]
            if self._fTranisition == 'HSV' and i == 0:
                # Make the nearest transition on Hue if delta is more than half the color wheel
                if abs(delta[i]) > 180.0:
                    if delta[i] < 0.0:
                        delta[i] = delta[i] + 360.0
                    else:
                        delta[i] = delta[i] - 360.0

        delta_max = max([abs(i) for i in delta])

        if delta_max == 0:
            return
        elif tim == 0:
            self._fNbInc = 1
            self._fTimeInc = 1   # After 1ms
        else:
            self._fNbInc = delta_max
            self._fTimeInc = tim / delta_max

            if self._fTimeInc < 100:
                self._fTimeInc = 100
                self._fNbInc = max(1, int(tim / self._fTimeInc))

        self._fTimeInc /= 1000.0    # time.clock gives seconds

        for i in range(len(delta)):
            self._fInc[i] = float(delta[i]) / self._fNbInc

    def fade_inc(self):
        """ Fading thread (handles increments) """
        while 1:
            if self._fHandler_en is True:
                now = get_clock()
                if (now - self._fTimeUpdate) >= self._fTimeInc:
                    self._fTimeUpdate = now

                    if not self.fFinished:
                        try:
                            next(self)
                        except StopIteration:
                            pass

    def set_transition(self, space):
        """ Set new fading transition color space
        :param space: Color space used for fading """
        old = self._fTranisition
        self._fTranisition = space if space in self.color_spaces else 'RGB'
        self._fCurrent = list(self.convert_space(old, self._fTranisition, self._fCurrent))

    def set_input(self, space):
        """ Set new input values color space
        :param space: Fading inputs color space """
        self._fInput = space if space in self.color_spaces else 'RGB'
        self._fFields = Fader.dfields[self._fInput]

    def set_output(self, space):
        """ Set new output values color space
        :param space: Fading output color space """
        self._fOutput = space if space in self.color_spaces else 'RGB'


class Scenario(Fader):
    """ Scenario object """
    speed_mult = [16, 8, 4, 2, 1, 1.0 / 2, 1.0 / 4, 1.0 / 8, 1.0 / 16]  # Speeds

    def __init__(self, *args, **kwargs):
        """ Scenario class initialization
        :param args:
        *args[0] (list): scenario list (optional), specify file in kwargs instead
        :param kwargs:
        **dir (str): Scenario file directory
        **file (str): Scenario filename
        **loops (int): Number of loops to perform (0 - infinite)
        **on_scenario_finished (str): Callback function when scenario has finished
        """
        super(Scenario, self).__init__(on_fading_finished=self.scenar_step, **kwargs)

        self.sFile = ''
        self.sDatas = []

        self._sLoopsDone = 0
        self._sStep = -1
        self._sSpeed = 4

        self.sRun, self.sFinished = False, False

        if 'dir' in kwargs:
            os.chdir(kwargs['dir'])

        if 'file' in kwargs:
            self.read_datas(kwargs['file'])
        elif args and isinstance(args[0], list):
            self.sDatas = deepcopy(args[0])

        self._sCbackEnd = kwargs['on_scenario_finished'] if 'on_scenario_finished' in kwargs else None

        if 'loops' in kwargs:
            self.sLoop, self.sNbLoops = True, kwargs['loops']
        else:
            self.sLoop, self.sNbLoops = False, 0

    def read_datas(self, csv_file):
        """ Read scenario datas from csv file
        :param csv_file: input file """
        self.sFile = csv_file
        with open(self.sFile, 'r') as f:
            reader = csv.DictReader(f, fieldnames=self._fFields)
            for row in reader:
                self.sDatas.append(row)
            self.sDatas.pop(0)  # Remove header line

    def scenar_start(self):
        """ Start scenario process """
        self._fCurrent = [0, 0, 0]
        self._sSpeed = 4
        self._sLoopsDone = 0
        self._sStep = -1
        self.sRun, self.sFinished = True, False
        self.scenar_step()

    def scenar_stop(self):
        """ Stop scenario process """
        self.sRun = False
        self.fader_stop()

    def scenar_pause(self):
        """ Pause scenario process """
        self.fader_pause()

    def scenar_resume(self):
        """ Resume scenario process """
        self.fader_resume()

    def scenar_speed_up(self):
        """ Increase scenario speed """
        self._sSpeed = min(self._sSpeed + 1, len(self.speed_mult) - 1)

    def scenar_speed_down(self):
        """ Decrease scenario speed """
        self._sSpeed = max(self._sSpeed - 1, 0)

    def scenar_step(self):
        """ Scenario steps handler """
        end = False

        if self._sStep == len(self.sDatas) - 1:
            self._sStep = 0
            if self.sLoop:
                self._sLoopsDone += 1
                if self.sNbLoops:
                    if self.sNbLoops == self._sLoopsDone:
                        end = True
            else:
                end = True
        else:
            self._sStep += 1

        if end:
            self.scenar_stop()
            self.sFinished = True
            self._sCbackEnd() if self._sCbackEnd is not None else None

        if self.sRun:
            dat = deepcopy(self.sDatas[self._sStep])
            dat['Time'] = long(dat['Time']) * self.speed_mult[self._sSpeed]
            self.fader_start(dat)


# if __name__ == "__main__":
