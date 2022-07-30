from typing import List

from pi_finder.display import Display
import paho.mqtt.client as mqtt


class MqttPublisher(Display):
    def __init__(self):
        Display.__init__(self)
        self.publisher = mqtt.Client('pi-finder')
        self.publisher.connect('localhost')

    def show_alert(self, level: int, alerts: List[str]):
        self.publisher.publish('pi-available','level %d alerts %d' % (level, len(alerts)))

