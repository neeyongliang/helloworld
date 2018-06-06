#! /usr/bin/python3
# *-* coding: utf-8 *-*
"""41implement-as-class
@Author: wikinee
@License: MIT
"""


class File(object):
    def __init__(self, file_name, method):
        print("--- __init__ ---")
        self.file_obj = open(file_name, method)

    def __enter__(self):
        print("--- __enter__ ---")
        return self.file_obj

    def __exit__(self, type, value, trackback):
        print("--- __exit__ ---")
        print("type: ", type)
        print("value: ", value)
        print("trackback: ", trackback)
        if type:
            return False
        print("Exception has been handled")
        self.file_obj.close()
        return True


with File('demo.txt', 'w') as opened_file:
    opened_file.write('Hola!')
