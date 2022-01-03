#! /usr/bin/python3
# *-* coding: utf-8 *-*
"""21global-return
@Author: yongliang
@License: MIT
"""


def add(value1, value2):
    # 尽量避免使用global
    global value
    result = value1 + value2
    value = value1 + value2

try:
    add(2, 4)
    print(value)
    print(result)
except Exception as e:
    print(e)

