#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:
#   yongliang <yongliang@cpu-os.ac.cn>

import pika
import sys

TEST_SERVER = '172.30.18.148'
TEST_PORT = 5672
TEST_USERNAME = 'test'
TEST_PASSWORD = '123456'


def main():
    test_credentials = pika.PlainCredentials(username=TEST_USERNAME, password=TEST_PASSWORD)
    connection = pika.BlockingConnection(pika.ConnectionParameters(
        host=TEST_SERVER,
        port=TEST_PORT,
        credentials=test_credentials))
    channel = connection.channel()
    channel.exchange_declare(exchange='logs', exchange_type='fanout')
    while True:
        message = input("<< ")
        if message == "quit":
            break
        channel.basic_publish(exchange='logs', routing_key='', body=message)
        print(" [x] Sent %r" % message)
    connection.close()


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print("Exception occur, %s" % e)
