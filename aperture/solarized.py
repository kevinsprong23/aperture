"""
function to return hex strings of solarized palette colors
for plot options

color scheme from Solarized by Ethan Schoonover
"""
from __future__ import print_function

def solarized(color_str):
    """
    return dictionary value if it exists, otherwise raise KeyError
    """
    
    sol_colors = {
        'base03':   '#002b36',
        'base02':   '#073642',
        'base01':   '#586e75',
        'base00':   '#657b83',
        'base0':    '#839496',
        'base1':    '#93a1a1',
        'base2':    '#eee8d5',
        'base3':    '#fdf6e3',
        'yellow':   '#b58900',
        'orange':   '#cb4b16',
        'red':      '#dc322f',
        'magenta':  '#d33682',
        'violet':   '#6c71c4',
        'blue':     '#268bd2',
        'cyan':     '#2aa198',
        'green':    '#859900'
    }
    
    try:
        return sol_colors[color_str]
    except KeyError:
        print(str(color_str) + ' is not a solarized color.')
        raise