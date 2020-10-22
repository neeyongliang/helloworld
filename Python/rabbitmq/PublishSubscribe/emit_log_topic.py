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

test_credentails = pika.PlainCredentials(TEST_USERNAME, TEST_PASSWORD)
connection = pika.BlockingConnection(pika.ConnectionParameters(
    host=TEST_SERVER,
    port=TEST_PORT,
    credentials=test_credentails))
channel = connection.channel()
channel.exchange_declare(exchange='topic_logs',
                         type='topic')
while True:
    routing_key = input("<< binding key: ")
    if not routing_key:
        routing_key = 'anonymous.info'
    elif routing_key == "quit":
        break
    message = input("<< message: ")
    if not message:
        message = 'Hello, YL!'

    channel.basic_publish(exchange='topic_logs',
                          routing_key=routing_key,
                          body=message)
    print(" [x] Sent %r:%r" % (routing_key, message))
connection.close()
