from collections import namedtuple

ParsedContent = namedtuple('ParsedContent','timestamp items')

AvailableItem = namedtuple('AvailableItem', 'alert vendor location product item_timestamp')