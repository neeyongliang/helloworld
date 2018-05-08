#!/usr/bin/python3

import textwrap
from textwrap_example import sample_text
from textwrap_example import sample_text2


print("---- Fill ----")
print(textwrap.fill(sample_text, width=50))

print("\n---- Fill ----")
print(textwrap.fill(sample_text, width=50))

print("\n---- Dedented ----")
print(textwrap.dedent(sample_text))

print("\n---- Fill Width ----")
dedented_text = textwrap.dedent(sample_text).strip()
for width in [45, 60]:
    print('{} Columns:\n'.format(width))
    print(textwrap.fill(dedented_text, width=width))
    print()

# replace prefix with '>'
dedented_text = textwrap.dedent(sample_text)
wrapped = textwrap.fill(dedented_text, width=50)
wrapped += '\n\nSecond paragraph after a blank line.'
final = textwrap.indent(wrapped, '> ')

print('Quoted block:\n')
print(final)


# indent_predicate.py
def should_indent(line):
    print('Indent {!r}?'.format(line))
    return len(line.strip()) % 2 == 0


print("\n---- indent predicate ----")
dedented_text = textwrap.dedent(sample_text)
wrapped = textwrap.fill(dedented_text, width=50)
final = textwrap.indent(wrapped, 'EVEN ', predicate=should_indent)
print('Quoted block:\n')
print(final)

print("\n---- hanging indent ----")
dedented_text = textwrap.dedent(sample_text).strip()
print(textwrap.fill(dedented_text, initial_indent='',
                    subsequent_indent=' ' * 4, width=50,))

print("\n---- shorten ----")
dedented_text = textwrap.dedent(sample_text)
original = textwrap.fill(dedented_text, width=50)
print('Original:\n%s' % original)

shortened = textwrap.shorten(original, 100)
shortened_wrapped = textwrap.fill(shortened, width=50)

print('\nShortened:%s\n' % shortened_wrapped)
