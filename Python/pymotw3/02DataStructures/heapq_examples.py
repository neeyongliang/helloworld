#! /usr/bin/python3
# *-* coding: utf-8 *-*
"""heapq_examples
@Author: yongliang
@License: MIT
"""

import heapq
import random
from heapq_heapdata import data
from heapq_showtree import show_tree

print('\n---- head push ----')
heap = []
print('random :', data)
print()

for n in data:
    print('add {:>3}:'.format(n))
    heapq.heappush(heap, n)
    show_tree(heap)

print('\n---- headpheappop ----')
import heapq
from heapq_showtree import show_tree
from heapq_heapdata import data

print('random    :', data)
heapq.heapify(data)
print('heapified :')
show_tree(data)
print()

for i in range(2):
    smallest = heapq.heappop(data)
    print('pop    {:>3}:'.format(smallest))
    show_tree(data)

print('\n---- heap merge ----')
random.seed(2016)

data = []
for i in range(4):
    new_data = list(random.sample(range(1, 101), 5))
    new_data.sort()
    data.append(new_data)

for i, d in enumerate(data):
    print('{}: {}'.format(i, d))

print('\nMerged:')
for i in heapq.merge(*data):
    print(i, end=' ')
print()
