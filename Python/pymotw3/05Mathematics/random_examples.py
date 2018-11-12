#! /usr/bin/python3
# *-* coding: utf-8 *-*
"""random_examples
@Author: wikinee
@License: MIT
"""

import random
import os
import pickle
import itertools
import time

print('\n--- random_random.py ---')
for i in range(5):
    print('%04.3f' % random.random(), end=' ')
print()

print('\n--- random_uniform.py ---')
for i in range(5):
    print('{:04.3f}'.format(random.uniform(1, 100)), end=' ')
print()

print('\n--- random_seed.py ---')
random.seed(1)

for i in range(5):
    print('{:04.3f}'.format(random.random()), end=' ')
print()

print('\n--- random_state.py ---')
if os.path.exists('state.dat'):
    # Restore the previously saved state
    print('Found state.dat, initializing random module')
    with open('state.dat', 'rb') as f:
        state = pickle.load(f)
    random.setstate(state)
else:
    # Use a well-known start state
    print('No state.dat, seeding')
    random.seed(1)

# Produce random values
for i in range(3):
    print('{:04.3f}'.format(random.random()), end=' ')
print()

# Save state for next time
with open('state.dat', 'wb') as f:
    pickle.dump(random.getstate(), f)

# Produce more random values
print('\nAfter saving state:')
for i in range(3):
    print('{:04.3f}'.format(random.random()), end=' ')
print()

print('\n--- random_randint.py ---')
print('[1, 100]:', end=' ')

for i in range(3):
    print(random.randint(1, 100), end=' ')

print('\n[-5, 5]:', end=' ')
for i in range(3):
    print(random.randint(-5, 5), end=' ')
print()

print('\n--- random_randrange.py ---')
for i in range(3):
    print(random.randrange(0, 101, 5), end=' ')
print()

print('\n--- random_choice.py ---')

outcomes = {
    'heads': 0,
    'tails': 0,
}

sides = list(outcomes.keys())

for i in range(10000):
    outcomes[random.choice(sides)] += 1

print('Heads:', outcomes['heads'])
print('Tails:', outcomes['tails'])

print('\n--- random_shuffle.py ---')

FACE_CARDS = ('J', 'Q', 'K', 'A')
SUITS = ('H', 'D', 'C', 'S')


def new_deck():
    return [
        # Always use 2 places for the value, so the strings
        # are a consistent width.
        '{:>2}{}'.format(*c)
        for c in itertools.product(
            itertools.chain(range(2, 11), FACE_CARDS),
            SUITS, )
    ]


def show_deck(deck):
    p_deck = deck[:]
    while p_deck:
        row = p_deck[:13]
        p_deck = p_deck[13:]
        for j in row:
            print(j, end=' ')
        print()


# Make a new deck, with the cards in order
deck = new_deck()
print('Initial deck:')
show_deck(deck)

# Shuffle the deck to randomize the order
random.shuffle(deck)
print('\nShuffled deck:')
show_deck(deck)

# Deal 4 hands of 5 cards each
hands = [[], [], [], []]

for i in range(5):
    for h in hands:
        h.append(deck.pop())

# Show the hands
print('\nHands:')
for n, h in enumerate(hands):
    print('{}:'.format(n + 1), end=' ')
    for c in h:
        print(c, end=' ')
    print()

# Show the remaining deck
print('\nRemaining deck:')
show_deck(deck)

print('\n--- random_sample.py ---')
with open('/etc/apt/sources.list', 'rt') as f:
    words = f.readlines()
words = [w.rstrip() for w in words]

for w in random.sample(words, 5):
    print(w)

print('\n--- random_random_class.py ---')
print('Default initialization:\n')

r1 = random.Random()
r2 = random.Random()

for i in range(3):
    print('{:04.3f} {:04.3f}'.format(r1.random(), r2.random()))

print('\nSame seed:\n')
seed = time.time()

print('\n--- random_system_random.py ---')
r1 = random.Random(seed)
r2 = random.Random(seed)

for i in range(3):
    print('{:04.3f}  {:04.3f}'.format(r1.random(), r2.random()))
