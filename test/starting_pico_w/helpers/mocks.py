from pi_finder.abstract_monitor_classes import Clock, Display, RssReader


class MockClock(Clock):
    def start_ticking(self):
        pass


class MockDisplay(Display):
    def show_alert(self, level: int):
        self.color = level


class MockRssReader(RssReader):
    def check_rss_feed(self, param):
        pass
