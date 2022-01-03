#! /usr/bin/python3
# *-* coding: utf-8 *-*
"""contextlib_file
@Author: yongliang
@License: MIT
"""

print('\n---- file ----')
with open('/tmp/pymotw.txt', 'wt') as f:
    f.write('contents go here')

# file is automatically closed

print('\n---- api ----')


class Context:
    def __init__(self):
        print('__init__()')

    def __enter__(self):
        print('__enter__()')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('__exit__()')


with Context():
    print('Doing work in the context')