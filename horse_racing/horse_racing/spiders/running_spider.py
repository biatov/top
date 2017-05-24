import scrapy
from scrapy import Request
from horse_racing.items import NeedItem
import json


class RunningSpider(scrapy.Spider):
    name = "read_data"
    allowed_domains = ["racing.hkjc.com"]

    try:
        with open('full_links.json') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = dict()

    start_urls = list(map(lambda x: x['numeric_pages'], data))

    def start_requests(self):
        requests = []
        for start_url in self.start_urls:
            requests.append(Request(url=start_url, headers={'Referer': 'http://racing.hkjc.com/'}))
        return requests

    def parse(self, response):
        for each in response.selector.css('table[class*="tableBorder trBgBlue tdAlignC number12 draggable"] tbody').xpath('tr[re:test(@class, "trBg\w+")]'):
            item = NeedItem()
            item['horse_no'] = each.xpath('td/text()').extract()[1]
            item['plc'] = each.xpath('td/text()').extract()[0]
            item['horse'] = '%s%s' % (each.xpath('td/a/text()').extract()[0], each.xpath('td/text()').extract()[2])
            item['jockey'] = each.xpath('td/a/text()').extract()[1]
            item['trainer'] = each.xpath('td/a/text()').extract()[2]
            item['actual_wt'] = each.xpath('td/text()').extract()[3]
            item['declar_horse_wt'] = each.xpath('td/text()').extract()[4]
            item['draw'] = each.xpath('td/text()').extract()[5]
            item['lbw'] = each.xpath('td/text()').extract()[6]
            item['running_position'] = ' '.join(each.xpath('td')[9].xpath('table/tr/td/text()').extract())
            item['finish_time'] = each.xpath('td/text()').extract()[7]
            item['win_odds'] = each.xpath('td/text()').extract()[8]
            item['date_folder'] = str(response.url).split('/')[-3]
            yield item
