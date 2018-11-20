#! /usr/bin/python3
# *-* coding: utf-8 *-*
"""fnmatch_translating_patterns
@Author: wikinee
@License: MIT
@Date: Nov.15 2018
"""
import fnmatch

print("\n===== file: fnmatch_translate.py =====")

pattern = 'fnmatch_*.py'
print('Pattern :', pattern)
print('Regex   :', fnmatch.translate(pattern))
