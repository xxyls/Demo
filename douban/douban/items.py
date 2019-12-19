# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    serial_number=scrapy.Field()
    #电影名称
    movie_name=scrapy.Field()
    #简介
    introduce=scrapy.Field()
    #宣传海报
    picture=scrapy.Field()
    #评分
    score=scrapy.Field()
    #评论数
    evaluate_number=scrapy.Field()
    #主演
    leadactors=scrapy.Field()
    #电影导演
    director=scrapy.Field()
    #电影类型
    typelist=scrapy.Field()
    #上映时间
    release_time=scrapy.Field()
