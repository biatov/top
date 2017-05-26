# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv


class HorseRacingPipeline(object):
    def __init__(self):
        self.file = csv.writer(open('scrapping_data/items_ch.csv', 'w'), quoting=csv.QUOTE_MINIMAL)
        self.file.writerow(
            ['日期', '馬號', '名次', '馬名', '騎師', '練馬師', '實際 負磅', '排位 體重', '檔位', '頭馬 距離',
             '沿途 走位', '完成 時間', '獨贏 賠率']
        )

    def process_item(self, item, spider):
        if spider.name is 'read_data':
            dirty_date = item['date_folder']
            date = '%s/%s/%s' % (dirty_date[:4], dirty_date[4:6], dirty_date[6:8])
            self.file.writerow(
                [date, item['horse_no'], item['plc'], item['horse'], item['jockey'], item['trainer'],
                 item['actual_wt'], item['declar_horse_wt'], item['draw'], item['lbw'], item['running_position'],
                 item['finish_time'], item['win_odds']])
        return item
