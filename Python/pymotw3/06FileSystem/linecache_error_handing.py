#! /usr/bin/python3
# *-* coding: utf-8 *-*
"""linecache_error_handing
@Author: wikinee
@License: MIT
@Date: Nov.20 2018
"""

import linecache
from linecache_data import *

filename = make_template()

print("\n===== file: linecache_out_of_range.py =====")
# The cache always returns a string, and uses
# an empty string to indicate a line which does
# not exist.
not_there = linecache.getline(filename, 500)
print('NOT THERE: {!r} includes {} characters'.format(
    not_there, len(not_there)))

cleanup(filename)

print("\n===== file: linecache_missing_file.py =====")
# Errors are even hidden if linecache cannot find the file
no_such_file = linecache.getline(
    'this_file_does_not_exist.txt', 1,
)

print('NO FILE: {!r}'.format(no_such_file))