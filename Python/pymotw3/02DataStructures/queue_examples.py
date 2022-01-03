#! /usr/bin/python3
# *-* coding: utf-8 *-*
"""queue_examples
@Author: yongliang
@License: MIT
"""

import queue
import functools
import threading
import time
import urllib
from urllib.parse import urlparse

import feedparser


print('\n---- fifo ----')
q = queue.Queue()

for i in range(5):
    q.put(i)

while not q.empty():
    print(q.get(), end='  ')
print()

print('\n---- lifo ----')

q = queue.LifoQueue()

for i in range(5):
    q.put(i)

while not q.empty():
    print(q.get(), end='  ')
print()

print('\n---- priority ----')


@functools.total_ordering
class Job:
    def __init__(self, priority, description):
        self.priority = priority
        self.description = description
        print('New Job:', description)
        return

    def __eq__(self, other):
        print('__eq__')
        try:
            return self.priority == other.priority
        except AttributeError:
            print('exception __eq__')
            return NotImplemented

    def __lt__(self, other):
        print('__lt__')
        try:
            return self.priority < other.priority
        except AttributeError:
            print('exception __lt__')
            return NotImplemented


q = queue.PriorityQueue()
q.put(Job(3, 'Mid-level job'))
q.put(Job(10, 'Low-level job'))
q.put(Job(1, 'Important job'))


def process_job(q):
    while True:
        next_job = q.get()
        print('Processing job:', next_job.description)
        q.task_done()


workers = [
    threading.Thread(target=process_job, args=(q,)),
    threading.Thread(target=process_job, args=(q,)),
]

for w in workers:
    print('www')
    w.setDaemon(True)
    w.start()

q.join()
