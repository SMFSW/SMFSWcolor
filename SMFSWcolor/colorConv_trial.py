# -*- coding: utf-8 -*-
"""
colorConv_trial.py
Author: SMFSW
Copyright (c) 2016-2025 SMFSW

"""

from time import strftime
from SMFSWtoolbox.SMFSWmath import percent

import itertools
import SMFSWtoolbox.SMFSWunittst as unit_tests

import colorConv as cCV


maxerr = 50     # Max errors before aborting current test
thr = 1         # Warning threshold


@unit_tests.timetst()
def tstRGB_YUV_RGB():
    """ RGB to YUV back to RGB full range test """
    report.write("\n*** RGB->YUV->RGB test ***")
    nberr = nbt = 0
    random_pick = unit_tests.RandPickInRange(100000, 500000)
    for rtst, gtst, btst in itertools.product(range(256), range(256), range(256)):
        nbt += 1
        colYUV = cCV.RGBtoYUV(rtst, gtst, btst)
        colRGB = cCV.YUVtoRGB(*colYUV)

        random_pick.increment()
        if random_pick.compare() is True:
            random_pick.restart()
            report.write("\ncase pick -> From: {}-{}-{} / To: {} / Back: {}"
                         .format(rtst, gtst, btst, colYUV, colRGB))

        if colRGB > (rtst + thr, gtst + thr, btst + thr) or colRGB < (rtst - thr, gtst - thr, btst - thr):
            report.write("\nWARNING -> From: {}-{}-{} / To: {} / Back: {}"
                         .format(rtst, gtst, btst, colYUV, colRGB))
            nberr += 1

        try:
            assert nberr <= maxerr
        except AssertionError:
            break
    report.write("\n {} / {} tests : {}% passed".format(nbt, 256 ** 3, percent(nbt, 256 ** 3)))
    return nbt


@unit_tests.timetst()
def tstRGB_YIQ_RGB():
    """ RGB to YIQ back to RGB full range test """
    report.write("\n*** RGB->YIQ->RGB test ***")
    nberr = nbt = 0
    random_pick = unit_tests.RandPickInRange(100000, 500000)
    for rtst, gtst, btst in itertools.product(range(256), range(256), range(256)):
        nbt += 1
        colYIQ = cCV.RGBtoYIQ(rtst, gtst, btst)
        colRGB = cCV.YIQtoRGB(*colYIQ)

        random_pick.increment()
        if random_pick.compare() is True:
            random_pick.restart()
            report.write("\ncase pick -> From: {}-{}-{} / To: {} / Back: {}".format(rtst, gtst, btst, colYIQ, colRGB))

        if colRGB > (rtst + thr, gtst + thr, btst + thr) or colRGB < (rtst - thr, gtst - thr, btst - thr):
            report.write("\nWARNING -> From: {}-{}-{} / To: {} / Back: {}".format(rtst, gtst, btst, colYIQ, colRGB))
            nberr += 1

        try:
            assert nberr <= maxerr
        except AssertionError:
            break
    report.write("\n {} / {} tests : {}% passed".format(nbt, 256 ** 3, percent(nbt, 256 ** 3)))
    return nbt


@unit_tests.timetst()
def tstRGB_YCbCr_RGB():
    """ RGB to YCbCr back to RGB full range test """
    report.write("\n*** RGB->YCbCr->RGB test ***")
    nberr = nbt = 0
    random_pick = unit_tests.RandPickInRange(100000, 500000)
    for rtst, gtst, btst in itertools.product(range(256), range(256), range(256)):
        nbt += 1
        colYCbCr = cCV.RGBtoYCbCr(rtst, gtst, btst)
        colRGB = cCV.YCbCrtoRGB(*colYCbCr)

        random_pick.increment()
        if random_pick.compare() is True:
            random_pick.restart()
            report.write("\ncase pick -> From: {}-{}-{} / To: {} / Back: {}".format(rtst, gtst, btst, colYCbCr, colRGB))

        if colRGB > (rtst + thr, gtst + thr, btst + thr) or colRGB < (rtst - thr, gtst - thr, btst - thr):
            report.write("\nWARNING -> From: {}-{}-{} / To: {} / Back: {}".format(rtst, gtst, btst, colYCbCr, colRGB))
            nberr += 1

        try:
            assert nberr <= maxerr
        except AssertionError:
            break
    report.write("\n {} / {} tests : {}% passed".format(nbt, 256 ** 3, percent(nbt, 256 ** 3)))
    return nbt


@unit_tests.timetst()
def tstRGB_YDbDr_RGB():
    """ RGB to YDbDr back to RGB full range test """
    report.write("\n*** RGB->YDbDr->RGB test ***")
    nberr = nbt = 0
    random_pick = unit_tests.RandPickInRange(100000, 500000)
    for rtst, gtst, btst in itertools.product(range(256), range(256), range(256)):
        nbt += 1
        colYDbDr = cCV.RGBtoYDbDr(rtst, gtst, btst)
        colRGB = cCV.YDbDrtoRGB(*colYDbDr)

        random_pick.increment()
        if random_pick.compare() is True:
            random_pick.restart()
            report.write("\ncase pick -> From: {}-{}-{} / To: {} / Back: {}".format(rtst, gtst, btst, colYDbDr, colRGB))

        if colRGB > (rtst + thr, gtst + thr, btst + thr) or colRGB < (rtst - thr, gtst - thr, btst - thr):
            report.write("\nWARNING -> From: {}-{}-{} / To: {} / Back: {}".format(rtst, gtst, btst, colYDbDr, colRGB))
            nberr += 1

        try:
            assert nberr <= maxerr
        except AssertionError:
            break
    report.write("\n {} / {} tests : {}% passed".format(nbt, 256 ** 3, percent(nbt, 256 ** 3)))
    return nbt


@unit_tests.timetst()
def tstRGB_YCoCg_RGB():
    """ RGB to YCoCg back to RGB full range test """
    report.write("\n*** RGB->YCoCg->RGB test ***")
    nberr = nbt = 0
    random_pick = unit_tests.RandPickInRange(100000, 500000)
    for rtst, gtst, btst in itertools.product(range(256), range(256), range(256)):
        nbt += 1
        colYCoCg = cCV.RGBtoYCoCg(rtst, gtst, btst)
        colRGB = cCV.YCoCgtoRGB(*colYCoCg)

        random_pick.increment()
        if random_pick.compare() is True:
            random_pick.restart()
            report.write("\ncase pick -> From: {}-{}-{} / To: {} / Back: {}".format(rtst, gtst, btst, colYCoCg, colRGB))

        if colRGB > (rtst + thr, gtst + thr, btst + thr) or colRGB < (rtst - thr, gtst - thr, btst - thr):
            report.write("\nWARNING -> From: {}-{}-{} / To: {} / Back: {}".format(rtst, gtst, btst, colYCoCg, colRGB))
            nberr += 1

        try:
            assert nberr <= maxerr
        except AssertionError:
            break
    report.write("\n {} / {} tests : {}% passed".format(nbt, 256 ** 3, percent(nbt, 256 ** 3)))
    return nbt


@unit_tests.timetst()
def tstRGB_RGBW_RGB():
    """ RGB to RGBW back to RGB full range test """
    report.write("\n*** RGB->RGBW->RGB test ***")
    nberr = nbt = 0
    random_pick = unit_tests.RandPickInRange(100000, 500000)
    for rtst, gtst, btst in itertools.product(range(256), range(256), range(256)):
        nbt += 1
        colRGBW = cCV.RGBtoRGBW(rtst, gtst, btst)
        colRGB = cCV.RGBWtoRGB(*colRGBW)

        random_pick.increment()
        if random_pick.compare() is True:
            random_pick.restart()
            report.write("\ncase pick -> From: {}-{}-{} / To: {} / Back: {}".format(rtst, gtst, btst, colRGBW, colRGB))

        if colRGB != (rtst, gtst, btst):
            report.write("\nWARNING -> From: {}-{}-{} / To: {} / Back: {}".format(rtst, gtst, btst, colRGBW, colRGB))
            nberr += 1

        try:
            assert nberr <= maxerr
        except AssertionError:
            break
    report.write("\n {} / {} tests : {}% passed".format(nbt, 256 ** 3, percent(nbt, 256 ** 3)))
    return nbt


@unit_tests.timetst()
def tstRGB_RGBDim_RGB():
    """ RGB to RGBDim back to RGB full range test """
    report.write("\n*** RGB->RGBDim->RGB test ***")
    nberr = nbt = 0
    random_pick = unit_tests.RandPickInRange(100000, 500000)
    for rtst, gtst, btst in itertools.product(range(256), range(256), range(256)):
        nbt += 1
        colRGBDim = cCV.RGBtoRGBDim(rtst, gtst, btst, adapt=True)
        colRGB = cCV.RGBDimtoRGB(*colRGBDim)

        random_pick.increment()
        if random_pick.compare() is True:
            random_pick.restart()
            report.write("\ncase pick -> From: {}-{}-{} / To: {} / Back: {}".format(rtst, gtst, btst, colRGBDim, colRGB))

        if colRGB > (rtst + thr, gtst + thr, btst + thr) or colRGB < (rtst - thr, gtst - thr, btst - thr):
            report.write("\nWARNING -> From: {}-{}-{} / To: {} / Back: {}".format(rtst, gtst, btst, colRGBDim, colRGB))
            nberr += 1

        try:
            assert nberr <= maxerr
        except AssertionError:
            break
    report.write("\n {} / {} tests : {}% passed".format(nbt, 256 ** 3, percent(nbt, 256 ** 3)))
    return nbt


@unit_tests.timetst()
def tstRGB_HSV_RGB():
    """ RGB to HSV back to RGB full range test """
    report.write("\n*** RGB->HSV->RGB test ***")
    nberr = nbt = 0
    random_pick = unit_tests.RandPickInRange(100000, 500000)
    for rtst, gtst, btst in itertools.product(range(256), range(256), range(256)):
        nbt += 1
        colHSV = cCV.RGBtoHSV(rtst, gtst, btst)
        colRGB = cCV.HSVtoRGB(*colHSV)

        random_pick.increment()
        if random_pick.compare() is True:
            random_pick.restart()
            report.write("\ncase pick -> From: {}-{}-{} / To: {} / Back: {}".format(rtst, gtst, btst, colHSV, colRGB))

        if colRGB > (rtst + thr, gtst + thr, btst + thr) or colRGB < (rtst - thr, gtst - thr, btst - thr):
            report.write("\nWARNING -> From: {}-{}-{} / To: {} / Back: {}".format(rtst, gtst, btst, colHSV, colRGB))
            nberr += 1

        try:
            assert nberr <= maxerr
        except AssertionError:
            break
    report.write("\n {} / {} tests : {}% passed".format(nbt, 256 ** 3, percent(nbt, 256 ** 3)))
    return nbt


@unit_tests.timetst()
def tstRGB_HSL_RGB():
    """ RGB to HSL back to RGB full range test """
    report.write("\nRGB->HSL->RGB test")
    nberr = nbt = 0
    random_pick = unit_tests.RandPickInRange(100000, 500000)
    for rtst, gtst, btst in itertools.product(range(256), range(256), range(256)):
        nbt += 1
        colHSL = cCV.RGBtoHSL(rtst, gtst, btst)
        colRGB = cCV.HSLtoRGB(*colHSL)

        random_pick.increment()
        if random_pick.compare() is True:
            random_pick.restart()
            report.write("\ncase pick -> From: {}-{}-{} / To: {} / Back: {}".format(rtst, gtst, btst, colHSL, colRGB))

        if colRGB > (rtst + thr, gtst + thr, btst + thr) or colRGB < (rtst - thr, gtst - thr, btst - thr):
            report.write("\nWARNING -> From: {}-{}-{} / To: {} / Back: {}".format(rtst, gtst, btst, colHSL, colRGB))
            nberr += 1

        try:
            assert nberr <= maxerr
        except AssertionError:
            break
    report.write("\n {} / {} tests : {}% passed".format(nbt, 256 ** 3, percent(nbt, 256 ** 3)))
    return nbt


@unit_tests.timetst()
def tstRGB_HWB_NCS_HWB_RGB():
    """ RGB to HWB to NCS back to HWB to RGB full range test """
    report.write("\nRGB->HWB->NCS->HWB->RGB test")
    nberr = nbt = 0
    random_pick = unit_tests.RandPickInRange(100000, 500000)
    for rtst, gtst, btst in itertools.product(range(256), range(256), range(256)):
        nbt += 1
        colHWB = cCV.RGBtoHWB(rtst, gtst, btst)
        colNCS = cCV.HUEtoNCOL(colHWB[0]), colHWB[1], colHWB[2]
        colHWB2 = cCV.NCStoHWB(*colNCS)
        colRGB = cCV.HWBtoRGB(*colHWB2)

        random_pick.increment()
        if random_pick.compare() is True:
            random_pick.restart()
            report.write("\ncase pick -> From: {}-{}-{} / To: HWB {} - NCS {} - HWB {} / Back: {}"
                         .format(rtst, gtst, btst, colHWB, colNCS, colHWB2, colRGB))

        if colRGB > (rtst + thr, gtst + thr, btst + thr) or colRGB < (rtst - thr, gtst - thr, btst - thr):
            report.write("\nWARNING -> From: {}-{}-{} / To: HWB {} - NCS {} - HWB {} / Back: {}"
                         .format(rtst, gtst, btst, colHWB, colNCS, colHWB2, colRGB))
            nberr += 1

        try:
            assert nberr <= maxerr
        except AssertionError:
            break
    report.write("\n {} / {} tests : {}% passed".format(nbt, 256 ** 3, percent(nbt, 256 ** 3)))
    return nbt


@unit_tests.timetst()
def tstRGB_CMY_CMYK_CMY_RGB():
    """ RGB to CMY to CMYK back to CMY to RGB full range test """
    report.write("\nRGB->CMY->CMYK->CMY->RGB test")
    nberr = nbt = 0
    random_pick = unit_tests.RandPickInRange(100000, 500000)
    for rtst, gtst, btst in itertools.product(range(256), range(256), range(256)):
        nbt += 1
        colCMY = cCV.RGBtoCMY(rtst, gtst, btst)
        colCMYK = cCV.CMYtoCMYK(*colCMY)
        colCMY2 = cCV.CMYKtoCMY(*colCMYK)
        colRGB = cCV.CMYtoRGB(*colCMY2)

        random_pick.increment()
        if random_pick.compare() is True:
            random_pick.restart()
            report.write("\ncase pick -> From: {}-{}-{} / To: CMY {} - CMYK {} - CMY {} / Back: {}"
                         .format(rtst, gtst, btst, colCMY, colCMYK, colCMY2, colRGB))

        if colRGB > (rtst + thr, gtst + thr, btst + thr) or colRGB < (rtst - thr, gtst - thr, btst - thr):
            report.write("\nWARNING -> From: {}-{}-{} / To: CMY {} - CMYK {} - CMY {} / Back: {}"
                         .format(rtst, gtst, btst, colCMY, colCMYK, colCMY2, colRGB))
            nberr += 1

        try:
            assert nberr <= maxerr
        except AssertionError:
            break
    report.write("\n {} / {} tests : {}% passed".format(nbt, 256 ** 3, percent(nbt, 256 ** 3)))
    return nbt


@unit_tests.timetst()
def tstRGB_XYZ_Yxy_XYZ_RGB():
    """ RGB to XYZ to Yxy back to XYZ to RGB full range test """
    report.write("\nRGB->XYZ->Yxy->XYZ->RGB test")
    nberr = nbt = 0
    random_pick = unit_tests.RandPickInRange(100000, 500000)
    for rtst, gtst, btst in itertools.product(range(256), range(256), range(256)):
        nbt += 1
        colXYZ = cCV.RGBtoXYZ(rtst, gtst, btst)
        colYxy = cCV.XYZtoYxy(*colXYZ)
        colXYZ2 = cCV.YxytoXYZ(*colYxy)
        colRGB = cCV.XYZtoRGB(*colXYZ2)

        random_pick.increment()
        if random_pick.compare() is True:
            random_pick.restart()
            report.write("\ncase pick -> From: {}-{}-{} / To: XYZ {} - Yxy {} - XYZ {} / Back: {}"
                         .format(rtst, gtst, btst, colXYZ, colYxy, colXYZ2, colRGB))

        if colRGB > (rtst + thr, gtst + thr, btst + thr) or colRGB < (rtst - thr, gtst - thr, btst - thr):
            report.write("\nWARNING -> From: {}-{}-{} / To: XYZ {} - Yxy {} - XYZ {} / Back: {}"
                         .format(rtst, gtst, btst, colXYZ, colYxy, colXYZ2, colRGB))
            nberr += 1

        try:
            assert nberr <= maxerr
        except AssertionError:
            break
    report.write("\n {} / {} tests : {}% passed".format(nbt, 256 ** 3, percent(nbt, 256 ** 3)))
    return nbt


def cc_trial_report():
    """ Write all tests outputs to report """
    print("Running unit tests")

    report.write(tstRGB_XYZ_Yxy_XYZ_RGB())
    print("...")
    report.write(tstRGB_HSV_RGB())
    print("...")
    report.write(tstRGB_HSL_RGB())
    print("...")
    report.write(tstRGB_HWB_NCS_HWB_RGB())
    print("...")
    report.write(tstRGB_RGBW_RGB())
    print("...")
    report.write(tstRGB_RGBDim_RGB())
    print("...")
    report.write(tstRGB_YUV_RGB())
    print("...")
    report.write(tstRGB_YIQ_RGB())
    print("...")
    report.write(tstRGB_YCbCr_RGB())
    print("...")
    report.write(tstRGB_YDbDr_RGB())
    print("...")
    report.write(tstRGB_YCoCg_RGB())
    print("...")
    report.write(tstRGB_CMY_CMYK_CMY_RGB())
    print("...")

    report.close()
    print("End of unit tests")


file = 'testlogs/colorConv-{}_{}_{}-{}_{}_{}.log'.format(strftime("%Y"), strftime("%m"), strftime("%d"),
                                                         strftime("%H"), strftime("%M"), strftime("%S"))
report = open(file, 'w')    # create report at location

if __name__ == "__main__":
    cc_trial_report()


