#! /usr/bin/python3
# *-* coding: utf-8 *-*
"""10set
@Author: wikinee
@License: MIT
"""

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

print("--- EXAMPLE 1 ---")
duplicates = []
for value in some_list:
    # print("---", value)
    if some_list.count(value) > 1:
        # count will record occurrences times in list
        # print(value)
        if value not in duplicates:
            duplicates.append(value)

print(duplicates)

print("--- EXAMPLE 2 ---")
duplicates2 = set([x for x in some_list if some_list.count(x) > 1])
print(duplicates2)

vaild = set(['yellow', 'red', 'blue', 'green', 'black'])
input_set = set(['red', 'brown'])
print(input_set.intersection(vaild))
print(input_set.difference(vaild))
