#! /usr/bin/python3
# *-* coding: utf-8 *-*
"""fnmatch_filtering
@Author: wikinee
@License: MIT
@Date: Nov.15 2018
"""
import os
import fnmatch
import pprint

print("\n===== file: fnmatch_filter.py =====")
pattern = 'fnmatch_*.py'
print('Pattern :', pattern)

files = list(sorted(os.listdir('.')))

print('\nFiles   :')
pprint.pprint(files)

print('\nMatches :')
pprint.pprint(fnmatch.filter(files, pattern))
