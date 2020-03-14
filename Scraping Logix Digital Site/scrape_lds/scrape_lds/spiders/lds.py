# -*- coding: utf-8 -*-
import scrapy


class LdsSpider(scrapy.Spider):
    name = 'lds'
    allowed_domains = ['www.lds.com.np/laptop/']
    start_urls = ['http://www.lds.com.np/laptop//']

    def parse(self, response):
        pass
