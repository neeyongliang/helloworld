#! /usr/bin/python3
# *-* coding: utf-8 *-*
"""fnmatch_fnmatch.py
@Author: yongliang
@License: MIT
@Date: Nov.14 2018
"""

import fnmatch
import os

# Case-sensitive
print("\n===== file: fnmatch_fnmatch.py =====")

pattern = 'fnmatch_*.py'
print('Pattern :', pattern)
print()

files = os.listdir('.')
for name in sorted(files):
    print('Filename: {:<55} {}'.format(
        name, fnmatch.fnmatch(name, pattern)))

print("\n===== file: fnmatch_fnmatchcase.py =====")

pattern = 'FNMATCH_*.PY'
print('Pattern2 :', pattern)
print()

files = os.listdir('.')
for name in sorted(files):
    print('Filename: {:<55} {}'.format(
        name, fnmatch.fnmatchcase(name, pattern)))
