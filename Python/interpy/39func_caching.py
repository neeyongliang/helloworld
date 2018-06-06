#! /usr/bin/python3
# *-* coding: utf-8 *-*
"""39func_caching
@Author: wikinee
@License: MIT
"""
from functools import lru_cache
print("--- python 3 version ---")


@lru_cache(maxsize=32)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)


print([fib(n) for n in range(10)])
fib.cache_clear()
