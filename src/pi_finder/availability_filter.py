from abc import ABC, abstractmethod

from pi_finder.display import Display
from pi_finder.parsed_content import ParsedContent


class AvailabilityFilter(ABC):
    def __init__(self, display: Display):
        self.display = display

    @abstractmethod
    def filter_availability(self, rss_content: ParsedContent, now):
        pass