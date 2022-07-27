import unittest

from hamcrest import assert_that, equal_to

from abstract_monitor_classes import Display, Clock, RssReader
from display import GREEN
from pi_monitor import Builder, PiMonitor


class MockClock(Clock):
    def __init__(self, monitor: PiMonitor):
        self.monitor = monitor

    def start_ticking(self):
        pass

    def tick(self, now: int):
        self.monitor.check_rss_feed(now)


class MockRssReader(RssReader):
    def read_rss(self, url: str) -> str:
        pass


class MockDisplay(Display):
    def show_alert(self, level: int):
        self.color = level

    def __init__(self):
        self.color = None


class PiMonitorTestCase(unittest.TestCase):
    def setUp(self) -> None:
        rss_reader = MockRssReader()
        self.display = MockDisplay()
        builder = Builder().with_clock(MockClock).with_rss_reader(rss_reader).with_display(self.display)
        self.runner = builder.build_for_computer()

    def test_shows_green_if_pi_recently_available(self):
        self.runner.tick(0)
        assert_that(self.display.color, equal_to(GREEN))


if __name__ == '__main__':
    unittest.main()
