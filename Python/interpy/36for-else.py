#! /usr/bin/python3
# *-* coding: utf-8 *-*
"""36for-else
@Author: wikinee
@License: MIT
"""
fruits = ['apple', 'banana', 'mango']
for fruit in fruits:
    print(fruit.capitalize())

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n / x)
            break
        else:
            print(">>>", n)

    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')