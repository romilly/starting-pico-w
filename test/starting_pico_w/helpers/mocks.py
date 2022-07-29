from typing import List

from pi_finder.abstract_monitor_classes import Clock, RssReader
from pi_finder.display import Display


class MockClock(Clock):
    def start_ticking(self):
        pass


class MockDisplay(Display):
    def show_alert(self, level: int, alerts: List[str]):
        self.color = level


class MockRssReader(RssReader):
    def check_rss_feed(self, param):
        pass
