"""Check RSS feed to see if Raspberry Pis are currently available to purchase and notify the user if they are.

Read raspilocator.com RSS feed ance a minute.

If there's been availability
- within one minute of the last feed update, show green,
- within five minutes, show amber
- otherwise, show red.


Uses Ports and Adapters, so it's easy to stest and easy to change.
"""
import time
try:
    import requests
except:
    import upip
    upip.install('urequests')
    import urequests as requests

from pi_finder.abstract_monitor_classes import RssReader, AvailabilityFilter, Display, Clock
from pi_finder.display import GREEN, RED, YELLOW
from pi_finder.parsed_content import ParsedContent
from pi_finder.simple_parser import SimpleRSSParser


class RecentAvailabilityFilter(AvailabilityFilter):
    def filter_availability(self, content: ParsedContent, time_now: int):
        if len(content.items) == 0: # nothing available
            self.display.show_alert(RED)
            return
        if content.timestamp <= time_now-5*60:
            self.display.show_alert(RED)
        elif content.timestamp <= time_now-60:
            self.display.show_alert(YELLOW)
        else:
            self.display.show_alert(GREEN)

URL = 'https://rpilocator.com/feed/'

class RequestingRssReader(RssReader):
    def check_rss_feed(self, param):
        result = requests.get(URL)
        if result.status_code != 200:
            raise ValueError('request for %s failed' % URL)
        return result.content



class SystemClock(Clock):
    def start_ticking(self):
        while True:
            time.sleep(60) # so we don't cause problems when testing!
            self.rss_reader.check_rss_feed(round(time.time()))


class Builder:
    def __init__(self):
        self.clock_class = SystemClock
        self.rss_reader_class = RequestingRssReader
        self.display = None
        self.rss_filter = None
        self.parser = None
        self.rss_reader = None

    def build(self) -> Clock:
        self.rss_filter = RecentAvailabilityFilter(self.display)
        self.parser = SimpleRSSParser(self.rss_filter)
        self.rss_reader = self.rss_reader_class(self.parser)
        return self.clock_class(self.rss_reader)

    def with_clock_class(self, clock_class):
        self.clock_class = clock_class
        return self

    def with_rss_reader_class(self, rss_reader_class: RssReader):
        self.rss_reader_class =  rss_reader_class
        return self

    def with_display(self, display: Display):
        self.display = display
        return self



