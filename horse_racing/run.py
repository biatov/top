import subprocess

subprocess.call('scrapy crawl date_pages -o date_pages.json', shell=True)
subprocess.call('scrapy crawl full_links -o full_links.json', shell=True)
subprocess.call('scrapy crawl read_data', shell=True)
