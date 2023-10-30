#!/bin/env python
# License: GNU GPL version 3

import sys

def process_array(array):
    if '--' in array: 
        result = array[1:array.index('--')] 
    else:
        result = array[1:]

    return result

