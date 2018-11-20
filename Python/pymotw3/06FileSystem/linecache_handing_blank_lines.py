#! /usr/bin/python3
# *-* coding: utf-8 *-*
"""linecache_handing_blank_lines
@Author: wikinee
@License: MIT
@Date: Nov.20 2018
"""

import linecache
from linecache_data import *

filename = make_template()

# Blank lines include the newline
print('BLANK : {!r}'.format(linecache.getline(filename, 8)))

cleanup(filename)