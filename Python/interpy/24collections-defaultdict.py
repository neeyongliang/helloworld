#! /usr/bin/python3
# *-* coding: utf-8 *-*
"""24collections-defaultdict
@Author: yongliang
@License: MIT
"""

from collections import defaultdict

colours = (
    ('Yasoob', 'Yeallow'),
    ('Ali', 'Blue'),
    ('Arham', 'Green'),
    ('Ali', 'Black'),
    ('Yasoob', 'Red'),
    ('Ahmed', 'Silver'),
)

print("--- defaultdict ---")

favourite_colours = defaultdict(list)

for name, colour in colours:
    favourite_colours[name].append(colour)

print(favourite_colours)


print("--- not use defaultdict ---")
try:
    some_dict = {}
    some_dict['colours']['favourite'] = "yellow"
except Exception as e:
    print(e)

print("--- use defaultdict ---")
tree = lambda :defaultdict(tree)
try:
    some_dict2 = tree()
    some_dict2['colours']['favourite'] = "yellow"
except Exception as e:
    print("use default failed")