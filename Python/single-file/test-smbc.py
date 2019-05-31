#!/usr/bin/python3
# -*- coding:utf-8 -*-

import smbc
import os
import stat
from pprint import pprint

WORKGROUP = "WORKGROUP"
SERVER = "172.30.36.101"
SHARE = "share_for_all"
USERNAME = "cdos"
PASSWORD = "heheda"
DESTDIR = "tmp/MyTest"

BASE_URI = "smb://" + SERVER + '/' + SHARE
DEST_URI = BASE_URI + '/' + "ubuntu-18.04.1-desktop-amd64.iso"

# print(DEST_URI)

def my_auth_callback_fn(wg, se, sh, u, p):
    return (WORKGROUP, USERNAME, PASSWORD)

def test_opendir(dest_dir):
    ctx = smbc.Context(auth_fn=my_auth_callback_fn)
    try:
        open_obj = ctx.opendir(dest_dir)
    except smbc.TimedOutError:
        print("Connection failed, server path maybe error")
    except smbc.NoEntryError:
        print("Connection failed, share path or destination path maybe error")
    except smbc.PermissionError as e:
        print("Permission failed, username or password error")
    except Exception as e:
        print("333 {}".format(e))

def test_write():
    ctx = smbc.Context(auth_fn=my_auth_callback_fn)
    file_obj = ctx.open(DEST_URI, os.O_CREAT | os.O_WRONLY)
    file_obj.write("YOYOYOYOYOYO")
    file_obj.close()

    st = ctx.stat(DEST_URI)
    # print(st)
    print(st[stat.ST_SIZE])
    # mode = st[stat.ST_MODE]
    # print(mode)
    print(os.path.getsize('/home/apple/MyTest/ubuntu-18.04.1-desktop-amd64.iso'))

if __name__ == '__main__':
    test_opendir(BASE_URI + '/' + DESTDIR)