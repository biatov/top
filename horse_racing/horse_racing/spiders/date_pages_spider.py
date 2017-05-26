import scrapy
from scrapy import Selector
from horse_racing.items import HorseRacingItem


class DatePagesSpider(scrapy.Spider):
    name = "date_pages"
    allowed_domains = ["racing.hkjc.com"]
    start_urls = ["http://racing.hkjc.com/racing/Info/meeting/Results/chinese/Local"]

    def parse(self, response):
        root = Selector(response)
        item = HorseRacingItem()
        for each in root.xpath('//select[@id="raceDateSelect"]'):
            item['date_pages'] = each.xpath('.//option/@value').extract()
            return item
