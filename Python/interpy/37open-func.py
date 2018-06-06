#! /usr/bin/python3
# *-* coding: utf-8 *-*
"""37open-func
@Author: wikinee
@License: MIT
"""

import io
# Wrong method! Wrong method! Wrong method!
# f = open('photo.jpg', 'r+')
# jpgdata = f.read()
# f.close()

# r: only read
# r+: read and write
# w: cover write
# a: append to end
try:

    with open('/home/cdos/Pictures/test.jpg', 'rb') as inf:
        jpgdata = inf.read()

    if jpgdata.startswith(b'\xff\xd8'):
        text = u'This is a JPEG file (%d bytes long)\n'
    else:
        text = u'This is a random file (%d bytes long)\n'

    with io.open('summary.txt', 'w', encoding='utf-8') as outf:
        outf.write(text % len(jpgdata))
except Exception as e:
    print(e)