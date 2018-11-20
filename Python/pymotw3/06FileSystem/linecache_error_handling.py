#! /usr/bin/python3
# *-* coding: utf-8 *-*
"""linecache_error_handling
@Author: wikinee
@License: MIT
@Date: Nov.15 2018
"""
import linecache
from linecache_data  import *

print("\n===== file: linecache_out_of_range.py =====")
filename = make_template()

# The cache always returns a string, and uses
# an empty string to indicate a line which does
# not exists.
not_there = linecache.getline(filename, 500)
print('NOT THERE: {!r} includes {} characters'.format(not_there, len(not_there)))

print("\n===== file: linecache_missing_file.py =====")
