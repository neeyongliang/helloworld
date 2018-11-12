#! /usr/bin/python3
# *-* coding: utf-8 *-*
"""ospath_examples
@Author: wikinee
@License: MIT
"""
import os.path
import os
import time

"""
b : 二进制
d ：十进制
o ：八进制
x ：十六进制
!s ：将对象格式化转换成字符串
!a ：将对象格式化转换成ASCII
!r ：将对象格式化转换成repr
"""

print('--- ospath_split.py ---')
PATHS = [
    '/one/two/three呵呵',
    '/one/two/three哈哈/',
    '/',
    '.',
    '',
]

for path in PATHS:
    print('{!r:>17} : {}'.format(path, os.path.split(path)))

print('\n--- ospath_basename.py ---')
for path in PATHS:
    print('{!r:>17} : {!r}'.format(path, os.path.basename(path)))

print('\n--- ospath_dirname.py ---')
for path in PATHS:
    print('{!r:>17} : {!r}'.format(path, os.path.dirname(path)))

print('\n--- ospath_splitex.py ---')
PATHS2 = [
    'filename.text',
    'filename',
    '/path/to/filename.txt',
    '/',
    '',
    'my-archive.tar.gz',
    'no-extension.'
]

for path in PATHS2:
    print('{!r:>21} : {!r}'.format(path, os.path.splitext(path)))

print('\n--- ospath_commonprefix.py ---')
paths = ['/one/two/three/four',
         '/one/two/threefold',
         '/one/two/three/',
         ]
for path in paths:
    print('PATH:', path)

print()
print('PREFIX:', os.path.commonprefix(paths))

print('\n--- ospath_commonpath.py ---')
paths = ['/one/two/three/four',
         '/one/two/threefold',
         '/one/two/three/',
         ]
for path in paths:
    print('PATH:', path)

print()
print('PREFIX:', os.path.commonpath(paths))


print('\n--- ospath_join.py ---')
PATHS = [
    ('one', 'two', 'three'),
    ('/', 'one', 'two', 'three'),
    ('/one', '/two', '/three'),
]

for parts in PATHS:
    print('{} : {!r}'.format(parts, os.path.join(*parts)))

print('\n--- ospath_expanduser.py ---')
for user in ['', 'Desktop', 'Desktop']:
    lookup = '~' + user
    print('{!r:>15} : {!r}'.format(
        lookup, os.path.expanduser(lookup)))

print('\n--- ospath_expandvars.py ---')
os.environ['MYVAR'] = 'VALUE'

print(os.path.expandvars('/path/to/$MYVAR'))

print('\n--- ospath_normpath.py ---')
PATHS = [
    'one//two//three',
    'one/./two/./three',
    'one/../alt/two/three',
]

for path in PATHS:
    print('{!r:>22} : {!r}'.format(path, os.path.normpath(path)))


print('\n--- ospath_abspath.py ---')
os.chdir('/usr')

PATHS = [
    '.',
    '..',
    './one/two/three',
    '../one/two/three',
]

for path in PATHS:
    print('{!r:>21} : {!r}'.format(path, os.path.abspath(path)))

print('\n--- ospath_properties.py ---')
print('File         :', __file__)
print('Access time  :', time.ctime(os.path.getatime(__file__)))
print('Modified time:', time.ctime(os.path.getmtime(__file__)))
print('Change time  :', time.ctime(os.path.getctime(__file__)))
print('Size         :', os.path.getsize(__file__))


print('\n--- ospath_tests.py ---')
FILENAMES = [
    __file__,
    os.path.dirname(__file__),
    '/',
    './broken_link',
]

for file in FILENAMES:
    print('File        : {!r}'.format(file))
    print('Absolute    :', os.path.isabs(file))
    print('Is File?    :', os.path.isfile(file))
    print('Is Dir?     :', os.path.isdir(file))
    print('Is Link?    :', os.path.islink(file))
    print('Mountpoint? :', os.path.ismount(file))
    print('Exists?     :', os.path.exists(file))
    print('Link Exists?:', os.path.lexists(file))
    print()


print('\n---  ---')