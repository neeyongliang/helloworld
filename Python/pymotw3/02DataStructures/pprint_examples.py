#! /usr/bin/python3
# *-* coding: utf-8 *-*
"""pprint
@Author: yongliang
@License: MIT
"""

import logging
from pprint import pprint
from pprint import pformat
from pprint_data import data


print('\n---- pprint ----')
print('PRINT:')
print(data)
print()
print('PPRINT:')
pprint(data)

print('\n---- pformat ----')
logging.basicConfig(
    level=logging.DEBUG,
    format='%(levelname)-8s %(message)s',
)

logging.debug('Logging pformatted data')
formatted = pformat(data)
for line in formatted.splitlines():
    logging.debug(line.rstrip())
