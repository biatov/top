from horse_racing.items import HorseRacingItem
from scrapy import Request
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import json


class FullLinksSpider(CrawlSpider):
    name = "full_links"
    allowed_domains = ["racing.hkjc.com"]

    try:
        with open('date_pages_ch.json') as f:
            paginate = json.load(f)[0]['date_pages']
    except FileNotFoundError:
            paginate = list()

    start_urls = list(map(lambda i: "http://racing.hkjc.com/racing/Info/meeting/Results/chinese/%s/1" % i, paginate))

    rules = (
        Rule(LinkExtractor(allow=(r'/meeting/Results/chinese/\w+/\d{8}/\w+/\d+')),
             callback='parse_numeric_pages', follow=True),
    )

    def start_requests(self):
        requests = []
        for start_url in self.start_urls:
            requests.append(Request(url=start_url, headers={'Referer': 'http://racing.hkjc.com/'}))
        return requests

    def parse_numeric_pages(self, response):
        item = HorseRacingItem()
        item['numeric_pages'] = response.url
        return item
