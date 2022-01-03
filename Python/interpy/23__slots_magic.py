#! /usr/bin/python3
# *-* coding: utf-8 *-*
"""23__slots_magic
@Author: yongliang
@License: MIT
"""


class MyClass(object):
    __slots__ = ['name', 'identifier']

    def __init__(self, name, identifier):
        self.name = name
        self.identifier = identifier
        # ...

