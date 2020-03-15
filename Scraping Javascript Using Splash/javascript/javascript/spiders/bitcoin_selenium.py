# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector

from selenium import  webdriver
from selenium.webdriver.firefox.options import Options


from shutil import which

class BitcoinSpiderSelenium(scrapy.Spider):
    name = 'selenium'
    allowed_domains = ['www.livecoin.net']
    start_urls = ["https://www.livecoin.net/en"]

    def __init__(self, name=None, **kwargs):

        firefox_options = Options()
        firefox_options.add_argument("--headless")

        executable_path = which("geckodriver")
        driver = webdriver.Firefox(executable_path=executable_path, options= firefox_options)
        driver.get(url = 'https://www.livecoin.net/en')
        driver.set_window_size(1920, 1080)

        find = driver.find_element_by_class_name("filterPanelItem___2z5Gb")
        find.click()

        self.html = driver.page_source
        
        driver.close()

    def parse(self, response):
        resp = Selector(text= self.html)
        for currency in resp.xpath("//div[contains(@class, 'ReactVirtualized__Table__row tableRow___3EtiS ')]"):
            yield{
                'Name': currency.xpath(".//div[1]/div/text()").get(),
                'Volume': currency.xpath(".//div[2]/span/text()").get(),
                'Change': currency.xpath(".//div[4]/span/span/text()").get(),
            }
            print("------------------------")