#! /usr/bin/python3
# *-* coding: utf-8 *-*
"""13return_func_in_func
@Author: yongliang
@License: MIT
"""


def hi(name="yasoob"):
    def greet():
        return "now you are in the greet() function"

    def welcome():
        return "now you are in the welcom() function"

    if name == "yasoob":
        return greet
    else:
        return welcome


a = hi()
print(a)
print(a())