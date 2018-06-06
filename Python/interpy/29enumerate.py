#! /usr/bin/python3
# *-* coding: utf-8 *-*
"""29enumerate
@Author: wikinee
@License: MIT
"""

some_list = ['a', 'v', 'd', 'e', 'g', 's']
for counter, value in enumerate(some_list):
    print(counter, value)

couter_list = list(enumerate(some_list, 1))
print("--- list enumerate ---")
print(couter_list)