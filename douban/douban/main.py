from scrapy import cmdline
cmdline.execute('scrapy crawl douban_spider -o DoubanMovie.csv -t csv'.split())