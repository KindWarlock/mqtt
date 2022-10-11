import time
import paho.mqtt.client as mqtt_client
import random
import serial

chk = True
port = '/dev/ttyUSB0'
ser = serial.Serial(port, 9600)

def on_message(client, userdata, message):
    global chk
    print("check")
    if chk:
        ser.write('1'.encode())
        chk = False
    else:
        ser.write('2'.encode())
        chk = True
    return chk


broker = "broker.emqx.io"
client = mqtt_client.Client(f'lab_{random.randint(10000, 99999)}')
client.on_message = on_message
try:
    client.connect(broker)
except Exception:
    print("Failed to connect.")
    exit()

client.loop_start()
client.subscribe('praise/the/sun')
time.sleep(600)
client.disconnect()
client.loop_stop()

'''
port = "COM10"
ser = serial.Serial(port, 9600)
inp = ''
while inp != "close":
    inp = input()
    if (inp == "lol"):
        on_message()
ser.close()
'''
