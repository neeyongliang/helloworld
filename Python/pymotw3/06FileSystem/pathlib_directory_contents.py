#! /usr/bin/python3
# *-* coding: utf-8 *-*
"""pathlib_directory_contents
@Author: yongliang
@License: MIT
@Date: Nov.14 2018
"""

import pathlib

print("===== file: pathlib_iterdir.py =====")
p = pathlib.Path('.')

print('\n==\n')
for f in p.iterdir():
    print(f)

print("===== file: pathlib_glob.py =====")
p = pathlib.Path('.')
for f in p.glob('*.py'):
    print(f)

print("===== file: pathlib_rglob.py =====")
p = pathlib.Path('.')

for f in p.rglob('pathlib_*.py'):
    print(f)