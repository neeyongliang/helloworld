#! /usr/bin/python3
# *-* coding: utf-8 *-*
"""26collections-deque
@Author: wikinee
@License: MIT
"""

from collections import deque

d = deque()
d.append('1')
d.append('2')
d.append('3')

print(len(d))

print(d[0])

print(d[-1])

d.popleft()
print(d)
d.pop(d)
print(d)
