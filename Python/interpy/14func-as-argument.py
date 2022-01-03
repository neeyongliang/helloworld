#! /usr/bin/python3
# *-* coding: utf-8 *-*
"""14func_as_argument
@Author: yongliang
@License: MIT
"""


def hi():
    return "hi yasoob!"


def do_something_before_hi(func):
    print("I am doing some boring work before executing hi()")
    print(func())


do_something_before_hi(hi)