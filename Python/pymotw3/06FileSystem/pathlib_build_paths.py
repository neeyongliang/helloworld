#! /usr/bin/python3
# *-* coding: utf-8 *-*
"""pathlib_build_paths
@Author: yongliang
@License: MIT
@Date: Nov.14 2018
"""

import pathlib

print("===== file: pathlib_operator.py =====")
usr = pathlib.PurePosixPath('/usr')
print(usr)

usr_local = usr / 'local'
print(usr_local)

usr_share = usr / pathlib.PurePosixPath('share')
print(usr_share)

root = usr / '..'
print(root)

etc = root / '/etc/'
print(etc)

print("===== file: pathlib_resolve.py =====")
usr_local = pathlib.Path('/usr/local')
share = usr_local / '..' / 'share'
print(share.resolve())

print("===== file: pathlib_joinpath.py =====")
root = pathlib.PurePosixPath('/')
subdirs = ['usr', 'local']
usr_local = root.joinpath(*subdirs)
print(usr_local)
