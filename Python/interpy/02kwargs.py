#! /usr/bin/python3
# *-* coding: utf-8 *-*
"""02kwargs
@Author: wikinee
@License: MIT
"""


def greet_me(**kwargs):
    for key, value in kwargs.items():
        print("{0} == {1}".format(key, value))


greet_me(name="yasoob")