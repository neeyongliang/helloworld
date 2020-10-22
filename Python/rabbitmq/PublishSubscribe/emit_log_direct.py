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
channel.exchange_declare(exchange='direct_logs', type='direct')
print("log format:\nLOG_LEVEL:LOG_DETAILS")
while True:
    input_str_list = input("<< ").split(':')
    if len(input_str_list) == 1:
        print("Log details cannot empty")
        continue
    serverity = input_str_list[0]
    message = input_str_list[1:][0]
    print(serverity, message)
    if serverity == "quit":
        break
    if serverity != 'info' and serverity != 'warning' and serverity != 'error':
        print("Log type only support info/warning/error")
        continue
    channel.basic_publish(exchange='direct_logs',
                          routing_key=serverity,
                          body=message)
    print(" [x] Sent %r:%r" % (serverity, message))

connection.close()