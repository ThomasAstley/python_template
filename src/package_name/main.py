#!/bin/env python
# License: GNU GPL version 3

import sys

if '--' in sys.argv: 
    ARGV = sys.argv[1:sys.argv.index('--')] 
else:
    ARGV = sys.argv[1:]
