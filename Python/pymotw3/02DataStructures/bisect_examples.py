#! /usr/bin/python3
# *-* coding: utf-8 *-*
"""bisect_examples
@Author: yongliang
@License: MIT
"""

import bisect

print('\n---- example1 ----')
# A series of random numbers
values = [14, 85, 77, 26, 50, 45, 66, 79, 10, 3, 84, 77, 1]

print('New  Pos  Contents')
print('---  ---  -----------')

l = []
for i in values:
    position = bisect.bisect(l, i)
    bisect.insort(l, i)
    print('{:3} {:3}   '.format(i, position), l)


print('\n---- example2 ----')
print('New  Pos  Contents')
print('---  ---  -----------')

# Use bisect_left and insert_left
l = []
for i in values:
    position = bisect.bisect_left(l, i)
    bisect.insort_left(l, i)
    print('{:3} {:3}   '.format(i, position), l)