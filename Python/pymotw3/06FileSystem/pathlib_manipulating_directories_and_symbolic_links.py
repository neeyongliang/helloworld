#! /usr/bin/python3
# *-* coding: utf-8 *-*
"""pathlib_manipulating_directories_and_symbolic_links
@Author: wikinee
@License: MIT
@Date: Nov.14 2018
"""
import pathlib

print("===== file: pathlib_mkdir.py =====")
p = pathlib.Path('example_dir')
print('Creating {}'. format(p))
# if directory is exists, will raises a FileExistsError
p.mkdir()

print("===== file: pathlib_symlink.py =====")
p = pathlib.Path('example_link')
p.symlink_to('index.rst')
print(p)
print(p.resolve().name)
