'''A module for convertion and exceptional handling'''

import sys

def convert(s):
    '''Convertion to an integer'''
    if not isinstance(s, str):
        raise TypeError("Argument must be a string")
    try:
        x = int(s)
        print("conversion succeeded : x =", x)
    except (ValueError, TypeError) as e:
        print("convertion error: {}", str(e))
        raise
    return x
