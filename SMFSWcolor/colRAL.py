# -*- coding: utf-8 -*-
"""
colRAL.py
Author: SMFSW
Copyright (c) 2016-2018 SMFSW
Description: RAL color reference & class
"""
# TODO: add search nearest

from colCIELab import ColCIELab as cCIELab


class RefRAL(object):
    """ RAL reference dicts & methods """
    @classmethod
    def searchref_RAL(cls, typ='HEX', srch=''):
        """ Search in RAL colors dict
        :param typ: returned type
        :param srch: item to search
        :return: item found returned as type passed in parameter """
        try:
            for idx, (h, l, n) in cls.ref_colRALclassic.items():
                if h == srch.upper() or l == srch or n.upper() == srch.upper() or idx == srch.upper():
                    if typ == 'HEX':
                        return h
                    elif typ == 'Lab':
                        return l
                    elif typ == 'Name':
                        return n
                    else:  # if typ == 'idx':
                        return idx
        except KeyError:
            print("Key not found!!!")
            pass

    lfields_RAL = ['id', 'HEX', 'Lab', 'Name']
    ref_colRALclassic = {   # set of RAL classic colors reference
        # HEX & RGB values are approximations
        # RAL        HEX       L*ab                     Name
        # Yellow
        'RAL1000': ('#BEBD7F', (76.02, -0.37, 27.64), 'Green beige'),
        'RAL1001': ('#C2B078', (74.99, 5.10, 24.64), 'Beige'),
        'RAL1002': ('#C6A664', (73.45, 6.83, 33.80), 'Sand yellow'),
        'RAL1003': ('#E5BE01', (75.99, 18.80, 72.93), 'Signal yellow'),
        'RAL1004': ('#CDA434', (71.42, 15.28, 69.28), 'Golden yellow'),
        'RAL1005': ('#A98307', (65.65, 12.30, 61.90), 'Honey yellow'),
        'RAL1006': ('#E4A010', (68.20, 21.13, 65.98), 'Maize yellow'),
        'RAL1007': ('#DC9D00', (68.38, 25.44, 67.13), 'Daffodil yellow'),
        'RAL1011': ('#8A6642', (59.92, 11.35, 29.17), 'Brown beige'),
        'RAL1012': ('#C7B446', (75.04, 4.64, 61.31), 'Lemon yellow'),
        'RAL1013': ('#EAE6CA', (88.13, 0.19, 9.67), 'Oyster white'),
        'RAL1014': ('#E1CC4F', (81.22, 2.47, 22.88), 'Ivory'),
        'RAL1015': ('#E6D690', (86.40, 2.06, 15.48), 'Light ivory'),
        'RAL1016': ('#EDFF21', (88.37, -9.78, 71.30), 'Sulfur yellow'),
        'RAL1017': ('#F5D033', (76.32, 19.37, 51.02), 'Saffron yellow'),
        'RAL1018': ('#F8F32B', (84.83, 3.05, 69.19), 'Zinc yellow'),
        'RAL1019': ('#9E9764', (62.62, 4.31, 12.94), 'Grey beige'),
        'RAL1020': ('#999950', (61.98, 0.39, 23.18), 'Olive yellow'),
        'RAL1021': ('#F3DA0B', (78.88, 10.03, 82.04), 'Rape yellow'),
        'RAL1023': ('#FAD201', (79.07, 10.46, 80.50), 'Traffic yellow'),
        'RAL1024': ('#AEA04B', (64.20, 7.95, 36.66), 'Ochre yellow'),
        'RAL1026': ('##FFFF0', (95.36, -21.56, 120.18), 'Luminous yellow'),
        'RAL1027': ('#9D9101', (58.15, 5.83, 47.68), 'Curry'),
        'RAL1028': ('#F4A90 ', (74.97, 29.64, 79.69), 'Melon yellow'),
        'RAL1032': ('#D6AE01', (72.32, 12.16, 66.97), 'Broom yellow'),
        'RAL1033': ('#F3A505', (73.20, 26.50, 63.47), 'Dahlia yellow'),
        'RAL1034': ('#EFA94A', (72.73, 21.40, 45.09), 'Pastel yellow'),
        'RAL1035': ('#6A5D4D', (54.79, 0.35, 11.86), 'Pearl beige'),
        'RAL1036': ('#705335', (48.95, 4.77, 26.69), 'Pearl gold'),
        'RAL1037': ('#F39F18', (70.28, 26.19, 64.79), 'Sun yellow'),
        # Orange
        'RAL2000': ('#ED760E', (60.35, 34.64, 54.65), 'Yellow orange'),
        'RAL2001': ('#C93C20', (49.41, 39.79, 35.29), 'Red orange'),
        'RAL2002': ('#CB2821', (47.74, 47.87, 33.73), 'Vermilion'),
        'RAL2003': ('#FF7514', (66.02, 41.22, 52.36), 'Pastel orange'),
        'RAL2004': ('#F44611', (56.89, 50.34, 49.81), 'Pure orange'),
        'RAL2005': ('#FF2301', (62.26, 87.83, 94.26), 'Luminous orange'),
        'RAL2007': ('#FFA420', (76.86, 47.87, 97.63), 'Luminous bright orange'),
        'RAL2008': ('#F75E25', (61.99, 44.64, 51.72), 'Bright red orange'),
        'RAL2009': ('#F54021', (55.83, 47.79, 48.83), 'Traffic orange'),
        'RAL2010': ('#D84B20', (55.39, 40.10, 42.42), 'Signal orange'),
        'RAL2011': ('#EC7C26', (61.76, 38.16, 52.39), 'Deep orange'),
        'RAL2012': ('#E55137', (57.75, 40.28, 30.66), 'Salmon range'),
        'RAL2013': ('#C35831', (40.73, 32.14, 34.92), 'Pearl orange'),
        # Red
        'RAL3000': ('#AF2B1E', (42.40, 43.24, 25.00), 'Flame red'),
        'RAL3001': ('#A52019', (40.19, 41.21, 21.60), 'Signal red'),
        'RAL3002': ('#A2231D', (39.82, 41.84, 22.04), 'Carmine red'),
        'RAL3003': ('#9B111E', (35.59, 35.87, 15.75), 'Ruby red'),
        'RAL3004': ('#75151E', (33.05, 25.61, 9.02), 'Purple red'),
        'RAL3005': ('#5E2129', (30.96, 18.46, 5.76), 'Wine red'),
        'RAL3007': ('#412227', (28.34, 8.14, 2.22), 'Black red'),
        'RAL3009': ('#642424', (35.05, 19.93, 11.53), 'Oxide red'),
        'RAL3011': ('#781F19', (34.52, 28.66, 13.44), 'Brown red'),
        'RAL3012': ('#C1876B', (63.81, 20.79, 20.45), 'Beige red'),
        'RAL3013': ('#A12312', (40.70, 36.67, 21.37), 'Tomato red'),
        'RAL3014': ('#D36E70', (60.17, 32.49, 12.58), 'Antique pink'),
        'RAL3015': ('#EA899A', (72.73, 20.48, 3.96), 'Light pink'),
        'RAL3016': ('#B32821', (44.70, 37.92, 23.96), 'Coral red'),
        'RAL3017': ('#E63244', (54.24, 44.26, 16.87), 'Rose'),
        'RAL3018': ('#D53032', (50.77, 49.15, 19.86), 'Strawberry red'),
        'RAL3020': ('#CC0605', (44.66, 52.03, 32.26), 'Traffic red'),
        'RAL3022': ('#D95030', (58.10, 36.44, 27.34), 'Salmon pink'),
        'RAL3024': ('#F80000', (51.32, 82.52, 71.62), 'Luminous red'),
        'RAL3026': ('#FE0000', (54.38, 86.26, 76.07), 'Luminous'),
        'RAL3027': ('#C51D34', (43.07, 46.96, 15.81), 'Raspberry red'),
        'RAL3028': ('#CB3234', (48.80, 54.42, 33.08), 'Pure red'),
        'RAL3031': ('#B32428', (43.87, 41.37, 18.33), 'Orient red'),
        'RAL3032': ('#721422', (26.88, 41.34, 19.40), 'Pearl ruby red'),
        'RAL3033': ('#B44C43', (44.29, 45.11, 28.62), 'Pearl pink'),
        # Violet
        'RAL4001': ('#6D3F5B', (49.10, 17.35, -12.85), 'Red lilac'),
        'RAL4002': ('#922B3E', (41.91, 30.05, 5.67), 'Red violet'),
        'RAL4003': ('#DE4C8A', (56.81, 40.89, -5.53), 'Heather violet'),
        'RAL4004': ('#641C34', (32.22, 24.83, 0.06), 'Claret violet'),
        'RAL4005': ('#6C4675', (50.92, 15.38, -23.06), 'Blue lilac'),
        'RAL4006': ('#A03472', (42.38, 39.48, -14.94), 'Traffic purple'),
        'RAL4007': ('#4A192C', (30.05, 13.16, -5.10), 'Purple violet'),
        'RAL4008': ('#924E7D', (44.82, 29.08, -18.58), 'Signal violet'),
        'RAL4009': ('#A18594', (60.59, 10.38, -2.88), 'Pastel violet'),
        'RAL4010': ('#CF3476', (50.39, 48.95, -4.24), 'Telemagenta'),
        'RAL4011': ('#8673A1', (47.92, 18.89, -20.83), 'Pearl violet'),
        'RAL4012': ('#6C6874', (46.33, 7.27, -11.94), 'Pearl black berry'),
        # Blue
        'RAL5000': ('#354D73', (38.30, 1.90, -19.45), 'Violet blue'),
        'RAL5001': ('#1F3438', (35.43, -7.52, -16.65), 'Green blue'),
        'RAL5002': ('#20214F', (33.11, 8.43, -35.40), 'Ultramarine blue'),
        'RAL5003': ('#1D1E33', (30.53, -0.37, -16.68), 'Saphire blue'),
        'RAL5004': ('#18171C', (26.56, -0.19, -4.07), 'Black blue'),
        'RAL5005': ('#1E2460', (38.35, -5.03, -32.56), 'Signal blue'),
        'RAL5007': ('#3E5F8A', (46.37, -6.24, -21.71), 'Brillant blue'),
        'RAL5008': ('#26252D', (32.00, -2.09, -6.07), 'Grey blue'),
        'RAL5009': ('#025669', (41.22, -9.56, -18.34), 'Azure blue'),
        'RAL5010': ('#0E294B', (36.57, -5.81, -28.94), 'Gentian blue'),
        'RAL5011': ('#231A24', (28.21, -1.11, -8.72), 'Steel blue'),
        'RAL5012': ('#3B83BD', (55.62, -13.84, -30.72), 'Light blue'),
        'RAL5013': ('#1E213D', (29.81, 1.67, -17.20), 'Cobalt blue'),
        'RAL5014': ('#606E8C', (53.79, -2.64, -15.59), 'Pigeon blue'),
        'RAL5015': ('#2271B3', (51.13, -12.69, -34.21), 'Sky blue'),
        'RAL5017': ('#063971', (40.40, -10.67, -32.0), 'Traffic blue'),
        'RAL5018': ('#3F888F', (55.13, -27.27, -8.47), 'Turquoise blue'),
        'RAL5019': ('#1B5583', (41.18, -9.97, -25.87), 'Capri blue'),
        'RAL5020': ('#1D334A', (32.30, -13.01, -9.39), 'Ocean blue'),
        'RAL5021': ('#256D7B', (47.15, -29.26, -9.32), 'Water blue'),
        'RAL5022': ('#252850', (29.61, 7.97, -21.50), 'Night blue'),
        'RAL5023': ('#49678D', (47.64, -2.96, -21.18), 'Distant blue'),
        'RAL5024': ('#5D9B9B', (60.50, -9.53, -17.38), 'Pastel blue'),
        'RAL5025': ('#2A6478', (35.93, -11.81, -16.28), 'Pearl gentian blue'),
        'RAL5026': ('#102C54', (16.00, 7.84, -29.10), 'Pearl night blue'),
        # Green
        'RAL6000': ('#316650', (48.70, -20.58, 4.64), 'Patina green'),
        'RAL6001': ('#287233', (43.86, -23.57, 18.31), 'Emerald green'),
        'RAL6002': ('#2D572C', (39.87, -19.39, 16.95), 'Leaf green'),
        'RAL6003': ('#424632', (39.25, -4.36, 10.17), 'Olive green'),
        'RAL6004': ('#1F3A3D', (33.40, -13.17, -3.07), 'Blue green'),
        'RAL6005': ('#2F4538', (32.26, -13.69, 2.85), 'Moss green'),
        'RAL6006': ('#3E3B32', (33.04, -1.11, 4.17), 'Grey olive'),
        'RAL6007': ('#343B29', (30.42, -3.85, 4.77), 'Bottle green'),
        'RAL6008': ('#39352A', (29.82, -0.67, 4.34), 'Brown green'),
        'RAL6009': ('#31372B', (29.81, -5.74, 3.12), 'Fir green'),
        'RAL6010': ('#35682D', (46.05, -20.46, 22.24), 'Grass green'),
        'RAL6011': ('#587246', (53.24, -11.61, 14.48), 'Reseda green'),
        'RAL6012': ('#343E40', (31.94, -4.36, -0.46), 'Black green'),
        'RAL6013': ('#6C7156', (52.30, -2.08, 14.26), 'Reed green'),
        'RAL6014': ('#47402E', (33.84, 0.46, 6.15), 'Yellow olive'),
        'RAL6015': ('#3B3C36', (31.93, -1.44, 2.99), 'Black olive'),
        'RAL6016': ('#1E5945', (42.92, -32.22, 6.72), 'Turquoise green'),
        'RAL6017': ('#4C9141', (52.33, -23.24, 26.15), 'May green'),
        'RAL6018': ('#57A639', (59.83, -32.96, 37.72), 'Yellow green'),
        'RAL6019': ('#BDECB6', (81.42, -12.57, 13.50), 'Pastel green'),
        'RAL6020': ('#2E3A23', (34.77, -5.82, 6.23), 'Chrome green'),
        'RAL6021': ('#89AC76', (63.69, -11.28, 14.13), 'Pale green'),
        'RAL6022': ('#25221B', (30.43, 0.54, 5.62), 'Olive drab'),
        'RAL6024': ('#308446', (51.81, -38.02, 15.50), 'Traffic green'),
        'RAL6025': ('#3D642D', (47.45, -13.45, 21.37), 'Fern green'),
        'RAL6026': ('#015D52', (39.25, -29.43, 0.67), 'Opal green'),
        'RAL6027': ('#84C3BE', (72.80, -19.82, -3.62), 'Light green'),
        'RAL6028': ('#2C5545', (38.15, -12.86, 3.82), 'Pine green'),
        'RAL6029': ('#20603D', (44.18, -39.06, 15.73), 'Mint green'),
        'RAL6032': ('#317F43', (50.67, -33.25, 14.76), 'Signal green'),
        'RAL6033': ('#497E76', (54.93, -20.4, -2.06), 'Mint turquoise'),
        'RAL6034': ('#7FB5B5', (69.16, -15.95, -5.10), 'Pastel turquoise'),
        'RAL6035': ('#1C542D', (29.14, -29.19, 16.35), 'Pearl green'),
        'RAL6036': ('#193737', (33.97, -29.04, 0.68), 'Pearl opal green'),
        'RAL6037': ('#008F39', (53.49, -46.77, 34.32), 'Pure green'),
        'RAL6038': ('#00BB2D', (63.64, -80.23, 54.00), 'Luminous green'),
        # Grey
        'RAL7000': ('#78858B', (58.32, -3.14, -4.71), 'Squirrel grey'),
        'RAL7001': ('#8A9597', (63.81, -2.22, -4.05), 'Silver grey'),
        'RAL7002': ('#7E7B52', (54.51, -0.09, 10.69), 'Olive grey'),
        'RAL7003': ('#6C7059', (52.32, -1.18, 6.92), 'Moss grey'),
        'RAL7004': ('#969992', (65.77, 0.20, -0.81), 'Signal grey'),
        'RAL7005': ('#646B63', (50.00, -1.55, 0.82), 'Mouse grey'),
        'RAL7006': ('#6D6552', (48.53, 2.15, 7.57), 'Beige grey'),
        'RAL7008': ('#6A5F31', (45.91, 3.34, 17.92), 'Khaki grey'),
        'RAL7009': ('#4D5645', (43.19, -2.43, 3.87), 'Green grey'),
        'RAL7010': ('#4C514A', (42.69, -2.09, 2.04), 'Tarpaulin grey'),
        'RAL7011': ('#434B4D', (41.52, -1.68, -2.72), 'Iron grey'),
        'RAL7012': ('#4E5754', (44.34, -1.77, -1.71), 'Basalt grey'),
        'RAL7013': ('#464531', (39.21, 0.59, 6.33), 'Brown grey'),
        'RAL7015': ('#434750', (40.50, -0.25, -3.40), 'Slate grey'),
        'RAL7016': ('#293133', (33.84, -1.33, -2.83), 'Anthracite grey'),
        'RAL7021': ('#23282B', (30.65, -0.43, -1.22), 'Black grey'),
        'RAL7022': ('#332F2C', (37.75, -0.07, 2.23), 'Umbra grey'),
        'RAL7023': ('#686C5E', (55.60, -1.45, 4.52), 'Concrete grey'),
        'RAL7024': ('#474A51', (36.97, -0.13, -3.32), 'Graphite grey'),
        'RAL7026': ('#2F353B', (34.71, -3.02, -2.48), 'Granite grey'),
        'RAL7030': ('#8B8C7A', (61.31, -0.26, 4.53), 'Stone grey'),
        'RAL7031': ('#474B4E', (47.83, -2.96, -4.01), 'Blue grey'),
        'RAL7032': ('#B8B799', (73.39, -0.93, 8.09), 'Pebble grey'),
        'RAL7033': ('#7D8471', (56.78, -3.36, 6.32), 'Cement grey'),
        'RAL7034': ('#8F8B66', (59.68, -0.10, 12.74), 'Yellow grey'),
        'RAL7035': ('#D7D7D7', (81.29, -1.24, 0.79), 'Light grey'),
        'RAL7036': ('#7F7679', (63.49, 1.27, 0.78), 'Platinum grey'),
        'RAL7037': ('#7D7F7D', (55.30, -0.46, 0.22), 'Dusty grey'),
        'RAL7038': ('#B5B8B1', (72.97, -1.50, 2.97), 'Agate grey'),
        'RAL7039': ('#6C6960', (47.86, 0.17, 4.0), 'Quartz grey'),
        'RAL7040': ('#9DA1AA', (66.63, -1.17, -2.82), 'Window grey'),
        'RAL7042': ('#8D948D', (62.58, -1.51, -0.21), 'Traffic grey A'),
        'RAL7043': ('#4E5452', (40.23, -1.28, 0.0), 'Traffic grey B'),
        'RAL7044': ('#CAC4B0', (74.66, -0.04, 5.08), 'Silk grey'),
        'RAL7045': ('#909090', (62.71, -1.24, -2.14), 'Telegrey 1'),
        'RAL7046': ('#82898F', (57.75, -1.60, -3.0), 'Telegrey 2'),
        'RAL7047': ('#D0D0D0', (81.43, 0.01, 0.10), 'Telegrey 4'),
        'RAL7048': ('#898176', (54.55, -0.45, 7.59), 'Pearl mouse grey'),
        # Brown
        'RAL8000': ('#826C34', (46.78, 7.55, 28.72), 'Green brown'),
        'RAL8001': ('#955F20', (50.62, 17.02, 31.31), 'Ochre brown'),
        'RAL8002': ('#6C3B2A', (41.88, 14.45, 13.31), 'Signal brown'),
        'RAL8003': ('#734222', (42.56, 15.59, 21.67), 'Clay brown'),
        'RAL8004': ('#8E402A', (43.78, 22.83, 20.22), 'Copper brown'),
        'RAL8007': ('#59351F', (38.99, 12.62, 17.08), 'Fawn brown'),
        'RAL8008': ('#6F4F28', (41.10, 10.45, 19.33), 'Olive brown'),
        'RAL8011': ('#5B3A29', (33.98, 10.04, 10.97), 'Nut brown'),
        'RAL8012': ('#592321', (34.39, 17.06, 10.17), 'Red brown'),
        'RAL8014': ('#382C1E', (31.99, 4.77, 7.71), 'Sepia brown'),
        'RAL8015': ('#633A34', (33.52, 15.02, 9.25), 'Chestnut brown'),
        'RAL8016': ('#4C2F27', (31.19, 9.63, 7.56), 'Mahogany brown'),
        'RAL8017': ('#45322E', (30.60, 5.99, 4.34), 'Chocolate Brown'),
        'RAL8019': ('#403A3A', (31.46, 2.12, 1.10), 'Grey brown'),
        'RAL8022': ('#212121', (25.08, 1.18, 0.67), 'Black brown'),
        'RAL8023': ('#A65E2E', (49.37, 24.91, 30.25), 'Orange brown'),
        'RAL8024': ('#79553D', (42.93, 11.88, 15.90), 'Beige brown'),
        'RAL8025': ('#755C48', (44.00, 7.95, 11.73), 'Pale brown'),
        'RAL8028': ('#4E3B31', (34.19, 5.72, 8.58), 'Terra brown'),
        'RAL8029': ('#763C28', (35.06, 25.58, 27.32), 'Pearl copper'),
        # White & Black
        'RAL9001': ('#FDF4E3', (90.40, 0.66, 6.64), 'Cream'),
        'RAL9002': ('#E7EBDA', (86.05, -0.89, 4.21), 'Grey white'),
        'RAL9003': ('#F4F4F4', (94.13, -0.55, 0.81), 'Signal white'),
        'RAL9004': ('#282828', (28.66, 0.24, -0.66), 'Signal black'),
        'RAL9005': ('#0A0A0A', (25.33, 0.13, -0.16), 'Jet black'),
        'RAL9006': ('#A5A5A5', (67.77, -0.58, 0.76), 'White aluminium'),
        'RAL9007': ('#8F8F8F', (59.39, 0.01, 2.34), 'Grey aluminium'),
        'RAL9010': ('#FFFFFF', (94.57, -0.47, 4.14), 'Pure white'),
        'RAL9011': ('#1C1C1C', (26.54, -0.05, -1.13), 'Graphite black'),
        'RAL9016': ('#F6F6F6', (95.26, -0.76, 2.11), 'Traffic white'),
        'RAL9017': ('#1E1E1E', (27.25, 0.44, 0.51), 'Traffic Black'),
        'RAL9018': ('#D7D7D7', (82.71, -2.06, 1.93), 'Papyrus white'),
        'RAL9022': ('#9C9C9C', (65.38, -0.43, 0.34), 'Pearl light grey'),
        'RAL9023': ('#828282', (57.32, -0.31, -0.98), 'Pearl dark grey'),
    }


class ColRAL(RefRAL, cCIELab):
    """ RAL set of colors class
    Inherits from ColCIELab & RefRAL """
    # TODO: add inherited class RGB or HEX
    # TODO: recreate method to get data in dict (from self)
    def __init__(self, idral='RAL9010', *args, **kwargs):    # default: Pure White (unless other spaces)
        """ Init idRAL & L*ab values from RAL string id passed as argument
        note: default init value corresponds to White, not black for RAL """
        self.idRAL = idral

        self.dfields_RAL = dict(zip(range(len(self.lfields)), self.lfields))  # make dict from list

        self.getHEX_from_id = lambda i: self.ref_colRALclassic.get(i)[0]
        self.getxy_from_id = lambda i: self.ref_colRALclassic.get(i)[1]
        self.getName_from_id = lambda i: self.ref_colRALclassic.get(i)[2]

        cCIELab.__init__(self, *self.get('Lab', idral), *args, **kwargs)
        self.type = 'RAL'  # can be used instead of isinstance on an object

    def get(self, typ, srch='self'):
        """ get data from RAL colors dict
        :param typ: row in dict (from lfields_RAL)
        :param srch: to search in dict keys
        :return: either string ot tuple of the type passed as parameter """
        if srch == 'self':
            srch = self.idRAL

        if not isinstance(typ, str):
            pass
        elif typ == 'id':
            return self.idRAL
        else:
            try:
                srch = srch.upper()
                if srch in self.ref_colRALclassic:
                    tup = self.ref_colRALclassic.get(srch)
                    for idx, val in enumerate(self.lfields_RAL):
                        if val == typ:
                            return tup[idx - 1]
            except KeyError:
                print("Key not found!!!")
                pass


if __name__ == "__main__":
    col_RAL = ColRAL('RAL9001')
    print(col_RAL)
    print(str(col_RAL))

    print("")
    print(col_RAL.searchref_RAL('HEX', 'pearl light grey'))

    print(col_RAL.searchref_RAL('Name', '#8F8F8F'))

    print("")
    print(col_RAL.get('id'))
    print(col_RAL.get('HEX'))
    print(col_RAL.get('Lab'))
    print(col_RAL.get('Name'))

    print("")
    print("still needs to print ID from something else in the dict")
    print(col_RAL.get('HEX', 'RAL8001'))
    print(col_RAL.get('Lab', 'RAL8001'))
    print(col_RAL.get('Name', 'RAL8001'))
