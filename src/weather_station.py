from umqtt.simple import MQTTClient
from network_connection import connect
from machine import ADC
import time
from secrets import SSID, PASSWORD, MQTT_HOST



connect(SSID, PASSWORD)
mc = MQTTClient('thermo', MQTT_HOST)
mc.connect()

light_levels = [65, 60, 55, 50, 45, 40, 35, 30, 25]


# convert voltage [0-65535] to light level [0-9]
def convert_to_light_level(adcv: int) -> int:
    for (i, level) in enumerate(light_levels):
        if adcv > 1000 * level:
            return i+1
    return 0


def convert_adc_value_to_temp(adcv: int):
    volts_mv = 3300 * adcv / 65535.0  # 3V3 = 65535
    return (volts_mv - 500) / 10.0  # formula from datasheet


adc0 = ADC(26) # 
adc1 = ADC(27)

while True:
    a0 = adc0.read_u16()
    a1 = adc1.read_u16()
    temp = convert_adc_value_to_temp(a0)
    light_level = convert_to_light_level(a1)
    temp_string = '%5.2f' % temp
    print('(%s, %d)' % (temp_string, light_level))
    mc.publish('weather', 'temp: %s light: %d' % (temp_string, light_level))
    time.sleep(1)
