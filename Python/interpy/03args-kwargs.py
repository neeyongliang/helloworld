#! /usr/bin/python3
# *-* coding: utf-8 *-*
"""03args_kwargs
@Author: wikinee
@License: MIT
"""


def test_args_kwargs(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)


print("========")
args = ("two", 3, 5)
test_args_kwargs("two", 3, 5)

print("========")
kwargs = {"arg3": 3, "arg2": "two", "arg1": 5}
test_args_kwargs(**kwargs)
