#! /usr/bin/python3
# *-* coding: utf-8 *-*
"""35oneline
@Author: wikinee
@License: MIT
"""

from pprint import pprint
import itertools

print("--- simple web server ---")
# python 2
print("python -m SimpleHTTPServer")
# python 3
print("python -m http.server")

print("--- beautiful print ---")
my_dict = {'name': 'Yasoob', 'age': 'undefined', 'personality': 'awesome'}
pprint(my_dict)
# cat file.json | python -m json.tool

print("--- script performance analysis ---")
print("python -m cProfile my_script.py")

print("--- covert CSV to json ---")
# python -c "import cvs, json;"
# "print json.dumps(list(cvs.reader(open('cvs_fils.cvs', 'rb'))))"

print("--- flat list ---")
a_list = [[1, 2], [3, 4], [5, 6]]
print(list(itertools.chain.from_iterable(a_list)))
print(list(itertools.chain(*a_list)))

print("--- creator ---")


class A(object):
    def __init__(self, a, b, c, d, e, f):
        self.__dict__.update({k: v for k, v in locals().items() if k != 'self'})

# Official Page:
# https://wiki.python.org/moin/Powerful%20Python%20One-Liners
