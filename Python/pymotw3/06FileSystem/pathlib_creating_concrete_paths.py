#! /usr/bin/python3
# *-* coding: utf-8 *-*
"""pathlib_creating_concrete_paths
@Author: yongliang
@License: MIT
@Date: Nov.14 2018
"""
import pathlib

print("===== file: pathlib_comvenience.py =====")
home = pathlib.Path.home()
print('home: ', home)

cwd = pathlib.Path.cwd()
print('cwd: ', cwd)
