#!/usr/bin/python3

import string


# in regular expression, '+' means show up at least once
class MyTemplate(string.Template):
    delimiter = '%'
    idpattern = '[a-z]+_[a-z]+'


template_text = '''
    Delimiter : %%
    Replaced  : %with_underscore
    Ignored   : %notunderscored
'''

d = {
    'with_underscore': 'replaced',
    'notunderscored': 'not replace',
}

t = MyTemplate(template_text)
print('Modified ID pattern:')
print(t.safe_substitute(d))