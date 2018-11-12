#! /usr/bin/python3
# *-* coding: utf-8 *-*
"""contextlib_ignore_error
@Author: wikinee
@License: MIT
"""

import contextlib


class NonFatalError(Exception):
    pass


def non_idempotent_operation():
    raise NonFatalError('The operation failed becase of existing state')


try:
    print('trying non-idempotent operation')
    non_idempotent_operation()
    print('succeeded!')
except NonFatalError:
    pass

print('done')
