#! /usr/bin/python3
# *-* coding: utf-8 *-*
"""04get_info
@Author: yongliang
@License: MIT
"""


class MyClass(object):
    """Define Class
    MyClass is use for test monkey patching
    """
    def get_info(self, *args):
        """get_info method"""
        print("This is MyClass get_info")


def get_info(self, *args):
    print("Test data")


MyClass.get_info = get_info
m = MyClass()
m.get_info()
