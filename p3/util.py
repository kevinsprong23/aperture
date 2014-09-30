"""
basic utilities
"""

import math

def increment(d, key, val=1):
    """
    increment dict d at key by amount val
    no need to return since d is mutable
    """
    if key in d:
        d[key] += val
    else:
        d[key] = val


def get_sig_digits(x):
    """
    get number of significant digits to pass to round function
    """
    return 1 if x >= 1 else len(str(x)) - 2


def floor_nearest(x, dx=1):
    """
    floor a number to within a given rounding accuracy
    """
    precision = get_sig_digits(dx)
    return round(math.floor(float(x) / dx) * dx, precision)


def frange(x, y, jump=1):
    """
    range for floats
    """
    precision = get_sig_digits(jump)
    while x < y:
        yield round(x, precision)
        x += jump
