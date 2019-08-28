#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import subprocess
import sys

def unpack_deb(deb_path):
    deb_files = os.listdir(deb_path)
    for deb_file in deb_files:
        if deb_file == "unpack.py":
            continue
        if not os.path.isdir(deb_file):
            subprocess.call(["dpkg-deb", "-R", deb_file, os.path.splitext(deb_file)[0]])

if __name__ == '__main__':
    if len(sys.argv) != 2:
        pkg_path = os.path.dirname(os.path.realpath(__file__))
    else:
        pkg_path = sys.argv[1]
    unpack_deb(pkg_path)
