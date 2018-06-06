#! /usr/bin/python3
# *-* coding: utf-8 *-*
"""38coroutines
@Author: wikinee
@License: MIT
"""


def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b


for i in fib():
    if i < 10:
        print(i)


def grep(pattern):
    print("Searching for", pattern)
    while True:
        line = (yield)
        if pattern in line:
            print(line)


search = grep('coroutine')
next(search)
# Output: Searching for coroutine
search.send("I love you")
search.send("Don't you love me?")
search.send("I love coroutine instead!")
# Output: I love coroutine instead!
search = grep('coroutine')
search.close()
