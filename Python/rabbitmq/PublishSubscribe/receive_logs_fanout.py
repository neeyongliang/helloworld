#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:
#   yongliang <yongliang@cpu-os.ac.cn>

import pika
TEST_SERVER = "172.30.18.148"
TEST_PORT = 5672
TEST_USERNAME = "test"
TEST_PASSWORD = "123456"


test_credentials = pika.PlainCredentials(TEST_USERNAME, TEST_PASSWORD)
connection = pika.BlockingConnection(pika.ConnectionParameters(
    host=TEST_SERVER,
    port=TEST_PORT,
    credentials=test_credentials
))
channel = connection.channel()
channel.exchange_declare(exchange='logs', exchange_type='fanout')

# 如果没有连接，就关闭它 => exclusive=True
result = channel.queue_declare('', exclusive=True)
queue_name = result.method.queue

# 如果交换机类型是扇形 fanout, 就会忽略 queue_bind 的参数 routing_key
# 为了防止与 basic_public 参数混淆，这里译为 绑定键 binding key
channel.queue_bind(exchange='logs', queue= queue_name)
print(" [x] Waiting for logs. To exit press CTRL+C")


def callback(ch, method, properties, body):
    print(" [x] %r" % body)


channel.basic_consume(consumer_callback=callback, queue=queue_name, no_ack=True)
channel.start_consuming()