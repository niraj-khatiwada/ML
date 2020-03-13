# -*- coding: utf-8 -*-
import scrapy


class CoronaSpider(scrapy.Spider):
    name = 'corona'
    allowed_domains = ['www.worldometers.info']
    start_urls = ['https://www.worldometers.info/coronavirus/']

    def parse(self, response):
        title = response.xpath("//h3/text()").get()
        # countries = response.xpath("//td/a/")
        yield{
            'Title': title
        }

        #Get Individual Country
        # for country in countries:
        #     name = country.xpath(".//text()").get()
        #     link = country.xpath(".//@href").get()
        #     yield {
        #         'Country': name,
        #         'Link': link
        #     }
