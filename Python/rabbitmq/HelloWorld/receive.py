#!/usr/bin/env python3
# -*- coding: utf-8 -*-
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
channel.queue_declare(queue='hello')


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


channel.basic_consume(callback,
                      queue='hello',
                      no_ack=False)

print(' [*] Waiting for message. To exit press CTRL+c')
channel.start_consuming()
