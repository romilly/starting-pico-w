from abc import ABC, abstractmethod

from display import colors, BLACK
from parsed_content import ParsedContent
from simple_parser import SimpleRSSParser


class Display(ABC):
    def __init__(self):
        self.color = BLACK

    @abstractmethod
    def show_alert(self, level: int):
        pass

    def __repr__(self):
        return 'a %s showing %s' % (type(self).__name__, colors[self.color])


class AvailabilityFilter(ABC):
    def __init__(self, display: Display):
        self.display = display

    @abstractmethod
    def filter_availability(self, rss_content: ParsedContent, now):
        pass


class RssReader(ABC):
    def __init__(self, parser: SimpleRSSParser):
        self.parser = parser

    @abstractmethod
    def check_rss_feed(self, param):
        pass


class Clock(ABC):
    def __init__(self, rss_reader: RssReader):
        self.rss_reader = rss_reader

    def tick(self, now: int):
        self.rss_reader.check_rss_feed(now)

    @abstractmethod
    def start_ticking(self):
        pass

