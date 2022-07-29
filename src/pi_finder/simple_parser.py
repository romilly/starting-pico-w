from io import StringIO

from pi_finder.parsed_content import AvailableItem, ParsedContent

MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']


class SimpleRSSParser:
    def __init__(self, availability_filter):
        self.availability_filter = availability_filter
        self.feed = ''

    def parse(self, raw_feed: str):
        self.feed = StringIO(raw_feed)
        ts =  self.timestamp()
        items = []
        while (item := self.next_item()) is not None:
            items.append(item)
        return ParsedContent(ts, items)

    def find_tag_contents(self, tag):
        start_tag = '<%s>' % tag
        tag_length = len(start_tag)
        for line in self.feed:
            stripped_line = line.strip()
            if stripped_line.startswith(start_tag):
                return stripped_line[tag_length:-(tag_length+1)]
        return None

    def timestamp(self):
        dt = self.find_tag_contents('lastBuildDate')
        return self.parse_date(dt)

    def month_number(self, month: str):
        result = 1 + MONTHS.index(month)
        if result > 12:
            raise ValueError('Month %s out of range' % month)
        return result

    def parse_date(self, date_string: str):
        _, d, m, y, hms, _ = date_string.split()
        day = int(d)
        month = self.month_number(m)
        year = int(y)
        hour, minute, second  = [int(s) for s in hms.split(':')]
        return year, month, day, hour, minute, second, 0

    def next_item(self):
        alert = self.find_tag_contents('description')
        if alert is None:
            return None
        vendor = self.find_tag_contents('category')
        location = self.find_tag_contents('category')
        product= self.find_tag_contents('category')
        date_string = self.find_tag_contents('pubDate')
        item_timestamp = self.parse_date(date_string)
        return AvailableItem(alert, vendor, location, product, item_timestamp)
