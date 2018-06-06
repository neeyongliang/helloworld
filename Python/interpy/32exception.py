#! /usr/bin/python3
# *-* coding: utf-8 *-*
"""32exception
@Author: wikinee
@License: MIT
"""

print("--- single exception ---")
try:
    file = open('test.txt', 'rb')
except IOError as e:
    print('An IOError occurred. {}'.format(e.args[-1]))

print("--- multiple exception 1 ---")
try:
    file = open('test.txt', 'rb')
except (IOError, EOFError) as e:
    print("An error occurred. {}".format(e.args[-1]))

print("--- multiple exception 2 ---")
try:
    file = open('test.txt', 'rb')
except EOFError as e:
    print("An EOF error occurred.")
    # raise e
except IOError as e:
    print("An error occured.")
    # raise e
finally:
    print("This would be printed whether or not an exception occurred!")

print("--- multiple exception 3 ---")
try:
    file = open('test.txt', 'rb')
except Exception as e:
    # print some log
    # raise
    print(e)

