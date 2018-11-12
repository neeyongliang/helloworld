#! /usr/bin/python3
# *-* coding: utf-8 *-*
"""contextlib_exitstack_enter_context
@Author: wikinee
@License: MIT
"""

import contextlib


@contextlib.contextmanager
def make_context(i):
    print('{} entering'.format(i))
    yield
    print('{} exiting'.format(i))


def variable_stack(n, msg):
    with contextlib.ExitStack() as stack:
        for i in range(n):
            stack.enter_context(make_context(i))
        print(msg)


variable_stack(2, 'inside context')
# 0 entering
# 1 entering
# inside context
# 1 exiting
# 0 exiting
