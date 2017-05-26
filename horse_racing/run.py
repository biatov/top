import subprocess

subprocess.call('scrapy crawl date_pages -o date_pages_ch.json', shell=True)
subprocess.call('scrapy crawl full_links -o full_links_ch.json', shell=True)
subprocess.call('scrapy crawl read_data', shell=True)
