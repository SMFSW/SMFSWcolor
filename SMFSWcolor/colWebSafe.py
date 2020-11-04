# -*- coding: utf-8 -*-
"""
colWebSafe.py
Author: SMFSW
Copyright (c) 2016-2018 SMFSW
Description: WebSafe color reference & class
"""
# TODO: add search nearest

from colHEX import ColHEX as cHEX


class RefWebSafe(object):
    """ WebSafe reference dicts & methods """
    @classmethod
    def searchref_WebSafe(cls, typ='HEX', srch=''):
        """ Search in Web safe colors dict
        :param typ: returned type
        :param srch: item to search
        :return: item found returned as type passed in parameter """
        try:
            for h, rgb in cls.ref_colWebSafe.items():
                if h == srch.upper() or rgb == srch:
                    if typ == 'RGB':
                        return rgb
                    else:
                        return h
        except KeyError:
            pass

    lfields_WebSafe = ['HEX', 'RGB']
    ref_colWebSafe = {
        # Col Hex   R    G   B
        '#FF00FF': (255, 0, 255),
        '#FF33FF': (255, 51, 255),
        '#CC00CC': (204, 0, 204),
        '#FF66FF': (255, 102, 255),
        '#CC33CC': (204, 51, 204),
        '#990099': (153, 0, 153),
        '#FF99FF': (255, 153, 255),
        '#CC66CC': (204, 102, 204),
        '#993399': (153, 51, 153),
        '#660066': (102, 0, 102),
        '#FFCCFF': (255, 204, 255),
        '#CC99CC': (204, 153, 204),
        '#996699': (153, 102, 153),
        '#663366': (102, 51, 102),
        '#330033': (51, 0, 51),

        '#CC00FF': (204, 0, 255),
        '#CC33FF': (204, 51, 255),
        '#9900CC': (153, 0, 204),
        '#CC66FF': (204, 102, 255),
        '#9933CC': (153, 51, 204),
        '#660099': (102, 0, 153),
        '#CC99FF': (204, 153, 255),
        '#9966CC': (153, 102, 204),
        '#663399': (102, 51, 153),
        '#330066': (51, 0, 102),

        '#9900FF': (153, 0, 255),
        '#9933FF': (153, 51, 255),
        '#6600CC': (102, 0, 204),
        '#9966FF': (153, 102, 255),
        '#6633CC': (102, 51, 204),
        '#330099': (51, 0, 153),

        '#6600FF': (102, 0, 255),
        '#6633FF': (102, 51, 255),
        '#3300CC': (51, 0, 204),

        '#3300FF': (51, 0, 255),

        '#0000FF': (0, 0, 255),
        '#3333FF': (51, 51, 255),
        '#0000CC': (0, 0, 204),
        '#6666FF': (102, 102, 255),
        '#3333CC': (51, 51, 204),
        '#000099': (0, 0, 153),
        '#9999FF': (153, 153, 255),
        '#6666CC': (102, 102, 204),
        '#333399': (51, 51, 153),
        '#000066': (0, 0, 102),
        '#CCCCFF': (204, 204, 255),
        '#9999CC': (153, 153, 204),
        '#666699': (102, 102, 153),
        '#333366': (51, 51, 102),
        '#000033': (0, 0, 51),

        '#0033FF': (0, 51, 255),

        '#3366FF': (51, 102, 255),
        '#0033CC': (0, 51, 204),
        '#0066FF': (0, 102, 255),

        '#6699FF': (102, 153, 255),
        '#3366CC': (51, 102, 204),
        '#003399': (0, 51, 153),
        '#3399FF': (51, 153, 255),
        '#0066CC': (0, 102, 204),
        '#0099FF': (0, 153, 255),

        '#99CCFF': (153, 204, 255),
        '#6699CC': (102, 153, 204),
        '#336699': (51, 102, 153),
        '#003366': (0, 51, 102),
        '#66CCFF': (102, 204, 255),
        '#3399CC': (51, 153, 204),
        '#006699': (0, 102, 153),
        '#33CCFF': (51, 204, 255),
        '#0099CC': (0, 153, 204),
        '#00CCFF': (0, 204, 255),

        '#00FFFF': (0, 255, 255),
        '#33FFFF': (51, 255, 255),
        '#00CCCC': (0, 204, 204),
        '#66FFFF': (102, 255, 255),
        '#33CCCC': (51, 204, 204),
        '#009999': (0, 153, 153),
        '#99FFFF': (153, 255, 255),
        '#66CCCC': (102, 204, 204),
        '#339999': (51, 153, 153),
        '#006666': (0, 102, 102),
        '#CCFFFF': (204, 255, 255),
        '#99CCCC': (153, 204, 204),
        '#669999': (102, 153, 153),
        '#336666': (51, 102, 102),
        '#003333': (0, 51, 51),

        '#00FFCC': (0, 255, 204),
        '#33FFCC': (51, 255, 204),
        '#00CC99': (0, 204, 153),
        '#66FFCC': (102, 255, 204),
        '#33CC99': (51, 204, 153),
        '#009966': (0, 153, 102),
        '#99FFCC': (153, 255, 204),
        '#66CC99': (102, 204, 153),
        '#339966': (51, 153, 102),
        '#006633': (0, 102, 51),

        '#00FF99': (0, 255, 153),
        '#33FF99': (51, 255, 153),
        '#00CC66': (0, 204, 102),
        '#66FF99': (102, 255, 153),
        '#33CC66': (51, 204, 102),
        '#009933': (0, 153, 51),

        '#00FF66': (0, 255, 102),
        '#33FF66': (51, 255, 102),
        '#00CC33': (0, 204, 51),

        '#00FF33': (0, 255, 51),

        '#00FF00': (0, 255, 0),
        '#33FF33': (51, 255, 51),
        '#00CC00': (0, 204, 0),
        '#66FF66': (102, 255, 102),
        '#33CC33': (51, 204, 51),
        '#009900': (0, 153, 0),
        '#99FF99': (153, 255, 153),
        '#66CC66': (102, 204, 102),
        '#339933': (51, 153, 51),
        '#006600': (0, 102, 0),
        '#CCFFCC': (204, 255, 204),
        '#99CC99': (153, 204, 153),
        '#669966': (102, 153, 102),
        '#336633': (51, 102, 51),
        '#003300': (0, 51, 0),

        '#33FF00': (51, 255, 0),

        '#66FF33': (102, 255, 51),
        '#33CC00': (51, 204, 0),
        '#66FF00': (102, 255, 0),

        '#99FF66': (153, 255, 102),
        '#66CC33': (102, 204, 51),
        '#339900': (51, 153, 0),
        '#99FF33': (153, 255, 51),
        '#66CC00': (102, 204, 0),
        '#99FF00': (153, 255, 0),

        '#CCFF99': (204, 255, 153),
        '#99CC66': (153, 204, 102),
        '#669933': (102, 153, 51),
        '#336600': (51, 102, 0),
        '#CCFF66': (204, 255, 102),
        '#99CC33': (153, 204, 51),
        '#669900': (102, 153, 0),
        '#CCFF33': (204, 255, 51),
        '#99CC00': (153, 204, 0),
        '#CCFF00': (204, 255, 0),

        '#FFFF00': (255, 255, 0),
        '#FFFF33': (255, 255, 51),
        '#CCCC00': (204, 204, 0),
        '#FFFF66': (255, 255, 102),
        '#CCCC33': (204, 204, 51),
        '#999900': (153, 153, 0),
        '#FFFF99': (255, 255, 153),
        '#CCCC66': (204, 204, 102),
        '#999933': (153, 153, 51),
        '#666600': (102, 102, 0),
        '#FFFFCC': (255, 255, 204),
        '#CCCC99': (204, 204, 153),
        '#999966': (153, 153, 102),
        '#666633': (102, 102, 51),
        '#333300': (51, 51, 0),

        '#FFCC00': (255, 204, 0),
        '#FFCC33': (255, 204, 51),
        '#CC9900': (204, 153, 0),
        '#FFCC66': (255, 204, 102),
        '#CC9933': (204, 153, 51),
        '#996600': (153, 102, 0),
        '#FFCC99': (255, 204, 153),
        '#CC9966': (204, 153, 102),
        '#996633': (153, 102, 51),
        '#663300': (102, 51, 0),

        '#FF9900': (255, 153, 0),
        '#FF9933': (255, 153, 51),
        '#CC6600': (204, 102, 0),
        '#FF9966': (255, 153, 102),
        '#CC6633': (204, 102, 51),
        '#993300': (153, 51, 0),

        '#FF6600': (255, 102, 0),
        '#FF6633': (255, 102, 51),
        '#CC3300': (204, 51, 0),

        '#FF3300': (255, 51, 0),

        '#FF0000': (255, 0, 0),
        '#FF3333': (255, 51, 51),
        '#CC0000': (204, 0, 0),
        '#FF6666': (255, 102, 102),
        '#CC3333': (204, 51, 51),
        '#990000': (153, 0, 0),
        '#FF9999': (255, 153, 153),
        '#CC6666': (204, 102, 102),
        '#993333': (153, 51, 51),
        '#660000': (102, 0, 0),
        '#FFCCCC': (255, 204, 204),
        '#CC9999': (204, 153, 153),
        '#996666': (153, 102, 102),
        '#663333': (102, 51, 51),
        '#330000': (51, 0, 0),

        '#FF0033': (255, 0, 51),

        '#FF3366': (255, 51, 102),
        '#CC0033': (204, 0, 51),
        '#FF0066': (255, 0, 102),

        '#FF6699': (255, 102, 153),
        '#CC3366': (204, 51, 102),
        '#990033': (153, 0, 51),
        '#FF3399': (255, 51, 153),
        '#CC0066': (204, 0, 102),
        '#FF0099': (255, 0, 153),

        '#FF99CC': (255, 153, 204),
        '#CC6699': (204, 102, 153),
        '#993366': (153, 51, 102),
        '#660033': (102, 0, 51),
        '#FF66CC': (255, 102, 204),
        '#CC3399': (204, 51, 153),
        '#990066': (153, 0, 102),
        '#FF33CC': (255, 51, 204),
        '#CC0099': (204, 0, 153),
        '#FF00CC': (255, 0, 204),

        '#FFFFFF': (255, 255, 255),
        '#CCCCCC': (204, 204, 204),
        '#999999': (153, 153, 153),
        '#666666': (102, 102, 102),
        '#333333': (51, 51, 51),
        '#000000': (0, 0, 0)
    }


class ColWebSafe(RefWebSafe, cHEX):
    """ WebSafe set of color class
    Inherits from colHEX & RefWebSafe """
    # TODO: recreate method to get data in dict (from self)
    def __init__(self, htm='#000000', *args, **kwargs):
        self.dfields_WebSafe = dict(zip(range(len(self.lfields_WebSafe)), self.lfields_WebSafe))    # make dict from fields list
        self.refs_WebSafe = lambda: [vars(self)[var] for var in self.lfields_WebSafe]               # make list from color space members

        self.getHEX_from_htm = lambda h: self.ref_colWebSafe.get(h)

        htm = self.searchref_WebSafe('HEX', htm)
        if htm is None:
            htm = '#000000'

        cHEX.__init__(self, htm, *args, **kwargs)
        self.type = 'WebSafe'   # can be used instead of isinstance on an object

    def get(self, srch='self'):
        """ get data from Web safe colors dict
        :param srch: to search in dict keys
        :return: either string ot tuple of the type passed as parameter """
        if srch == 'self':
            srch = self.HEX

        try:
            return self.ref_colWebSafe[srch.upper()]
        except KeyError:
            print("Key not found!!!")
            pass


if __name__ == "__main__":
    col_WebSafe = ColWebSafe('#FF0000')
    print(col_WebSafe)
    col_WebSafe = ColWebSafe('#999999')
    print(col_WebSafe)

    # print colors with link to index
    for i, col in enumerate(col_WebSafe.ref_colWebSafe):
        print("Color {} is: {}".format(i, col))
        if i >= 10:  # show only first 10
            break

    print(RefWebSafe.searchref_WebSafe('RGB', '#996600'))

    tst = '#8f8f8f'
    # print tuple of color values (from dict)
    print("Color {} corresponds to {}".format(tst, col_WebSafe.get(tst)))

    tst = '#996600'
    # print tuple of color values (from dict)
    print("Color {} corresponds to {}".format(tst, col_WebSafe.searchref_WebSafe('RGB', tst)))

    # print tuple of color values (from dict)
    print("Color {} corresponds to {}".format(col_WebSafe, col_WebSafe.get()))
    
    # print tuple of color values dissecting HTML color
    r, g, b = col_WebSafe.get()
    print("Color {} corresponds to {} {} {}".format(col_WebSafe, r, g, b))

    print("Still have to implement search for nearest!!!")
