#! /usr/bin/python3
# *-* coding: utf-8 *-*
"""27collections-namedtuple
@Author: yongliang
@License: MIT
"""

from collections import namedtuple

Animal = namedtuple('Animal', 'name age type')
perry = Animal(name="perry", age=31, type="cat")

print(perry)
try:
    perry(perry.name)
except Exception as e:
    print(e)

print(perry[0])
print(perry._asdict())