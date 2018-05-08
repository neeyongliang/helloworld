#! /usr/bin/python3
# *-* coding: utf-8 *-*
"""collections_deque
@Author: wikinee
@License: MIT
"""

import collections
import threading
import time
import random

print('\n---- deque ----')
d = collections.deque('abcdefg')
print('Deque:', d)
print('Length:', len(d))
print('Left end:', d[0])
print('Right end:', d[-1])

d.remove('c')
print('remove(c):', d)

print('\n---- deque populating ----')
# Add to the right
d1 = collections.deque()
d1.extend('abcdefg')
print('extend    :', d1)
d1.append('h')
print('append    :', d1)

# Add to the left
d2 = collections.deque()
d2.extendleft(range(6))
print('extendleft:', d2)
d2.appendleft(6)
print('appendleft:', d2)


print('\n---- deque consuming ----')
print('From the right:')
d = collections.deque('abcdefg')
print('Original {}'.format(d))
while True:
    try:
        print(d.pop(), end='')
    except IndexError:
        break
print()

print('\nFrom the left:')
d = collections.deque(range(6))
print('Original {}'.format(d))
while True:
    try:
        print(d.popleft(), end='')
    except IndexError:
        break
print()


print('\n---- deque both ends ----')
candle = collections.deque(range(5))


def burn(direction, nextSource):
    while True:
        try:
            next = nextSource()
        except IndexError:
            break
        else:
            print('{:>8}: {}'.format(direction, next))
            time.sleep(0.1)
    print('{:>8} done'.format(direction))
    return


left = threading.Thread(target=burn,
                        args=('Left', candle.popleft))
right = threading.Thread(target=burn,
                         args=('Right', candle.pop))

left.start()
right.start()

left.join()
right.join()

print('\n---- deque rotate ----')
d = collections.deque(range(10))
print('Normal           :', d)

d = collections.deque(range(10))
d.rotate(2)
print('Right rotation   :', d)

d = collections.deque(range(10))
d.rotate(-2)
print('Left rotation    :', d)


print('\n---- deque maxlen ----')
# Set the random seed so we see the same output each time
# the script is run.
random.seed(1)  # random is not real random!

d1 = collections.deque(maxlen=3)
d2 = collections.deque(maxlen=3)

for i in range(5):
    n = random.randint(0, 100)
    print('n=', n)
    d1.append(n)
    d2.appendleft(n)
    print('D1:', d1)
    print('D2:', d2)

