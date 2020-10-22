#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:
#   yongliang <yongliang@cpu-os.ac.cn>

import pika
TEST_SERVER = "172.30.18.148"
TEST_PORT = 5672
TEST_USER = "test"
TEST_PASSWORD = "123456"

test_credentials = pika.PlainCredentials(TEST_USER, TEST_PASSWORD)
connection = pika.BlockingConnection(pika.ConnectionParameters(
    host=TEST_SERVER,
    port=TEST_PORT,
    credentials=test_credentials))
channel = connection.channel()
channel.queue_declare(queue='rpc_queue')


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def on_request(ch, method, properties, body):
    n = int(body)
    print(" [.] fib(%s)" % n)
    response = fib(n)

    ch.basic_publish(exchange='',
                     routing_key=properties.reply_to,
                     properties=pika.BasicProperties(
                         correlation_id=properties.correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(on_request, queue='rpc_queue')

print(" [x] Awaiting RPC requests")
channel.start_consuming()