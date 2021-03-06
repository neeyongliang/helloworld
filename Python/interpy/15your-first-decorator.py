#! /usr/bin/python3
# *-* coding: utf-8 *-*
"""15your_first_decorator
@Author: yongliang
@License: MIT
"""
from functools import wraps


def a_new_decorator(a_func):
    def wrap_the_function():
        print("I am doing some boring work before executing a_fun()")

        a_func()

        print("I am doing some boring work after executing a_func()")

    return wrap_the_function


def a_function_requiring_decoration():
    print("I am the function which needs some decoration to remove foul smell")


a_function_requiring_decoration()
print("------------------------")
a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)
a_function_requiring_decoration()
print("------------------------")


def a_new_decorator2(a_func):
    @wraps(a_func)
    def wrap_the_function():
        print("I am doing some broing work before executing a_func()")
        a_func()
        print("I am doing some boring work after executing a_func()")
    return wrap_the_function


@a_new_decorator2
def a_function_requiring_decoration():
    """Hey yo! Decorate me!"""
    print("I am the function which needs some decoration to remove my"
          " foul smell")


print(a_function_requiring_decoration.__name__)