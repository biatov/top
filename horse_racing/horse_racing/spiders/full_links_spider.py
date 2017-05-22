from horse_racing.items import HorseRacingItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import json


class FullLinksSpider(CrawlSpider):
    name = "full_links"
    allowed_domains = ["racing.hkjc.com"]

    with open('page_date.json') as f:
        paginate = json.load(f)[0]['date_pages']

    start_urls = list(map(lambda i: "http://racing.hkjc.com/racing/Info/meeting/Results/english/%s/1" % i, paginate))

    rules = (
        Rule(LinkExtractor(allow=(r'/meeting/Results/english/\w+/\d{8}/\w+/\d+')),
             callback='parse_numeric_pages', follow=True),
    )

    def parse_numeric_pages(self, response):
        item = HorseRacingItem()
        item['numeric_pages'] = response.url
        return item

