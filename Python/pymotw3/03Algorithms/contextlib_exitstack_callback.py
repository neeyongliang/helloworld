#! /usr/bin/python3
# *-* coding: utf-8 *-*
"""contextlib_exitstack_callback
@Author: yongliang
@License: MIT
"""

import contextlib


def callback(*args, **kwds):
    print('closing callback({}, {})'.format(args, kwds))


with contextlib.ExitStack() as stack:
    stack.callback(callback, 'arg1', 'arg2')
    stack.callback(callback, arg3='val3')

# contextlib_exitstack_callbacks_errors
try:
    with contextlib.ExitStack() as stack:
        stack.callback(callback, 'arg1', 'arg2')
        stack.callback(callback, arg3='val3')
        raise RuntimeError('thrown error')
except RuntimeError as err:
    print('ERROR: {}'.format(err))

# contextlib_exitstack_callbacks_decorator
with contextlib.ExitStack() as stack:

    @stack.callback
    def inline_cleanup():
        print('inline_cleanup()')
        print('local_resource = {!r}'.format(locale_resource))

    locale_resource = 'resource created in context'
    print('within the context')
