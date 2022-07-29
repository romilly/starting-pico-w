from pi_finder.simple_parser import SimpleRSSParser

try:
    from abc import ABC, abstractmethod
except:
    from mp.abc import ABC, abstractmethod


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

