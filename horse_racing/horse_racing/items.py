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
    plc = scrapy.Field()
    horse = scrapy.Field()
    jockey = scrapy.Field()
    trainer = scrapy.Field()
    actual_wt = scrapy.Field()
    declar_horse_wt = scrapy.Field()
    draw = scrapy.Field()
    lbw = scrapy.Field()
    running_position = scrapy.Field()
    finish_time = scrapy.Field()
    win_odds = scrapy.Field()
    date_folder = scrapy.Field()
