#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:
#   yongliang <yongliang@cpu-os.ac.cn>

import pika
import time
import os
import sys

TEST_SERVER = '172.30.18.148'
TEST_PORT = 5672
TEST_USERNAME = "test"
TEST_PASSWORD = "123456"


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    time.sleep(body.decode().count('.'))
    print(" [x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)


def main():
    test_credentials = pika.PlainCredentials(TEST_USERNAME, TEST_PASSWORD)
    connection = pika.BlockingConnection(pika.ConnectionParameters(
        host=TEST_SERVER,
        port=TEST_PORT,
        credentials=test_credentials))

    channel = connection.channel()
    channel.queue_declare(queue='task_queue', durable=True)
    print(' [*] Waiting for message. To exit press CTRL+c')
    channel.basic_qos(prefetch_count=2)
    channel.basic_consume(callback,
                          queue='task_queue')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        sys.exit(0)
