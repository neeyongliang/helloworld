#!/usr/bin/python3
# -*- coding:utf-8 -*-

import smbc
import os
import stat

WORKGROUP = "WORKGROUP"
SERVER = "192.168.0.103"
SHARE = "MyTest"
USERNAME = "apple"
PASSWORD = " "
DESTDIR = "test"

BASE_URI = "smb://" + SERVER + '/' + SHARE
DEST_URI = BASE_URI + '/' + "ubuntu-18.04.1-desktop-amd64.iso"

print(DEST_URI)

def my_auth_callback_fn(wg, se, sh, u, p):
    return (WORKGROUP, USERNAME, PASSWORD)

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