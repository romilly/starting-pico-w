from pi_finder.led_display import LEDDisplay
from pi_finder.pi_monitor import Builder
from pi_finder.pico_ntp_client import update_time


def run():
    update_time()
    builder = Builder().with_display(LEDDisplay())
    builder.build().start_ticking()