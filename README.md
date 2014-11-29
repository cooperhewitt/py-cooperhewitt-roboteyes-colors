# py-cooperhewitt-roboteyes-colors

## Usage

### Simple

    import sys
    import cooperhewitt.roboteyes.colors.palette as palette

    path = sys.argv[1]
    rsp = palette.extract_roygbiv(path, 'css4')

    print pprint.pformat(rsp)

### Fancy

There is no fancy usage.

## See also

* http://labs.cooperhewitt.org/2013/giv-do/
* https://github.com/givp/RoyGBiv
