# -*- coding: utf-8 -*-
import scrapy
import logging
from scrapy_djan

class CoronaSpider(scrapy.Spider):
    name = 'corona'
    allowed_domains = ['www.worldometers.info']
    start_urls = ['https://www.worldometers.info/coronavirus/']

    def parse(self, response):
        title = response.xpath("//h3/text()").get()
        countries = response.xpath("//table[@id='main_table_countries']/tbody/tr/td[1]")

        for country in countries:
            country_name = country.xpath(".//a/text()").get()
            country_link = country.xpath(".//a/@href").get()

            yield response.follow(url = country_link, callback = self.country_parse, meta={'Country': country_name, 'Country_Link': country_link})


    def country_parse(self, response):
        country_name = response.request.meta['Country']
        infected_patients = response.xpath("//div[@class='panel_front']")
        for i in infected_patients:
            title = i.xpath(".//div[2]/text()").get()
            patient_number = i.xpath(".//div[1]/text()").get()

            yield {
                'Country': country_name,
                'Title': title,
                'Infected Patient Number': patient_number

            }


