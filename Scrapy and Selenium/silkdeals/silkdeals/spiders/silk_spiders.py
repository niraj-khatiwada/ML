# -*- coding: utf-8 -*-
import scrapy
from scrapy_selenium import SeleniumRequest
from selenium import webdriver

class SilkSpidersSpider(scrapy.Spider):
    name = 'silk_spiders'
   
    def start_requests(self):
        
        yield SeleniumRequest(
            url = "https://www.duckduckgo.com",
            wait_time= 3,
            callback = self.parse

        )

    def parse(self, response):
        
        driver = response.meta['driver']
        search_input = driver.find_element_by_xpath("//input[@id='search_form_input_homepage']")
        search_input.send_keys("Hello Word")
        driver.save_screenshot("search.png")



# d = webdriver.Firefox(executable_path= "./geckodriver.exe")

# si = d.find_element_by_xpath("//input[@id='search_form_input_homepage']")
# si.send_keys("Hello Word")
# d.save_screenshot("search.png")