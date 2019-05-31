#!/usr/bin/python3
# -*- coding:utf-8 -*-

import subprocess

def get_cmd_name(pid_str):
    cmd = "ps -o comm= {}".format(pid_str)
    # 在 Python3 是二进制字符串
    cmd_name = subprocess.check_output(cmd, stderr=subprocess.STDOUT, encoding='utf-8', shell=True)
    return cmd_name

def test_cmd_name():
    try:
        res = get_cmd_name('1000')
    except subprocess.CalledProcessError as e:
        print("NfsSyncGtk: Get ahead pid failed, because %s" % e.output)
        print("returncode: %d" % e.returncode)
    else:
        print("res: %s" % res)


if __name__ == '__main__':
    test_cmd_name()