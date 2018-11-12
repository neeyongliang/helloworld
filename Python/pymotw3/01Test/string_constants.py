#!/usr/bin/python3

import inspect
import string


def is_str(value):
    return isinstance(value, str)


for name, value in inspect.getmembers(string, is_str):
    if name.startswith('_'):
        print('start with _\'s-->>%s\n' % name)
        continue
    print('%s=%r\n' % (name, value))