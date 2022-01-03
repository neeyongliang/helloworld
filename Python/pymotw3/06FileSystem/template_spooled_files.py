#! /usr/bin/python3
# *-* coding: utf-8 *-*
"""template_spooled_files
@Author: yongliang
@License: MIT
@Date: Nov.20 2018
"""

import tempfile

print("\n===== file: tempfile_SpooledTemporaryFile.py =====")
with tempfile.SpooledTemporaryFile(max_size=100,
                                   mode='w+t',
                                   encoding='utf-8') as temp:
    print('temp: {!r}'.format(temp))

    for i in range(3):
        temp.write('This line is repeated over and over.\n')
        print(temp._rolled, temp._file)

print("\n===== file: tempfile_SpooledTemporaryFile_explicit.py =====")
with tempfile.SpooledTemporaryFile(max_size=1000,
                                   mode='w+t',
                                   encoding='utf-8') as temp:
    print('temp: {!r}'.format(temp))

    for i in range(3):
        temp.write('This line is repeated over and over.\n')
        print(temp._rolled, temp._file)
    print('rolling over')
    temp.rollover()
    print(temp._rolled, temp._file)