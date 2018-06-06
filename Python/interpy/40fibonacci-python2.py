#! /usr/bin/python2
# *-* coding: utf-8 *-*
"""40fibonacci-python2
@Author: wikinee
@License: MIT
"""
from functools import wraps


def memoize(function):
    memo = {}

    @wraps(function)
    def wrapper(*args):
        if args in memo:
            return memo[args]
        else:
            rv = function(*args)
            memo[args] = rv
            return rv
    return wrapper


@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci(25)
