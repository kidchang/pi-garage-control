#!/usr/local/bin/python3

#import RPi.GPIO as GPIO
import os
import time
import pika
import simplejson as json
import sys

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.output(7, True)
GPIO.output(11, True)



def operate_garage_door(action='open'):
    GPIO.output(7, False)
    time.sleep(.8)
    GPIO.output(7, True)
    return "Door cycled."

if __name__ == "__main__":
    queue = sys.argv[1]
    connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='13.52.107.109',
        port='5672')
    )
    channel = connection.channel()
    channel.queue_declare(queue=queue, durable=False)

    def callback(ch, method, properties, body):
        decoded_body = str(body, 'utf-8')
        action = json.loads(decoded_body)['action']
        operate_garage_door(action)

    channel.basic_consume(
        callback,
        queue,
        no_ack=True
    )
    print(' [*] Waiting for actions...')
    channel.start_consuming()
