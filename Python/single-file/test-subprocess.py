#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import subprocess

def test_popen():
    proc = subprocess.Popen("ping www.bing.com", shell=True)
    print("proc: {}".format(proc.pid))
    try:
        outs, errs = proc.communicate(timeout=15)
    except subprocess.TimeoutExpired:
        proc.kill()
        outs, errs = proc.communicate()
        print("proc: {}".format(proc.pid))

if __name__ == '__main__':
    test_popen()
