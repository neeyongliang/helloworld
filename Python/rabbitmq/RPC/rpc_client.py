#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:
#   yongliang <yongliang@cpu-os.ac.cn>
import pika
import uuid

TEST_SERVER = "172.30.18.148"
TEST_PORT = 5672
TEST_USER = "test"
TEST_PASSWORD = "123456"


class FibonacciRpcClient(object):
    def __init__(self):
        self.response = None
        self.corr_id = ""
        self.test_credentials = pika.PlainCredentials(TEST_USER, TEST_PASSWORD)
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(
            host=TEST_SERVER,
            port=TEST_PORT,
            credentials=self.test_credentials))
        self.channel = self.connection.channel()
        result = self.channel.queue_declare(exclusive=True)
        self.callback_queue = result.method.queue

        self.channel.basic_consume(self.on_response, no_ack=True,
                                   queue=self.callback_queue)

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self, n):
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(exchange='',
                                   routing_key='rpc_queue',
                                   properties=pika.BasicProperties(
                                         reply_to=self.callback_queue,
                                         correlation_id=self.corr_id),
                                   body=str(n))
        while self.response is None:
            self.connection.process_data_events()
        return int(self.response)


fibonacci_rpc = FibonacciRpcClient()


print(" [x] Requesting fib(30)")
response = fibonacci_rpc.call(30)
print(" [.] Got %r" % (response,))
