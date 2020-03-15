# -*- coding: utf-8 -*-
import scrapy

from  scrapy_selenium import SeleniumRequest
from selenium import webdriver

from shutil import which

class SlickSpider(scrapy.Spider):
    name = 'slick'

    def start_requests(self):

        yield SeleniumRequest(
            url = "https://slickdeals.net/laptop-deals",
            wait_time= 4,
            screenshot= True,
            callback = self.parse
        )

    def parse(self, response):
        for laptop in response.xpath("//div[@class='itemImageLink']"):
            yield{
                'Title': laptop.xpath(".//a/text()").get(),
                'Link': laptop.xpath(".//a/@href").get(),
            }

        next_page = response.xpath("//a[@data-role='next-page']/@href").get()

        if next_page:
            absolute_url = response.urljoin(next_page)
            yield SeleniumRequest(
                url= absolute_url,
                wait_time= 3,
                callback = self.parse
            )






# path = which("geckodriver")
# driver = webdriver.Firefox(executable_path= path)

# driver.fins