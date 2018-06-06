#! /usr/bin/python3
# *-* coding: utf-8 *-*
"""25collections-counter
@Author: wikinee
@License: MIT
"""

from collections import Counter

print("--- Counter Example ---")
colours = (
    ('Yasoob', 'Yellow'),
    ('Ali', 'Blue'),
    ('Arham', 'Green'),
    ('Ali', 'Black'),
    ('Yasoob', 'Red'),
    ('Ahmed', 'Silver'),
)

favs = Counter(name for name, colour in colours)
print(favs)

print("--- Counter file ---")
try:
    with open('filename', 'rb') as f:
        line_count = Counter(f)
    print(line_count)
except Exception as e:
    print(e)