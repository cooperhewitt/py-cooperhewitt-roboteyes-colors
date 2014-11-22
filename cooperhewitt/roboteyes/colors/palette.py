#!/usr/bin/env python

import roygbiv
import cooperhewitt.swatchbook as swatchbook

def extract_roygbiv(path, reference):

    ref = swatchbook.load_palette(reference)

    roy = roygbiv.Roygbiv(path)
    average = roy.get_average_hex()
    palette = roy.get_palette_hex()
    
    def prep(hex):
        c_hex, c_name = ref.closest(hex)        
        return {'color': hex, 'closest': c_hex}

    average = prep(average)
    palette = map(prep, palette)
        
    return {
        'reference-closest': reference,
        'average': average,
        'palette': palette
    }

if __name__ == '__main__':

    import sys
    path = sys.argv[1]

    print extract_roygbiv(path, 'css4')
