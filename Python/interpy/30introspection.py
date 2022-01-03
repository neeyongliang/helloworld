#! /usr/bin/python3
# *-* coding: utf-8 *-*
"""30introspection
@Author: yongliang
@License: MIT
"""

import inspect

print("--- dir ---")
my_list = [1, 2, 3]
print(dir(my_list))

print("--- type ---")
print(type(''))
print(type([]))
print(type({}))
print(type(dict))
print(type(3))

print("--- inspect ---")
print(inspect.getmembers(str))
