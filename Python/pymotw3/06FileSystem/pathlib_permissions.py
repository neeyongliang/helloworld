#! /usr/bin/python3
# *-* coding: utf-8 *-*
"""pathlib_permissions
@Author: yongliang
@License: MIT
@Date: Nov.14 2018
"""
import os
import pathlib
import stat

print("\n===== file: pathlib_.py =====")

print("\n===== file: pathlib_chmod.py =====")
# Create a fresh test file
f = pathlib.Path('pathlib_chmod_example.txt')

if f.exists():
    f.unlink()

f.write_text('contents')

# Determine what permissions are already set using stat.
exsiting_permissions = stat.S_IMODE(f.stat().st_mode)
print('Before: {:0}'.format(exsiting_permissions))

# Decide with way to toggle them.
print(exsiting_permissions)
if not (exsiting_permissions & os.X_OK):
    print('Adding execute permission')
    new_permissions = exsiting_permissions | stat.S_IXUSR
else:
    print('Removing execute permission')
    new_permissions = exsiting_permissions ^ stat.S_IXUSR

# Make the change and show the new value.
f.chmod(new_permissions)
after_permission = stat.S_IMODE(f.stat().st_mode)
print('After: {:0}'.format(exsiting_permissions))