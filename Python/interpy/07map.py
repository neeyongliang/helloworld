#! /usr/bin/python3
# *-* coding: utf-8 *-*
"""07map
@Author: yongliang
@License: MIT
"""

items = [1, 2, 3, 4, 5]
# squared = []
# for i in items:
#     squared.append(i**2)
squared = list(map(lambda x: x**2, items))

print(squared)


def multiply(x):
    return (x*x)


def add(x):
    return (x+x)


funcs = [multiply, add]
for i in range(5):
    value = map(lambda x: x(i), funcs)
    # add list function, because python2 return list, python3 return iterator
    print(list(value))