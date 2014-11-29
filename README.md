# py-cooperhewitt-roboteyes-colors

Functions for extracting color palettes from an image.

## Usage

    import sys
    import pprint
    import cooperhewitt.roboteyes.colors.palette as palette

    path = sys.argv[1]

    # Where ref is a valid cooperhewitt.swatchbook color palette
    ref = 'css4'

    rsp = palette.extract_roygbiv(path, ref)
    print pprint.pformat(rsp)

## See also

* http://labs.cooperhewitt.org/2013/giv-do/
* https://github.com/givp/RoyGBiv
* https://github.com/cooperhewitt/py-cooperhewitt-swatchbook
