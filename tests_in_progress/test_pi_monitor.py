import unittest

from hamcrest import assert_that

from abstract_monitor_classes import Display, Clock, RssReader
from display import GREEN, BLACK, colors
from pi_monitor import Builder
from starting_pico_w.helpers.color_matcher import shows


class MockClock(Clock):
    def start_ticking(self):
        pass


class MockDisplay(Display):
    def show_alert(self, level: int):
        self.color = level


class MockRssReader(RssReader):
    def check_rss_feed(self, param):
        pass


class PiMonitorTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.display = MockDisplay()

        builder = Builder().with_clock_class(MockClock).with_rss_reader_class(MockRssReader).with_display(self.display)
        self.runner = builder.build()

    def test_shows_green_if_pi_recently_available(self):
        self.runner.tick(0)
        assert_that(self.display, shows(GREEN))


if __name__ == '__main__':
    unittest.main()
