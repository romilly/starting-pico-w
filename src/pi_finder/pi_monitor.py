"""Check RSS feed to see if Raspberry Pis are currently available to purchase and notify the user if they are.

Read raspilocator.com RSS feed ance a minute.

If there's been availability
- within one minute of the last feed update, show green,
- within five minutes, show amber
- otherwise, show red.


Uses Ports and Adapters, so it's easy to stest and easy to change.
"""
import time

from pi_finder.availability_filter import AvailabilityFilter
from pi_finder.display import Display


try:
    import requests
except:
    import upip
    upip.install('urequests')
    import urequests as requests

from pi_finder.abstract_monitor_classes import RssReader, Clock
from pi_finder.colors import GREEN, RED, YELLOW
from pi_finder.parsed_content import ParsedContent
from pi_finder.simple_parser import SimpleRSSParser


class RecentAvailabilityFilter(AvailabilityFilter):
    def filter_availability(self, content: ParsedContent, time_now: int):
        alerts = [item.alert for item in content.items]
        if len(alerts) == 0: # nothing available
            self.display.show_alert(RED, alerts)
            return
        content_timestamp = time.mktime(content.timestamp)
        if content_timestamp <= time_now-5*60:
            self.display.show_alert(RED, alerts)
        elif content_timestamp <= time_now-60:
            self.display.show_alert(YELLOW, alerts)
        else:
            self.display.show_alert(GREEN, alerts)

# URL = 'https://rpilocator.com/feed/'
URL = 'https://hwlocator.com/feed/'


class RequestingRssReader(RssReader):
    def check_rss_feed(self, time_now: int):
        result = requests.get(URL)
        if result.status_code != 200:
            raise ValueError('request for %s failed' % URL)
        self.parser.parse(result.content.decode('UTF8'), time_now)


class SystemClock(Clock):
    def start_ticking(self):
        while True:
            # so we don't cause problems when testing!
            for i in range(60):
                time.sleep(1)
                print(i)
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


class PrintingDisplay(Display):

    def show_alert(self, level: int, alerts):
        print('alert(%d, %s)' % (level, alerts))


if __name__ == '__main__':
    builder = Builder().with_display(PrintingDisplay())
    builder.build().start_ticking()

