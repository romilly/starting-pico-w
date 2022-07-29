import unittest

from hamcrest import assert_that, equal_to

from pi_finder.availability_filter import AvailabilityFilter
from pi_finder.parsed_content import ParsedContent, AvailableItem
from pi_finder.pi_monitor import SimpleRSSParser
from starting_pico_w.helpers.sample_rss import SAMPLE_RSS


class MockFilter(AvailabilityFilter):
    def __init__(self):
        AvailabilityFilter.__init__(self, None)
        self.rss_content = None

    def filter_availability(self, rss_content: ParsedContent, now):
        self.rss_content = rss_content


class ParserTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.mock_filter = MockFilter()
        self.parser = SimpleRSSParser(self.mock_filter)

    def test_parses_rss(self):
        self.parser.parse(SAMPLE_RSS)

        assert_that(self.mock_filter.rss_content,
                    equal_to(ParsedContent(timestamp=(2022, 7, 27, 11, 45, 17, 0, 0, -1),
                        items=[AvailableItem(alert='Stock Alert (DE): RPi CM4 - 1GB RAM, 8GB MMC, With Wifi is In Stock at Reichelt',
                                    vendor='reichelt',
                                    location='DE',
                                    product='CM4',
                                    item_timestamp=(2022, 7, 27, 11, 45, 17, 0, 0, -1))])))


if __name__ == '__main__':
    unittest.main()
