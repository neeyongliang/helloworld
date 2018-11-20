#! /usr/bin/python3
# *-* coding: utf-8 *-*
"""template_named_files
@Author: wikinee
@License: MIT
@Date: Nov.20 2018
"""

import os
import pathlib
import tempfile

with tempfile.NamedTemporaryFile() as temp:
    print('temp:')
    print('  {!r}'.format(temp))
    print('temp.name:')
    print('  {!r}'.format(temp.name))

    f = pathlib.Path(temp.name)
