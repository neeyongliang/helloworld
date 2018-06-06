#! /usr/bin/python3
# *-* coding: utf-8 *-*
"""18logging
@Author: wikinee
@License: MIT
"""

from functools import wraps

def logit(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__ + " was called")
        return func(*args, **kwargs)
    return with_logging


@logit
def addition_func(x):
    """Do some math."""
    return x + x


result = addition_func(4)
