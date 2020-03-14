# -*- coding: utf-8 -*-
import scrapy
import logging
import re

class KajiSpider(scrapy.Spider):
    name = 'kaji'
    allowed_domains = ['www.kajidigital.com']
    page_num = 1
    headers = { 'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Mobile Safari/537.36' }

    def start_requests(self):
        yield scrapy.Request(url= 'https://kajidigital.com/shop/?product-page=1', callback= self.parse, 
        headers= KajiSpider.headers)

    def parse(self, response):

        for product in response.xpath('//ul[@class="woo-entry-inner clr"]'):
            yield{
                'Product Name': product.xpath(".//li[@class='title']/a/text()").get(),
                'Product Link': response.urljoin(url = product.xpath(".//li[@class='title']/a/@href").get()),
                'Product-Image': response.xpath(".//li[@class='image-wrap']/div/a/noscript/img[@class='woo-entry-image-main']/@src").get(),
                # "User-Agent": response.request.headers['User-Agent']
            }

        next_page = response.xpath("//ul[@class='page-numbers']/li/a/@href").get()

        pattern = "\S*product-page=\d\S*"
        print("Regexxxxxxxxxxxxxx", re.findall(pattern, next_page))
        page_number = len(re.findall(pattern, next_page))
        # print(next_page)

        if KajiSpider.page_num <= page_number:
            yield scrapy.Request(url = response.urljoin(next_page), callback= self.parse, dont_filter= True,  headers= KajiSpider.headers)
            KajiSpider.page_num += 1


       
        print("-----------------------------------------------------")
