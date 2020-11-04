# -*- coding: utf-8 -*-
"""
colNamedColours.py
Author: SMFSW
Copyright (c) 2016-2018 SMFSW
Description: HTMLrestricted & CSS color space reference & classes
"""
# TODO: add search nearest
# TODO: ajouter la gestion des exceptions lorsque le nom de la couleur n'est pas trouvee

from colHEX import ColHEX as cHEX


class RefHTMLrestricted(object):
    """ HTMLrestricted reference dicts & methods """
    @classmethod
    def searchref_HTMLrestricted(cls, typ='HEX', srch=''):
        """ Search in restricted HTML colors dict
        :param typ: returned type
        :param srch: item to search
        :return: item found returned as type passed in parameter """
        try:
            for idx, (h, r, ms) in cls.ref_colHTMLrestricted.items():
                if h == srch.upper() or r == srch or ms == srch or idx == srch.lower():
                    if typ == 'HEX':
                        return h
                    elif typ == 'RGB':
                        return r
                    elif typ == 'MSCode':
                        return ms
                    else:  # if typ == 'Name':
                        return idx
        except KeyError:
            pass

    lfields_HTMLrestricted = ['Name', 'HEX', 'RGB', 'MSCode']
    ref_colHTMLrestricted = {   # restricted set of HTML colors reference
        'fuchsia': ('#FF00FF', (255, 0, 255), 16711935),
        'purple' : ('#800080', (128, 0, 128), 8388736),
        'blue'   : ('#0000FF', (0, 0, 255), 16711680),
        'navy'   : ('#000080', (0, 0, 128), 8388608),
        'aqua'   : ('#00FFFF', (0, 255, 255), 16776960),
        'teal'   : ('#008080', (0, 128, 128), 8421376),
        'lime'   : ('#00FF00', (0, 255, 0), 65280),
        'green'  : ('#008000', (0, 128, 0), 32768),
        'yellow' : ('#FFFF00', (255, 255, 0), 65535),
        'olive'  : ('#808000', (128, 128, 0), 32896),
        'red'    : ('#FF0000', (255, 0, 0), 255),
        'maroon' : ('#800000', (128, 0, 0), 128),
        'white'  : ('#FFFFFF', (255, 255, 255), 16777215),
        'silver' : ('#C0C0C0', (192, 192, 192), 12632256),
        'gray'   : ('#808080', (128, 128, 128), 8421504),
        'black'  : ('#000000', (0, 0, 0), 0)
    }


class RefCSS(object):
    """ CSS reference dicts & methods """
    @classmethod
    def searchref_CSS(cls, typ='HEX', srch=''):
        """ Search in CSS color dict
        :param typ: returned type
        :param srch: item to search
        :return: item found returned as type passed in parameter """
        try:
            for idx, (h, r, ms) in cls.ref_colCSS.items():
                if h == srch.upper() or r == srch or ms == srch or idx == srch.lower():
                    if typ == 'HEX':
                        return h
                    elif typ == 'RGB':
                        return r
                    elif typ == 'MSCode':
                        return ms
                    else:  # if typ == 'Name':
                        return idx
        except KeyError:
            pass

    lfields_CSS = ['Name', 'HEX', 'RGB', 'MSCode']
    ref_colCSS = {  # CSS colors reference
        # Colour Name,           Hex,        R,   G,   B,    Microsoft Access code nr
        'lightpink'           : ('#FFB6C1', (255, 182, 193), 12695295),
        'pink'                : ('#FFC0CB', (255, 192, 203), 13353215),
        'crimson'             : ('#DC143C', (220, 20, 60), 3937500),
        'lavenderblush'       : ('#FFF0F5', (255, 240, 245), 16118015),
        'palevioletred'       : ('#DB7093', (219, 112, 147), 9662683),
        'hotpink'             : ('#FF69B4', (255, 105, 180), 11823615),
        'deeppink'            : ('#FF1493', (255, 20, 147), 9639167),
        'mediumvioletred'     : ('#C71585', (199, 21, 133), 8721863),
        'orchid'              : ('#DA70D6', (218, 112, 214), 14053594),
        'thistle'             : ('#D8BFD8', (216, 191, 216), 14204888),
        'plum'                : ('#DDA0DD', (221, 160, 221), 14524637),
        'violet'              : ('#EE82EE', (238, 130, 238), 15631086),
        'fuchsia'             : ('#FF00FF', (255, 0, 255), 16711935),
        'darkmagenta'         : ('#8B008B', (139, 0, 139), 9109643),
        'purple'              : ('#800080', (128, 0, 128), 8388736),
        'mediumorchid'        : ('#BA55D3', (186, 85, 211), 13850042),
        'darkviolet'          : ('#9400D3', (148, 0, 211), 13828244),
        'darkorchid'          : ('#9932CC', (153, 50, 204), 13382297),
        'indigo'              : ('#4B0082', (75, 0, 130), 8519755),
        'blueviolet'          : ('#8A2BE2', (138, 43, 226), 14822282),
        'mediumpurple'        : ('#9370DB', (147, 112, 219), 14381203),
        'mediumslateblue'     : ('#7B68EE', (123, 104, 238), 15624315),
        'slateblue'           : ('#6A5ACD', (106, 90, 205), 13458026),
        'darkslateblue'       : ('#483D8B', (72, 61, 139), 9125192),
        'ghostwhite'          : ('#F8F8FF', (248, 248, 255), 16775416),
        'lavender'            : ('#E6E6FA', (230, 230, 250), 16443110),
        'blue'                : ('#0000FF', (0, 0, 255), 16711680),
        'mediumblue'          : ('#0000CD', (0, 0, 205), 13434880),
        'darkblue'            : ('#00008B', (0, 0, 139), 9109504),
        'navy'                : ('#000080', (0, 0, 128), 8388608),
        'midnightblue'        : ('#191970', (25, 25, 112), 7346457),
        'royalblue'           : ('#4169E1', (65, 105, 225), 14772545),
        'cornflowerblue'      : ('#6495ED', (100, 149, 237), 15570276),
        'lightsteelblue'      : ('#B0C4DE', (176, 196, 222), 14599344),
        'lightslategray'      : ('#778899', (119, 136, 153), 10061943),
        'slategray'           : ('#708090', (112, 128, 144), 9470064),
        'dodgerblue'          : ('#1E90FF', (30, 144, 255), 16748574),
        'aliceblue'           : ('#F0F8FF', (240, 248, 255), 16775408),
        'steelblue'           : ('#4682B4', (70, 130, 180), 11829830),
        'lightskyblue'        : ('#87CEFA', (135, 206, 250), 16436871),
        'skyblue'             : ('#87CEEB', (135, 206, 235), 15453831),
        'deepskyblue'         : ('#00BFFF', (0, 191, 255), 16760576),
        'lightblue'           : ('#ADD8E6', (173, 216, 230), 15128749),
        'powderblue'          : ('#B0E0E6', (176, 224, 230), 15130800),
        'cadetblue'           : ('#5F9EA0', (95, 158, 160), 10526303),
        'darkturquoise'       : ('#00CED1', (0, 206, 209), 13749760),
        'azure'               : ('#F0FFFF', (240, 255, 255), 16777200),
        'lightcyan'           : ('#E0FFFF', (224, 255, 255), 16777184),
        'paleturquoise'       : ('#AFEEEE', (175, 238, 238), 15658671),
        'aqua'                : ('#00FFFF', (0, 255, 255), 16776960),
        'darkcyan'            : ('#008B8B', (0, 139, 139), 9145088),
        'teal'                : ('#008080', (0, 128, 128), 8421376),
        'darkslategray'       : ('#2F4F4F', (47, 79, 79), 5197615),
        'mediumturquoise'     : ('#48D1CC', (72, 209, 204), 13422920),
        'lightseagreen'       : ('#20B2AA', (32, 178, 170), 11186720),
        'turquoise'           : ('#40E0D0', (64, 224, 208), 13688896),
        'aquamarine'          : ('#7FFFD4', (127, 255, 212), 13959039),
        'mediumaquamarine'    : ('#66CDAA', (102, 205, 170), 11193702),
        'mediumspringgreen'   : ('#00FA9A', (0, 250, 154), 10156544),
        'mintcream'           : ('#F5FFFA', (245, 255, 250), 16449525),
        'springgreen'         : ('#00FF7F', (0, 255, 127), 8388352),
        'mediumseagreen'      : ('#3CB371', (60, 179, 113), 7451452),
        'seagreen'            : ('#2E8B57', (46, 139, 87), 5737262),
        'honeydew'            : ('#F0FFF0', (240, 255, 240), 15794160),
        'darkseagreen'        : ('#8FBC8F', (143, 188, 143), 9419919),
        'palegreen'           : ('#98FB98', (152, 251, 152), 10025880),
        'lightgreen'          : ('#90EE90', (144, 238, 144), 9498256),
        'limegreen'           : ('#32CD32', (50, 205, 50), 3329330),
        'lime'                : ('#00FF00', (0, 255, 0), 65280),
        'forestgreen'         : ('#228B22', (34, 139, 34), 2263842),
        'green'               : ('#008000', (0, 128, 0), 32768),
        'darkgreen'           : ('#006400', (0, 100, 0), 25600),
        'lawngreen'           : ('#7CFC00', (124, 252, 0), 64636),
        'chartreuse'          : ('#7FFF00', (127, 255, 0), 65407),
        'greenyellow'         : ('#ADFF2F', (173, 255, 47), 3145645),
        'darkolivegreen'      : ('#556B2F', (85, 107, 47), 3107669),
        'yellowgreen'         : ('#9ACD32', (154, 205, 50), 3329434),
        'olivedrab'           : ('#6B8E23', (107, 142, 35), 2330219),
        'ivory'               : ('#FFFFF0', (255, 255, 240), 15794175),
        'beige'               : ('#F5F5DC', (245, 245, 220), 14480885),
        'lightyellow'         : ('#FFFFE0', (255, 255, 224), 14745599),
        'lightgoldenrodyellow': ('#FAFAD2', (250, 250, 210), 13826810),
        'yellow'              : ('#FFFF00', (255, 255, 0), 65535),
        'olive'               : ('#808000', (128, 128, 0), 32896),
        'darkkhaki'           : ('#BDB76B', (189, 183, 107), 7059389),
        'palegoldenrod'       : ('#EEE8AA', (238, 232, 170), 11200750),
        'lemonchiffon'        : ('#FFFACD', (255, 250, 205), 13499135),
        'khaki'               : ('#F0E68C', (240, 230, 140), 9234160),
        'gold'                : ('#FFD700', (255, 215, 0), 55295),
        'cornsilk'            : ('#FFF8DC', (255, 248, 220), 14481663),
        'goldenrod'           : ('#DAA520', (218, 165, 32), 2139610),
        'darkgoldenrod'       : ('#B8860B', (184, 134, 11), 755384),
        'floralwhite'         : ('#FFFAF0', (255, 250, 240), 15792895),
        'oldlace'             : ('#FDF5E6', (253, 245, 230), 15136253),
        'wheat'               : ('#F5DEB3', (245, 222, 179), 11788021),
        'orange'              : ('#FFA500', (255, 165, 0), 42495),
        'moccasin'            : ('#FFE4B5', (255, 228, 181), 11920639),
        'papayawhip'          : ('#FFEFD5', (255, 239, 213), 14020607),
        'blanchedalmond'      : ('#FFEBCD', (255, 235, 205), 13495295),
        'navajowhite'         : ('#FFDEAD', (255, 222, 173), 11394815),
        'antiquewhite'        : ('#FAEBD7', (250, 235, 215), 14150650),
        'tan'                 : ('#D2B48C', (210, 180, 140), 9221330),
        'burlywood'           : ('#DEB887', (222, 184, 135), 8894686),
        'darkorange'          : ('#FF8C00', (255, 140, 0), 36095),
        'bisque'              : ('#FFE4C4', (255, 228, 196), 12903679),
        'linen'               : ('#FAF0E6', (250, 240, 230), 15134970),
        'peru'                : ('#CD853F', (205, 133, 63), 4163021),
        'peachpuff'           : ('#FFDAB9', (255, 218, 185), 12180223),
        'sandybrown'          : ('#F4A460', (244, 164, 96), 6333684),
        'chocolate'           : ('#D2691E', (210, 105, 30), 1993170),
        'saddlebrown'         : ('#8B4513', (139, 69, 19), 1262987),
        'seashell'            : ('#FFF5EE', (255, 245, 238), 15660543),
        'sienna'              : ('#A0522D', (160, 82, 45), 2970272),
        'lightsalmon'         : ('#FFA07A', (255, 160, 122), 8036607),
        'coral'               : ('#FF7F50', (255, 127, 80), 5275647),
        'orangered'           : ('#FF4500', (255, 69, 0), 17919),
        'darksalmon'          : ('#E9967A', (233, 150, 122), 8034025),
        'tomato'              : ('#FF6347', (255, 99, 71), 4678655),
        'salmon'              : ('#FA8072', (250, 128, 114), 7504122),
        'mistyrose'           : ('#FFE4E1', (255, 228, 225), 14804223),
        'lightcoral'          : ('#F08080', (240, 128, 128), 8421616),
        'snow'                : ('#FFFAFA', (255, 250, 250), 16448255),
        'rosybrown'           : ('#BC8F8F', (188, 143, 143), 9408444),
        'indianred'           : ('#CD5C5C', (205, 92, 92), 6053069),
        'red'                 : ('#FF0000', (255, 0, 0), 255),
        'brown'               : ('#A52A2A', (165, 42, 42), 2763429),
        'firebrick'           : ('#B22222', (178, 34, 34), 2237106),
        'darkred'             : ('#8B0000', (139, 0, 0), 139),
        'maroon'              : ('#800000', (128, 0, 0), 128),
        'white'               : ('#FFFFFF', (255, 255, 255), 16777215),
        'whitesmoke'          : ('#F5F5F5', (245, 245, 245), 16119285),
        'gainsboro'           : ('#DCDCDC', (220, 220, 220), 14474460),
        'lightgrey'           : ('#D3D3D3', (211, 211, 211), 13882323),
        'silver'              : ('#C0C0C0', (192, 192, 192), 12632256),
        'darkgray'            : ('#A9A9A9', (169, 169, 169), 11119017),
        'gray'                : ('#808080', (128, 128, 128), 8421504),
        'dimgray'             : ('#696969', (105, 105, 105), 6908265),
        'black'               : ('#000000', (0, 0, 0), 0)
    }


class ColHTMLrestricted(RefHTMLrestricted, cHEX):
    """ restricted HTML set of colors class
    Inherits from colHEX & RefHTMLrestricted """
    # TODO: recreate method to get data in dict (from self)
    def __init__(self, name='black', *args, **kwargs):
        self.dfields_HTMLrestricted = dict(zip(range(len(self.lfields_HTMLrestricted)), self.lfields_HTMLrestricted))    # make dict from fields list
        self.refs_HTMLrestricted = lambda: [vars(self)[var] for var in self.lfields_HTMLrestricted]                      # make list from color space members

        self.getHEX_from_Name = lambda n: self.ref_colHTMLrestricted.get(n)[0]
        self.getRGB_from_Name = lambda n: self.ref_colHTMLrestricted.get(n)[1]
        self.getMSCode_from_Name = lambda n: self.ref_colHTMLrestricted.get(n)[2]

        tmp = self.searchref_HTMLrestricted('Name', name)
        if name is None:
            tmp = 'black'

        cHEX.__init__(self, self.get('HEX', tmp), *args, **kwargs)
        self.type = 'HTMLrestricted'  # can be used instead of isinstance on an object

    def get(self, typ='HEX', srch='self'):
        """ get data from restricted HTML colors dict
        :param typ: row in dict (from lfields_HTMLrestricted)
        :param srch: to search in dict keys
        :return: either string ot tuple of the type passed as parameter """
        if srch == 'self':
            srch = self.HEX

        if not isinstance(typ, str):
            pass
        elif typ == 'Name':
            return self.HEX
        else:
            try:
                srch = srch.lower()
                if srch in self.ref_colHTMLrestricted:
                    tup = self.ref_colHTMLrestricted.get(srch)
                    for idx, val in enumerate(self.lfields_HTMLrestricted):
                        if val == typ:
                            return tup[idx - 1]
            except KeyError:
                print("Key not found!!!")
                pass


class ColCSS(RefCSS, cHEX):
    """ CSS HTML set of colors class
    Inherits from colHEX & RefCSS """
    # TODO: recreate method to get data in dict (from self)
    def __init__(self, name='black', *args, **kwargs):
        self.dfields_CSS = dict(zip(range(len(self.lfields_CSS)), self.lfields_CSS))    # make dict from fields list
        self.refs_CSS = lambda: [vars(self)[var] for var in self.lfields_CSS]           # make list from color space members

        self.getHEX_from_Name = lambda n: self.ref_colCSS.get(n)[0]
        self.getRGB_from_Name = lambda n: self.ref_colCSS.get(n)[1]
        self.getMSCode_from_Name = lambda n: self.ref_colCSS.get(n)[2]

        tmp = self.searchref_CSS('Name', name)
        if name is None:
            tmp = 'black'

        cHEX.__init__(self, self.get('HEX', tmp), *args, **kwargs)
        self.type = 'CSS'   # can be used instead of isinstance on an object

    def get(self, typ='HEX', srch='self'):
        """ get data from CSS colors dict
        :param typ: row in dict (from lfields_CSS)
        :param srch: to search in dict keys
        :return: either string ot tuple of the type passed as parameter
        """
        if srch == 'self':
            srch = self.HEX

        if not isinstance(typ, str):
            pass
        elif typ == 'Name':
            return self.HEX
        else:
            try:
                srch = srch.lower()
                if srch in self.ref_colCSS:
                    tup = self.ref_colCSS.get(srch)
                    for idx, val in enumerate(self.lfields_CSS):
                        if val == typ:
                            return tup[idx - 1]
            except KeyError:
                print("Key not found!!!")
                pass


if __name__ == "__main__":
    # TODO: recreate method to get data in dict (from self)
    col_HTMr = ColHTMLrestricted('olive')
    print(col_HTMr.searchref_HTMLrestricted())  # TODO: what's the point if called without param?
    col_CSS = ColCSS('thistle')
    print(col_CSS.searchref_CSS())              # TODO: what's the point if called without param?

    test_cases = ['navy', 'aqua', 'teal', 'lime', 'green', 'yellow', 'olive', 'red', 'ghostwhite']

    for i, strcol in enumerate(test_cases):
        print("CSS set:\t\t\t\tColor {} corresponds to: HTML {} / RGB R{} G{} B{} / Access Code {}".format(
            strcol, col_CSS.get('HEX', strcol),
            col_CSS.get('RGB', strcol)[0], col_CSS.get('RGB', strcol)[1], col_CSS.get('RGB', strcol)[2],
            col_CSS.get('MSCode', strcol)
        ))

        print("HTML restricted set:\ttColor '{}' is RGB {}".format(strcol, col_HTMr.get('RGB', strcol)))
