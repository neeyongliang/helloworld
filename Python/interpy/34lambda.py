#! /usr/bin/python3
# *-* coding: utf-8 *-*
"""34lambda
@Author: wikinee
@License: MIT
"""

add = lambda x, y: x + y
print(add(3, 5))

a = [(1, 2), (4, 1), (9, 10), (13, -3)]
a.sort(key=lambda x: x[1])
print(a)

try:
    data = zip(list1, list2)
    data = sorted(data)
    list1, list2 = map(lambda t: list(t), zip(*data))
except Exception as e:
    print(e)