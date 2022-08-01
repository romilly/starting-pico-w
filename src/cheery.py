from umqtt.simple import MQTTClient
from network_connection import connect
import time
from secrets import SSID, PASSWORD, MQTT_HOST
import machine, neopixel

np = neopixel.NeoPixel(machine.Pin(16), 8)
history = 8 * [(0, 0, 0)]
BRIGHTNESS = 0.25


def hex_to_rgb(hex):
    return tuple(int(hex[i:i + 2], 16) for i in (1, 3, 5))


def display_level(topic, message):
    print(message)
    rgbs = message.decode('UTF8')
    rgb3 = hex_to_rgb(rgbs)
    rgb_dim = tuple([int(c * BRIGHTNESS) for c in rgb3])
    global history
    history = history[1:] + [rgb_dim]
    for i in range(8):
        np[i] = history[i]
    np.write()


def run():
    connect(SSID, PASSWORD)
    mc = MQTTClient('pi-zz056', MQTT_HOST)
    mc.connect()
    mc.set_callback(display_level)
    mc.subscribe('cheerlightsRGB')
    while True:
        mc.wait_msg()


run()