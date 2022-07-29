from parsed_content import ParsedContent, AvailableItem

ALERT = 'Stock Alert (DE): RPi CM4 - 1GB RAM, 8GB MMC, With Wifi is In Stock at Reichelt'
EPOCH_FOR_27_Jul_2022_11_45_17 = 1658918717
ONE_MINUTE = 60
SIX_MINUTES = 6 * ONE_MINUTE

ITEM_TIMESTAMP = EPOCH_FOR_27_Jul_2022_11_45_17 - 30 # Thirty seconds before the RSS feed timetamp


AVAILABLE_ITEM = AvailableItem(ALERT, 'reichelt', 'DE', 'CM4', ITEM_TIMESTAMP)
EMPTY_CONTENT = ParsedContent(EPOCH_FOR_27_Jul_2022_11_45_17, [])
SAMPLE_CONTENT = ParsedContent(EPOCH_FOR_27_Jul_2022_11_45_17, [AVAILABLE_ITEM])