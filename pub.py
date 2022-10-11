import paho.mqtt.client as mqtt_client
import random
import time
import sys

import serial


broker = 'broker.emqx.io'
client = mqtt_client.Client(f'lab_{random.randint(10000,99999)}')

try:
    client.connect(broker)
except Exception:
    print('Failed to connect')
    exit()

#room = sys.argv[1]
#client.publish(room, 'HAS JOINED THE ROOM'.encode('utf-8'))
#print()
#while True:
#    try:
#        msg = input()
#        client.publish(room, msg.encode('utf-8'))
#    except KeyboardInterrupt:
#        client.publish(room, 'HAS LEFT THE ROOM'.encode('utf-8'))
#        client.disconnect()
#        print()
#        exit()
srl = serial.Serial('/dev/ttyUSB0', 9600)
while True:
    while srl.in_waiting < 1:
        time.sleep(0.1)
    msg = srl.read(1).decode()
    # print(msg)
    client.publish('praise/the/sun', msg.encode('utf-8'))

client.disconnect()