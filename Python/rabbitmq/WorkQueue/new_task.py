#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:
#   yongliang <yongliang@cpu-os.ac.cn>

import pika

TEST_SERVER = '172.30.18.148'
TEST_PORT = 5672
TEST_USERNAME = "test"
TEST_PASSWORD = "123456"

test_credentials = pika.PlainCredentials(TEST_USERNAME, TEST_PASSWORD)
connection = pika.BlockingConnection(pika.ConnectionParameters(
    host=TEST_SERVER,
    port=TEST_PORT,
    credentials=test_credentials))
channel = connection.channel()
channel.queue_declare(queue='task_queue', durable=True)

while True:
    input_str = input("<< ")
    if input_str == "quit":
        break
    channel.basic_publish(exchange='',
                          routing_key='task_queue',
                          body=input_str.encode(),
                          properties=pika.BasicProperties(
                              delivery_mode=2,
                          ))
    print(" [x] Sent '%s!'" % input_str)
connection.close()
