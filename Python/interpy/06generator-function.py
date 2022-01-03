#! /usr/bin/python3
# *-* coding: utf-8 *-*
"""06generator_function
@Author: yongliang
@License: MIT
"""


def generator_function():
    for i in range(10):
        yield i


def fibon(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b


for item in generator_function():
    print(item)

for x in fibon(100):
    print(x)