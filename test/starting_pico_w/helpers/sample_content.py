from pi_finder.parsed_content import ParsedContent, AvailableItem

ALERT = 'Stock Alert (DE): RPi CM4 - 1GB RAM, 8GB MMC, With Wifi is In Stock at Reichelt'
EPOCH_FOR_27_Jul_2022_11_45_17 = 1658918717
ONE_MINUTE = 60
SIX_MINUTES = 6 * ONE_MINUTE

FEED_TIMESTAMP = (2022, 7, 27, 11, 45, 17, 0 ,0, -1)
ITEM_TIMESTAMP = (2022, 7, 27, 11, 44, 47, 0, 0, -1) # Thirty seconds before the RSS feed timetamp


AVAILABLE_ITEM = AvailableItem(ALERT, 'reichelt', 'DE', 'CM4', ITEM_TIMESTAMP)
EMPTY_CONTENT = ParsedContent(FEED_TIMESTAMP, [])
SAMPLE_CONTENT = ParsedContent(FEED_TIMESTAMP, [AVAILABLE_ITEM])