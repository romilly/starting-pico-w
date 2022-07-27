from abc import ABC, abstractmethod


class RssReader(ABC):
    @abstractmethod
    def read_rss(self, url: str) -> str:
        pass


class Display(ABC):
    @abstractmethod
    def show_alert(self, level: int):
        pass


class RSSFilter(ABC):
    @abstractmethod
    def filter_rss(self, rss, now):
        pass


class Clock(ABC):
    @abstractmethod
    def start_ticking(self):
        pass

