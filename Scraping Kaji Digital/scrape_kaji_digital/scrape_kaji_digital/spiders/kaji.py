# -*- coding: utf-8 -*-
import scrapy
import logging

class KajiSpider(scrapy.Spider):
    name = 'kaji'
    allowed_domains = ['www.kajidigital.com']
    start_urls = ['https://www.kajidigital.com/shop']
    def parse(self, response):
        products = response.xpath('//ul[@class="woo-entry-inner clr"]/li[@class="title"]')

        for product in products:
            yield{
                'Product Name': product.xpath(".//a/text()").get(),
                'Product Link': response.urljoin(url = product.xpath(".//a/@href").get())
            }

        next_page = response.urljoin(url = response.xpath('//a[@class="next page-numbers"]/@href').get())

        if next_page:
            yield scrapy.Request(url= next_page, callback= self.parse)
        print("-----------------------------------------------------")
