#import RPi.GPIO as GPIO
import os
import time
import pika
import simplejson as json


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

if __name__ == '__main__':
    connection = pika.BlockingConnection(pika.ConnectionParameters(
        host=os.environ['RABBIT_HOST'],
        port='5672')
    )
    channel = connection.channel()
    channel.queue_declare(queue=os.environ['QUEUE'], durable=False)

    def callback(ch, method, properties, body):
        decoded_body = str(body, 'utf-8')
        action = json.loads(decoded_body)['action']
        operate_garage_door(action)

    channel.basic_consume(
        callback,
        os.environ['QUEUE'],
        no_ack=True
    )
    print(' [*] Waiting for actions...')
    channel.start_consuming()
