#! /usr/bin/python3
# *-* coding: utf-8 *-*
"""pathlib_file_properies
@Author: yongliang
@License: MIT
@Date: Nov.14 2018
"""
import pathlib
import sys
import time

print("\n===== file: pathlib_.py =====")

print("===== file: pathlib_state.py =====")
if len(sys.argv) == 1:
    filename = __file__
else:
    filename = sys.argv[1]

p = pathlib.Path(filename)

stat_info = p.stat()

print('Filename: %s' % filename)
print('{!s:>20} : {}'. format('Size:', stat_info.st_size))
print('{!s:>20} : {}'. format('Permissions:', oct(stat_info.st_mode)))
print('{!s:>20} : {}'. format('Owner:', stat_info.st_uid))
print('{!s:>20} : {}'. format('Device:', stat_info.st_dev))
print('{!s:>20} : {}'. format('Created      :', time.ctime(stat_info.st_ctime)))
print('{!s:>20} : {}'. format('Last modified:', time.ctime(stat_info.st_mtime)))
print('{!s:>20} : {}'. format('Last accessed:', time.ctime(stat_info.st_atime)))

print("\n===== file: pathlib_touch.py =====")

p = pathlib.Path('touched')
if p.exists():
    print('already exists')
else:
    print('creating new')

p.touch()
start = p.stat()
time.sleep(1)
p.touch()
end = p.stat()

print('Start:', time.ctime(start.st_mtime))
print('End  :', time.ctime(end.st_mtime))
