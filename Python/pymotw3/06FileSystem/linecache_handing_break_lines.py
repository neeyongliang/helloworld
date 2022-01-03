#! /usr/bin/python3
# *-* coding: utf-8 *-*
"""linecache_handing_break_lines
@Author: yongliang
@License: MIT
@Date: Nov.15 2018
"""
import linecache
from linecache_data import *

file_name = make_template()

# Blank lines include the newline
print('BLANK : {!r}'.format(linecache.getline(file_name, 8)))