#! /usr/bin/python3
# *-* coding: utf-8 *-*
"""contextlib_suppress
@Author: wikinee
@License: MIT
"""

import contextlib


class NonFatalError(Exception):
    pass


def non_idempotent_operation():
    raise NonFatalError('The operation failed because of existing state')


with contextlib.suppress(NonFatalError):
    print('trying non-idempotent operation')
    non_idempotent_operation()
    print('succeeded!')

print('done')
