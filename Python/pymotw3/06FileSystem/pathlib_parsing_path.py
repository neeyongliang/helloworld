#! /usr/bin/python3
# *-* coding: utf-8 *-*
"""pathlib_parsing_path
@Author: yongliang
@License: MIT
@Date: Nov.14 2018
"""
import pathlib

print("===== pathlib_parts.py =====")
p = pathlib.PurePosixPath('/usr/local')
print(p.parts)

print("===== pathlib_parents.py =====")
p = pathlib.PurePosixPath('/usr/local/lib')
print('parent: {}'.format(p.parent))

print('\nhierachy:')
for up in p.parents:
    print(up)

print("===== pathlib_name.py =====")
p = pathlib.PurePosixPath('./ospath_examples.py')
print('{!s:>10} : {}'.format('path', p))
print('{!s:>10} : {}'.format('name', p.name))
print('{!s:>10} : {}'.format('suffix', p.suffix))
print('{!s:>10} : {}'.format('stem', p.stem))
