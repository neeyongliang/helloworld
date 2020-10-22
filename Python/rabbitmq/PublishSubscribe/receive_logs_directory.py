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
channel.exchange_declare(exchange='direct_logs',
                         type='direct')
result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

serverties = sys.argv[1:]
if not serverties:
    print(sys.stderr, "Usage: %s [info] [warning] [error]" % sys.argv[0])
    sys.exit(1)

for serverity in serverties:
    channel.queue_bind(exchange='direct_logs',
                       queue=queue_name,
                       routing_key=serverity)
print(" [x] Waiting for logs. To exit press CTRL+C")


def callback(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body))


channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)
channel.start_consuming()