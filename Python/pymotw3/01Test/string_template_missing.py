#!/usr/bin/python3

import string

values = {'var': 'foo'}

t = string.Template("$var is hear but $missing is not provided")

try:
    print('substitude()     :', t.substitute(values))
except KeyError as err:
    print('ERROR:', str(err))

print('safe_substitude():', t.safe_substitute(values))