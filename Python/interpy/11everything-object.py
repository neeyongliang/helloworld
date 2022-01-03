#! /usr/bin/python3
# *-* coding: utf-8 *-*
"""11everything_object
@Author: yongliang
@License: MIT
"""


def hi(name="yasoob"):
    return "hi" + name


print(hi())
# Output: 'hi yasoob'

greet = hi
print(greet())
# Output: 'hi yasoob'

del hi
try:
    print(hi())
except NameError as e:
    print("NameError: ", e)
except Exception as e:
    print('Unknown Error')

# Output: NameError

print(greet())
# Output: 'hi yasoob'
