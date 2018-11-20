#! /usr/bin/python3
# *-* coding: utf-8 *-*
"""tempfile_files
@Author: wikinee
@License: MIT
@Date: Nov.20 2018
"""
import os
import tempfile

print("\n===== file: tempfile_TemporaryFile.py =====")
print('Building a filename with PID:')
filename = '/tmp/guess_my_name.{}.txt'.format(os.getpid())
with open(filename, 'w+b') as temp:
    print('temp:')
    print('  {!r}'.format(temp))
    print('temp.name:')
    print('  {!r}'.format(temp.name))

# Clean up the temporary file yourself.
os.remove(filename)

print()
print('TemporaryFile:')
with tempfile.TemporaryFile() as temp:
    print('temp:')
    print('  {!r}'.format(temp))
    print('temp.name:')
    print('  {!r}'.format(temp.name))


print("\n===== file: temp_TemporaryFile_text.py =====")
with tempfile.TemporaryFile(mode='w+t') as f:
    f.writelines(['first\n', 'second\n'])

    f.seek(0)
    for line in f:
        print(line.rstrip())
