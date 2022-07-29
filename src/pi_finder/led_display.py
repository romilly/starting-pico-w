from machine import Pin
from time import sleep

from pi_finder.display import Display


class LEDDisplay(Display):
    def __init__(self):
        Display.__init__(self)
        self.led = Pin("LED", Pin.OUT)

    def show_alert(self, level: int, alerts): # ignore alerts for now
        for i in range(level):
            self.blink()

    def blink(self):
        self.led.on()
        sleep(0.5)
        self.led.off()
        sleep(0.5)
