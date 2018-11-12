#! /usr/bin/python3
# *-* coding: utf-8 *-*
"""pprint_arbitraty_object
@Author: wikinee
@License: MIT
"""
from pprint import pprint
from pprint_data import data

print('\n---- arbitrary object ----')


class node:

    def __init__(self, name, contents=[]):
        self.name = name
        self.contents = contents[:]

    def __repr__(self):
        return (
            'node(' + repr(self.name) + ', ' +
            repr(self.contents) + ')'
        )


trees = [
    node('node-1'),
    node('node-2', [node('node-2-1')]),
    node('node-3', [node('node-3-1')]),
]

pprint(trees)

print('\n---- depth ----')
pprint(data, depth=1)
pprint(data, depth=2)

print('\n---- compact ----')
print('DEFAULT:')
pprint(data, compact=False)
print('\nCOMPACT:')
pprint(data, compact=True)