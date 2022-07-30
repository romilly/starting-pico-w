from umqtt.simple import MQTTClient
from network_connection import connect
import time
from secrets import SSID, PASSWORD, MQTT_HOST
import machine, neopixel

np = neopixel.NeoPixel(machine.Pin(16), 8)

colors = [(255, 0, 0),(0, 255, 0),(0, 0, 255)]

def display_level(topic, message):
    print(message)
    _, level_s, _, count_s =  message.decode('UTF8').split(' ')[:4]
    level = int(level_s)
    count = min(int(count_s), 8)
    for i in range(8):
        np[i] = (0, 0, 0)
    for i in range(count):
        np[i] = colors[level-1]
    np.write()
    

def run():
    connect(SSID, PASSWORD)
    mc = MQTTClient('pi-zz056', MQTT_HOST)
    mc.set_last_will('pi-available', 'bye')
    mc.connect()
    mc.set_callback(display_level)
    mc.subscribe('pi-available')
    while True:
        mc.wait_msg()

run()