#! /usr/bin/python3
# *-* coding: utf-8 *-*
"""linecache_reading_specific_lines
@Author: yongliang
@License: MIT
@Date: Nov.15 2018
"""
import linecache
from linecache_data import *

print("\n===== file: linecache_getline.py =====")
filename = make_template()

# Pick out the same line from source and cache.
# (Notice that linecache counts from 1)
print('SOURCE:')
print('{!r}'.format(lorem.split('\n')[4]))
print()
print('CACHE:')
print('{!r}'.format(linecache.getline(filename, 5)))

cleanup(filename)
