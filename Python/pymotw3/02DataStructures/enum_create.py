#! /usr/bin/python3
# *-* coding: utf-8 *-*
"""enum_create
@Author: yongliang
@License: MIT
"""

import enum


class BugStatus(enum.Enum):

    new = 7
    incomplete = 6
    invalid = 5
    wont_fix = 4
    in_progress = 3
    fix_committed = 2
    fix_released = 1


print('\n---- create ----')
print('\nMember name: {}'.format(BugStatus.wont_fix.name))
print('Member value: {}'.format(BugStatus.wont_fix.value))


print('\n---- iterate ----')
for status in BugStatus:
    print('{:15} = {}'.format(status.name, status.value))


print('\n---- comparison ----')

actual_state = BugStatus.wont_fix
desired_state = BugStatus.fix_released

print('Equality:',
      actual_state == desired_state,
      actual_state == BugStatus.wont_fix)
print('Identity:',
      actual_state is desired_state,
      actual_state is BugStatus.wont_fix)
print('Ordered by value:')
try:
    print('\n'.join('  ' + s.name for s in sorted(BugStatus)))
except TypeError as err:
    print('  Cannot sort: {}'.format(err))


print('\n---- intenum ----')


class BugStatus2(enum.IntEnum):
    new = 7
    incomplete = 6
    invalid = 5
    wont_fix = 4
    in_progress = 3
    fix_committed = 2
    fix_released = 1


print('Ordered by value:')
print('\n'.join('  ' + s.name for s in sorted(BugStatus2)))


print('\n---- aliases ----')


class BugStatus3(enum.IntEnum):
    new = 7
    incomplete = 6
    invalid = 5
    wont_fix = 4
    in_progress = 3
    fix_committed = 2
    fix_released = 1

    by_design = 4
    closed = 1


for status in BugStatus3:
    print('{:15} = {}'.format(status.name, status.value))

print('\nSame: by_design is wont_fix: ',
      BugStatus3.by_design is BugStatus3.wont_fix)
print('Same: closed is fix_released: ',
      BugStatus3.closed is BugStatus3.fix_released)


print('\n---- unique enforce ----')


try:
    @enum.unique
    class BugStatus4(enum.Enum):

        new = 7
        incomplete = 6
        invalid = 5
        wont_fix = 4
        in_progress = 3
        fix_committed = 2
        fix_released = 1

        # This will trigger an error with unique applied.
        by_design = 4
        closed = 1
except ValueError as e:
    print(e)
except Exception as e:
    print(e)


print('\n---- programmatic create ----')
BugStatus5 = enum.Enum(
    value='BugStatus5',
    names=('fix_released fix_committed in_progress '
           'wont_fix invalid incomplete new'),
)

print('Member: {}'.format(BugStatus5.new))

print('\nAll members:')
for status in BugStatus5:
    print('{:15} = {}'.format(status.name, status.value))


print('\n---- programmatic mapping ----')
BugStatus6 = enum.Enum(
    value='BugStatus6',
    names=[
        ('new', 7),
        ('incomplete', 6),
        ('invalid', 5),
        ('wont_fix', 4),
        ('in_progress', 3),
        ('fix_committed', 2),
        ('fix_released', 1),
    ],
)

print('All members:')
for status in BugStatus6:
    print('{:15} = {}'.format(status.name, status.value))


print('\n---- tuple values ----')


class BugStatus7(enum.Enum):
    """
    Enum member values are not restricted to integers.
    In fact, any type of object can be associated with a member.
    If the value is a tuple, the members are passed as individual
    arguments to __init__().
    """
    new = (7, ['incomplete',
               'invalid',
               'wont_fix',
               'in_progress'])
    incomplete = (6, ['new', 'wont_fix'])
    invalid = (5, ['new'])
    wont_fix = (4, ['new'])
    in_progress = (3, ['new', 'fix_committed'])
    fix_committed = (2, ['in_progress', 'fix_released'])
    fix_released = (1, ['new'])

    def __init__(self, num, transitions):
        self.num = num
        self.transitions = transitions
        print('--> name {} transitions {}'.format(num, transitions))

    def can_transition(self, new_state):
        print('--> new_state: {} transitions: {}'.format(
            new_state, self.transitions))
        return new_state.name in self.transitions


print('Name:', BugStatus7.in_progress)
print('Value:', BugStatus7.in_progress.value)
print('Custom attribute:', BugStatus7.in_progress.transitions)
print('Using attribute:',
      BugStatus7.in_progress.can_transition(BugStatus7.new))


print('\n---- complex values ----')


class BugStatus8(enum.Enum):
    """
    For more complex cases, tuples might become unwieldy.
    Since member values can be any type of object, dictionaries can
    be used for cases where there are a lot of separate attributes
    to track for each enum value. Complex values are passed directly
    to __init__() as the only argument other than self.
    """
    new = {
        'num': 7,
        'transitions': [
            'incomplete',
            'invalid',
            'wont_fix',
            'in_progress',
        ],
    }
    incomplete = {
        'num': 6,
        'transitions': ['new', 'wont_fix'],
    }
    invalid = {
        'num': 5,
        'transitions': ['new'],
    }
    wont_fix = {
        'num': 4,
        'transitions': ['new'],
    }
    in_progress = {
        'num': 3,
        'transitions': ['new', 'fix_committed'],
    }
    fix_committed = {
        'num': 2,
        'transitions': ['in_progress', 'fix_released'],
    }
    fix_released = {
        'num': 1,
        'transitions': ['new'],
    }

    def __init__(self, vals):
        self.num = vals['num']
        self.transitions = vals['transitions']

    def can_transition(self, new_state):
        return new_state.name in self.transitions


print('Name:', BugStatus8.in_progress)
print('Value:', BugStatus8.in_progress.value)
print('Custom attribute:', BugStatus8.in_progress.transitions)
print('Using attribute:',
      BugStatus8.in_progress.can_transition(BugStatus8.new))
