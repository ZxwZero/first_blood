# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FirstbloodItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = "first_blood"  # 爬虫的名字
    allowed_domains = ['www.qiushibaike.com']  # 允许的域名，是一个列表
    start_urls = ['http://www.qiushibaike.com/']  # 起始url，是一个列表

    url = 'https://www.qiushibaike.com/article/121163920'
    page = 1

    def parse(self, response):
        div_list = response.xpath('//div[class="col1 new-style-col1"]/h1[class="article-title"]')

