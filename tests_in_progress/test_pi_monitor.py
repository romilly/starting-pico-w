import unittest

from hamcrest import assert_that

from pi_finder.colors import GREEN
from pi_finder.pi_monitor import Builder
from starting_pico_w.helpers.color_matcher import shows
from starting_pico_w.helpers.mocks import MockDisplay, MockClock, MockRssReader


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
