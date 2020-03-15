# -*- coding: utf-8 -*-
import scrapy
from scrapy_selenium import SeleniumRequest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from scrapy.selector import Selector

class SilkSpidersSpider(scrapy.Spider):
    name = 'silk_spiders'
   
    def start_requests(self):
        yield SeleniumRequest(
            url = "https://www.duckduckgo.com",
            wait_time= 5,
            screenshot= True,
            callback = self.parse

        )

    def parse(self, response):
        
        driver = response.meta['driver']
        search_input = driver.find_element_by_xpath("//input[@id='search_form_input_homepage']")
        search_input.send_keys("Hello Word")
        btn = driver.find_element_by_xpath("//input[@id='search_button_homepage']")   
        btn.click()  

        html = driver.page_source
        response_object = Selector(text= html)
        links = response_object.xpath("//div[@class='result__extras__url']")
        for link in links:
            yield{
                'Link': link.xpath(".//a/@href").get()
            }
        # driver.save_screenshot("hashas.png")



# d = webdriver.Firefox(executable_path= "./geckodriver.exe")

# si = d.find_element_by_xpath("//input[@id='search_form_input_homepage']")
# si.send_keys("Hello Word") 
# d.save_screenshot("search.png")

# si.click
# d.save_screenshot()