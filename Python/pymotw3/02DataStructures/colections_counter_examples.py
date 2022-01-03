#! /usr/bin/python3
# *-* coding: utf-8 *-*
"""colections_counter_examples
@Author: yongliang
@License: MIT
"""

import collections

print('\n---- counter init ----')
print(collections.Counter(['a', 'b', 'c', 'a', 'b', 'b']))
print(collections.Counter({'a': 2, 'b': 3, 'c': 1}))
print(collections.Counter(a=2, b=3, c=1))


print('\n---- counter update ----')
c = collections.Counter()
print('Initial :', c)

c.update('abcdaab')
print('Sequence:', c)

c.update({'a': 1, 'd': 5})
print('Dict    :', c)

print('\n---- counter get values ----')
c = collections.Counter('abcdaab')

for letter in 'abcde':
    print('{} : {}'.format(letter, c[letter]))


print('\n---- counter elements ----')
c = collections.Counter('extremely')
c['z'] = 0
print(c)
print(list(c.elements()))

print('\n---- counter most common ----')
c = collections.Counter()
try:
    with open('/etc/apt/sources.list', 'rt') as f:
        for line in f:
            c.update(line.rstrip().lower())
except Exception as e:
    print(e)
else:
    print('Most common:')
    for letter, count in c.most_common(3):
        print('{}: {:>7}'.format(letter, count))
