# SMFSWcolor
Author: SMFSW

All the work involved here is dedicated to my beloved very special kitty Nietzschee
who brought some harmony in my life (miss you so much).

Copyright (c) 2016-2018 SMFSW


This package includes various color schemes classes, low level conversions and transformation functions

## Classes:
- RefYYY: data dict classes
- ColXXX: color classes
- Color: multi-space color class

## Low Level Algorithms:
- colorConv.py: raw conversions
- colorConvCIE.py: CIE 1931/1976 coordinates conversions
- colorConvGamma.py: Gamma expand & compress functions
- colorConvTemperature.py: Temperature calculations, conversions
- colorFuncs.py: raw transformations, manipulations
- colorScenarios.py: fading & scenarios calculations in different color models

## GUI Interface:
Commit of these interfaces will follow along with updates
- ColorConverter.pyw
- ColorConverter_GUI.pyw

# Basic usage:
- Multi space color:
  - import colMulti
  - declare an object of type Color('RGB', 0, 0, 0) with color space and corresponding values
  - use get method on the object with given output space to get converted values
- when the need is only a direct conversion from space to space (close spaces):
  - import colXXX _(XXX corresponding to desired source or destination space depending the need)_
  - Source:
    - declare an object of type colXXX(0, 0, 0) with corresponding values
    - using toYYY method on the object returns the values of the destination space
      - _YYY corresponding to desired destination space_
  - Destination:
    - declare an object of type colXXX()
    - using fromYYY(0, 0, 0) method on the object fills it with the converted values 
      - _YYY(0, 0, 0) corresponding to desired source space with values from that space_

## References and Links:
thanks for the help in making this package
- http://www.brucelindbloom.com/
  - main reference in making this package (some material reproduced with permission)
- www.w3schools.com/colors/colors_converter.asp
