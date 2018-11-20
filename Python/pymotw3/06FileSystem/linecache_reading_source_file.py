#! /usr/bin/python3
# *-* coding: utf-8 *-*
"""linecache_reading_source_file
@Author: wikinee
@License: MIT
@Date: Nov.20 2018
"""

import linecache
import os

# Look for the linecache module, using
# the build in sys.path search
module_line = linecache.getline('linecache_data.py', 3)
print('MODULE:')
print(repr(module_line))

# Look at the linecache module source directly
file_src = linecache.__file__
if file_src.endswith('.pyc'):
    file_src = file_src[:-1]
print('\nFILE:')
with open(file_src, 'r') as f:
    file_line = f.readlines()[2]
print(repr(file_line))