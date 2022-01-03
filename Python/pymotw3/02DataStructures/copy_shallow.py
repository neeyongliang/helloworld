#! /usr/bin/python3
# *-* coding: utf-8 *-*
"""copy_shallow
@Author: yongliang
@License: MIT
"""

import copy
import functools


@functools.total_ordering
class MyClass:

    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

    def __gt__(self, other):
        return self.name > other.name


a = MyClass('a')
my_list = [a]
print('\n---- shallow ----')
dup = copy.copy(my_list)

print('             my_list:', my_list)
print('                 dup:', dup)
print('      dup is my_list:', (dup is my_list))  # False
print('      dup == my_list:', (dup == my_list))
print('dup[0] is my_list[0]:', (dup[0] is my_list[0]))
print('dup[0] == my_list[0]:', (dup[0] == my_list[0]))

print('\n---- deep ----')
deep_dup = copy.deepcopy(my_list)

print('                  my_list:', my_list)
print('                 deep_dup:', deep_dup)
print('      deep_dup is my_list:', (deep_dup is my_list))  # False
print('      deep_dup == my_list:', (deep_dup == my_list))
print('deep_dup[0] is my_list[0]:', (deep_dup[0] is my_list[0]))  # False
print('deep_dup[0] == my_list[0]:', (deep_dup[0] == my_list[0]))

print('\n---- hooks ----')


@functools.total_ordering
class MyClass2:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

    def __gt__(self, other):
        return self.name > other.name

    def __copy__(self):
        print('__copy__()')
        return MyClass2(self.name)

    def __deepcopy__(self, memo):
        print('__deepcopy__()')
        return MyClass2(copy.deepcopy(self.name, memo))

a = MyClass2('a')
sc = copy.copy(a)
dc = copy.deepcopy(a)