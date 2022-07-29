from hamcrest.core.base_matcher import BaseMatcher, T
from hamcrest.core.description import Description

from pi_finder.display import colors


class ColorMatcher(BaseMatcher):
    def _matches(self, item: T) -> bool:
        return self.expected_color == item.color

    def describe_to(self, description: Description) -> None:
        description.append_text('a display showing %s' % colors[self.expected_color])

    def __init__(self, color):
        self.expected_color = color


def shows(color):
    return ColorMatcher(color)