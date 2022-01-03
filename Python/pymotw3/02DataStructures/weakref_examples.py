#! /usr/bin/python3
# *-* coding: utf-8 *-*
"""weakref_examples
@Author: yongliang
@License: MIT
"""

import weakref

print('\n---- ref ----')


class ExpensiveObject():
    def __del__(self):
        print('(Deleting {})'.format(self))


obj = ExpensiveObject()
r = weakref.ref(obj)

print('obj:', obj)
print('ref:', r)
print('r():', r())

print('deleting obj')
del obj
print('r():', r())


print('\n---- callbacks ----')


def callback(reference):
    """Invoked when referenced object is deleted"""
    print('callback({!r})'.format(reference))


obj = ExpensiveObject()
r = weakref.ref(obj, callback)
print('obj:', obj)
print('ref:', r)
print('r():', r())

print('deleting obj')
del obj
print('r():', r())
