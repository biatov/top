# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HorseRacingItem(scrapy.Item):
    numeric_pages = scrapy.Field()
    date_pages = scrapy.Field()
    horse_no = scrapy.Field()


class NeedItem(scrapy.Item):
    horse_no = scrapy.Field()
