#! /usr/bin/python3
# *-* coding: utf-8 *-*
"""20deco_class
@Author: wikinee
@License: MIT
"""


class Logit(object):
    def __init__(self, logfile='out.log'):
        self.logfile = logfile

    def __call__(self, func):
        log_string = func.__name__ + " was called"
        print(log_string)
        # 打开logfile并写入
        with open(self.logfile, 'a') as opened_file:
            # 现在将日志打到指定的文件
            opened_file.write(log_string + '\n')
        # 现在，发送一个通知
        self.notify()

    def notify(self):
        # logit只打日志，不做别的
        pass


@Logit()
def myfunc1():
    pass


class EmailLogit(Logit):
    """
    一个 logit 的实现版本，可以发送email
    """
    def __init__(self, email='admin@myproject.com', *args, **kwargs):
        self.email = email
        super(EmailLogit, self).__init__(*args, **kwargs)

    def notify(self):
        pass