#! /usr/bin/python3
# *-* coding: utf-8 *-*
"""22multiple-return-values
@Author: yongliang
@License: MIT
"""


def profile():
    name = "Danny"
    age = 30
    # or return name, age
    return (name, age)


profile_data = profile()
print(profile_data[0])
print(profile_data[1])