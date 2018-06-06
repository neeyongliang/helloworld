#! /usr/bin/python3
# *-* coding: utf-8 *-*
"""33excepiton-try-else
@Author: wikinee
@License: MIT
"""

try:
    print("I am sure no exception is going to occur!")
except Exception:
    print('exception')
else:
    print("This would only run if no excepiton occurs. and an error here "
          "would NOT be caught.")
finally:
    print("This would be printed in every case.")