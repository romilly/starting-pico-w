import unittest

from hamcrest import assert_that

from pi_finder.colors import GREEN, YELLOW, RED
from pi_finder.pi_monitor import RecentAvailabilityFilter
from starting_pico_w.helpers.color_matcher import shows
from starting_pico_w.helpers.mocks import MockDisplay
from starting_pico_w.helpers.sample_content import SAMPLE_CONTENT, EPOCH_FOR_27_Jul_2022_11_45_17, ONE_MINUTE, \
    SIX_MINUTES, EMPTY_CONTENT


class FilterTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.display = MockDisplay()
        self.f = RecentAvailabilityFilter(self.display)

    def test_no_items_available_shows_red(self):
        self.f.filter_availability(EMPTY_CONTENT, EPOCH_FOR_27_Jul_2022_11_45_17)
        assert_that(self.display, shows(RED))

    def test_recent_availability_turns_display_green(self):
        self.f.filter_availability(SAMPLE_CONTENT, EPOCH_FOR_27_Jul_2022_11_45_17)
        assert_that(self.display, shows(GREEN))

    def test_older_availability_turns_display_yellow(self):
        self.f.filter_availability(SAMPLE_CONTENT, EPOCH_FOR_27_Jul_2022_11_45_17 + ONE_MINUTE)
        assert_that(self.display, shows(YELLOW))

    def test_older_availability_turns_display_red(self):
        self.f.filter_availability(SAMPLE_CONTENT, EPOCH_FOR_27_Jul_2022_11_45_17 + SIX_MINUTES)
        assert_that(self.display, shows(RED))


if __name__ == '__main__':
    unittest.main()
