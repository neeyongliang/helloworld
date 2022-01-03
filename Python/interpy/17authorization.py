#! /usr/bin/python3
# *-* coding: utf-8 *-*
"""17authorization
@Author: yongliang
@License: MIT
"""

# use in web application's endpoint, such as Flask and Django web framework

from functools import wraps


def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            authenticate()
        return f(*args, **kwargs)
    return decorated