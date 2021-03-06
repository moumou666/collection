# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 19:44:15 2020
@author: Zane
"""
# width = 50,height = 40
walls=[{"x":0,"y":430},
       {"x":50,"y":430},
       {"x":100,"y":430},
       {"x":145,"y":385},
       {"x":195,"y":385},
       {"x":245,"y":385},
       {"x":285,"y":345},
       {"x":335,"y":345},
       {"x":385,"y":345},
       {"x":435,"y":345},
       {"x":470,"y":295},
       {"x":515,"y":295},
       {"x":515,"y":345},
       {"x":560,"y":385},
       {"x":610,"y":385},
       {"x":655,"y":255},
       {"x":695,"y":255},
       {"x":655,"y":430},
       {"x":705,"y":430},
       {"x":755,"y":430},
       {"x":805,"y":430},
       {"x":855,"y":430},
       {"x":885,"y":430},
       {"x":800,"y":300},
       {"x":850,"y":300},
       {"x":900,"y":300},
       {"x":935,"y":300},
       {"x":985,"y":385},
       {"x":1035,"y":385},
       {"x":1080,"y":340},
       {"x":1130,"y":340},
       {"x":1180,"y":340},
       {"x":1220,"y":300},
       {"x":1230,"y":340},
       {"x":1265,"y":300},
       {"x":1265,"y":340},
       {"x":1265,"y":385},
       {"x":1315,"y":385},
       {"x":935,"y":470},
       {"x":985,"y":470},
       {"x":1035,"y":470},
       {"x":1085,"y":470},
       {"x":1135,"y":470},
       {"x":1185,"y":470},
       {"x":1235,"y":470},
       {"x":1285,"y":470},
       {"x":1335,"y":470},
       {"x":1385,"y":470},
       {"x":1435,"y":470},
       {"x":1455,"y":470},
       {"x":1365,"y":385},
       {"x":1405,"y":385},
       {"x":1412,"y":342},
       {"x":1462,"y":342},
       {"x":1512,"y":342},
       {"x":1562,"y":342},
       {"x":1612,"y":342},
       {"x":1625,"y":342},
       {"x":1675,"y":470},
       {"x":1625,"y":470},
       {"x":1575,"y":470},
       {"x":1555,"y":470},
       {"x":1725,"y":430},
       {"x":1775,"y":385},
       {"x":1775,"y":300},
       {"x":1725,"y":300},
       {"x":1810,"y":300},
       {"x":1820,"y":430},
       {"x":1870,"y":430},
       {"x":1920,"y":430},
       {"x":1970,"y":430},
       {"x":1918,"y":340},
       {"x":2015,"y":385},
       {"x":2065,"y":385},
       {"x":2110,"y":342},
       {"x":2160,"y":342},
       {"x":2210,"y":342},
       {"x":2260,"y":342},
       {"x":2310,"y":342},
       {"x":2360,"y":342},
       {"x":2410,"y":342},
       {"x":2460,"y":342},
       {"x":2510,"y":342},
       {"x":2540,"y":297},
       {"x":2590,"y":297},
       {"x":2640,"y":297},
       {"x":2680,"y":297},
       {"x":2685,"y":255},
       {"x":2735,"y":255},
       {"x":2775,"y":255},
       {"x":2735,"y":340},
       {"x":2785,"y":340},
       {"x":2835,"y":340},
       {"x":2885,"y":340},
       {"x":2885,"y":210},
       {"x":2915,"y":210},
       {"x":2935,"y":340},
       {"x":2985,"y":340},
       {"x":3015,"y":340},
       {"x":3065,"y":340},
       {"x":3115,"y":340},
       {"x":3030,"y":168},
       {"x":3060,"y":168},
       {"x":3170,"y":125},
       {"x":3215,"y":125},
       {"x":3240,"y":125},
       {"x":3165,"y":340},
       {"x":3215,"y":340},
       {"x":3265,"y":340},
       {"x":3300,"y":298},
       {"x":3350,"y":298},
       {"x":3380,"y":298},
       {"x":3305,"y":340},
       {"x":3355,"y":340},
       {"x":3405,"y":340},
       {"x":3455,"y":340},
       {"x":3505,"y":340},
       {"x":3555,"y":340},
       {"x":3605,"y":340},
       {"x":3655,"y":340},
       {"x":3705,"y":340},
       {"x":3755,"y":340},
       {"x":3805,"y":340},
       {"x":3840,"y":298},
       {"x":3885,"y":255},
       {"x":3935,"y":255},
       {"x":3985,"y":255},
       {"x":4050,"y":255},
       {"x":4050,"y":212},
       {"x":4050,"y":295},
       {"x":4105,"y":340},
       {"x":4155,"y":340},
       {"x":4205,"y":340},
       {"x":4255,"y":340},
       {"x":4305,"y":340},
       {"x":4355,"y":340},
       {"x":4370,"y":295},
       {"x":4415,"y":255},
       {"x":4460,"y":210},
       {"x":4465,"y":255},
       {"x":4515,"y":255},
       {"x":4540,"y":255},
       {"x":4455,"y":295},
       {"x":4505,"y":340},
       {"x":4555,"y":340},
       {"x":4605,"y":340},
       {"x":4655,"y":340},
       {"x":4705,"y":340},
       {"x":4725,"y":300},
       {"x":4725,"y":255},
       {"x":4680,"y":255},
       {"x":4645,"y":255},
       {"x":4755,"y":340},
       {"x":4805,"y":340},
       {"x":4855,"y":340},
       {"x":4905,"y":340},
       {"x":4955,"y":340},
       {"x":4775,"y":210},
       {"x":4825,"y":210},
       {"x":4875,"y":210},
       {"x":4900,"y":210},
       {"x":4950,"y":255},
       {"x":5000,"y":340},
       {"x":5050,"y":340},
       {"x":5100,"y":340},
       {"x":5150,"y":340},
       {"x":5200,"y":340},
       {"x":5250,"y":340},
       {"x":5300,"y":340},
       {"x":5350,"y":340},
       {"x":5365,"y":295},
       {"x":5410,"y":255},
       {"x":5450,"y":255}]
