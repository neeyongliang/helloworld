#! /usr/bin/python3
# *-* coding: utf-8 *-*
"""pathlib_deleting
@Author: wikinee
@License: MIT
@Date: Nov.14 2018
"""
import pathlib

print("===== file: pathlib_rmdir.py =====")
p = pathlib.Path('example_dir')

print('Removing {}'.format(p))
try:
    p.rmdir()
except FileNotFoundError as e:
    print('FileNotFoundError')
except Exception as e:
    print(e)

print("===== file: pathlib_unlink.py =====")
p = pathlib.Path('touched')
p.touch()
print('exists before removing:', p.exists())

p.unlink()
print('exists after removing: ', p.exists())