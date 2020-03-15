# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest


class BitcoinSpider(scrapy.Spider):
    name = 'bitcoin'
    allowed_domains = ['www.livecoin.net']
    # Slash Scripts

    script = '''
            function main(splash, args)
                splash.private_mode_enabled = FALSE
                url = args.url
                assert(splash:go(url))
                assert(splash:wait(3))
                
                russian = assert(splash:select_all(".filterPanelItem___2z5Gb"))
                russian[5]:mouse_click()
                assert(splash:wait(1))
                splash:set_viewport_full()
                
                return splash:html()
            
            end
            '''

    #Set start URLS
    def start_requests(self):
        yield SplashRequest(url='https://www.livecoin.net/en', callback= self.parse, endpoint= "execute", args={'lua_source': self.script} )

    def parse(self, response):
        for currency in response.xpath("//div[contains(@class, 'ReactVirtualized__Table__row tableRow___3EtiS ')]"):
            yield{
                'Name': currency.xpath(".//div[1]/div/text()").get(),
                'Volume': currency.xpath(".//div[2]/span/text()").get(),
                'Change': currency.xpath(".//div[4]/span/span/text()").get(),
            }
            print("------------------------")