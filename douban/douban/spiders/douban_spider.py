# -*- coding: utf-8 -*-
import scrapy
from ..items import DoubanItem

class DoubanSpiderSpider(scrapy.Spider):
    #爬虫名字
    name = 'douban_spider'
    #允许的域名
    allowed_domains = ['movie.douban.com']
    #入口url,扔到调度器里面去
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        movie_list=response.xpath('//div[@class="article"]//ol[@class="grid_view"]/li')
        for i_item in movie_list:
            douban_item=DoubanItem()
            douban_item['serial_number']=i_item.xpath('.//div[@class="item"]//em/text()').extract_first()
            douban_item['movie_name']=i_item.xpath('.//div[@class="info"]/div[@class="hd"]/a/span/text()').extract_first()
            douban_item['director']=i_item.xpath('.//div[@class="info"]/div[@class="bd"]/p[1]/text()').extract_first()
            douban_item['introduce']=i_item.xpath('.//div[@class="info"]/div[@class="bd"]/p[@class="quote"]/span/text()').extract_first()
            douban_item['release_time']=i_item.xpath('.//div[@class="info"]/div[@class="bd"]/p[1]/text()').extract()
            douban_item['score']=i_item.xpath('.//span[@class="rating_num"]/text()').extract_first()
            douban_item['evaluate_number']=i_item.xpath('.//div[@class="star"]/span[4]/text()').extract_first()
            douban_item['picture']=i_item.xpath('.//div[@class="pic"]/a/img/@src').extract_first()
            yield douban_item
        next_link=response.xpath('//span[@class="next"]/link/@href').extract()
        if next_link:
            next_link=next_link[0]
            yield scrapy.Request("https://movie.douban.com/top250"+next_link,callback=self.parse)


