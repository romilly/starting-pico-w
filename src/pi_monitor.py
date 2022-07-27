"""Check RSS feed to see if Rapsberry Pis are currently vailable to purchase and notify the user if they are.

Read raspilocator.com RSS feed ance a minute.

If there's been availability
- within five  minutes of the last feed update, show green,
- within thirty minute, show amber
- otherwise, show red.


Uses Ports and Adapters, so it's easy to stest and easy to change.
"""
import time

from abstract_monitor_classes import RssReader, RSSFilter, Display, Clock
from display import GREEN


class TimeSensitiveFilter(RSSFilter):
    def __init__(self, display: Display):
        self.display = display

    def filter_rss(self, rss, time_now: int):
        self.display.show_alert(GREEN)


class RequestingRssReader(RssReader):
    def read_rss(self, url: str) -> str:
        pass


class LEDDisplay(Display):
    def show_alert(self, level: int):
        pass


class PiMonitor:
    URL = 'https://rpilocator.com/feed/'

    def __init__(self, rss_reader: RssReader, rss_filter: RSSFilter):
        self.rss_reader = rss_reader
        self.rss_filter = rss_filter

    def check_rss_feed(self, time_now: int):
        rss = self.rss_reader.read_rss(self.URL)
        self.rss_filter.filter_rss(rss, time_now)


class SystemClock(Clock):
    def start_ticking(self):
        while True:
            self.monitor.check_rss_feed(round(time.time()))
            time.sleep(60)

    def __init__(self, monitor: PiMonitor):
        self.monitor = monitor


class Builder:
    def __init__(self):
        self.clock_class = SystemClock
        self.rss_reader = RequestingRssReader()
        self.display = LEDDisplay()

    def build_for_computer(self) -> Clock:
        return self.clock_class(PiMonitor(self.rss_reader, TimeSensitiveFilter(self.display)))

    def with_clock(self, clock_class):
        self.clock_class = clock_class
        return self

    def with_rss_reader(self, rss_reader: RssReader):
        self.rss_reader =  rss_reader
        return self

    def with_display(self, display: Display):
        self.display = display
        return self




