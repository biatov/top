import scrapy
from scrapy import Selector
from horse_racing.items import NeedItem


class RunningSpider(scrapy.Spider):
    name = "read_data"
    allowed_domains = ["racing.hkjc.com"]
    start_urls = ["http://racing.hkjc.com/racing/Info/meeting/Results/english/Local"]

    # def parse(self, response):
    #     root = Selector(response)
    #     item = NeedItem()
    #     for each in root.xpath('.//table[@class="tableBorder trBgBlue tdAlignC number12 draggable"]/tbody/tr'):
    #         item['horse_no'] = each.xpath('td').extract()
    #         return item

    def parse(self, response):
        item = NeedItem()
        for each in response.selector.css('table[class*="tableBorder trBgBlue tdAlignC number12 draggable"] tbody'):
            item['horse_no'] = each.xpath('.//tr').extract()
            return item
