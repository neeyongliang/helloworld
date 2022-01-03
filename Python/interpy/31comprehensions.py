#! /usr/bin/python3
# *-* coding: utf-8 *-*
"""31comprehensions-list
@Author: yongliang
@License: MIT
"""

print("--- list comprehensions ---")
multiples = [i for i in range(30) if i % 3 is 0]
print(multiples)

squared = []
for x in range(10):
    squared.append(x**2)

# or
# squared = [x**2 for x in range(10)]

print("--- dict comprehensions ---")

mcase = {'a': 10, 'b': 42, 'A': 7, 'Z': 3}


# mcase_frequency == {'a': 17, 'z': 3, 'b': 34}
mcase_frequency = {
    k.lower(): mcase.get(k.lower(), 0) + mcase.get(k.upper(), 0)
    for k in mcase
}
print(mcase_frequency)
# {v: k for k, v in some_dict.items()}

print("--- set comprehensions ---")
squared = {x**2 for x in [1, 1, 2]}
print(squared)
