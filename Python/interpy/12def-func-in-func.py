#! /usr/bin/python3
# *-* coding: utf-8 *-*
"""12def_func_in_func
@Author: wikinee
@License: MIT
"""


def hi(name="yasoob"):
    print("now you are inside the hi() function")

    def greet():
        return "now you are in the greet() function"

    def welcome():
        return "now you are in the welcome() function"

    print(greet())
    print(welcome())
    print("now you are back in the hi() function")

hi()
try:
    greet()
except Exception as e:
    print(e)
