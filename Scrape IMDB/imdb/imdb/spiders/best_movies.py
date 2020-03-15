# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BestMoviesSpider(CrawlSpider):
    name = 'best_movies'
    allowed_domains = ['www.imdb.com']

    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36 Edg/80.0.361.66"

    def start_requests(self):
        yield scrapy.Request(url= 'https://www.imdb.com/chart/top/?ref_=nv_mv_250', headers= {'User-Agent': self.user_agent})

    rules = (
        Rule(LinkExtractor(restrict_xpaths= "//div[@class='lister']/table/tbody/tr/td[@class='titleColumn']/a"), callback='parse_item', follow=True, process_request= 'set_user_agent'),
    )

    def set_user_agent(self, request):
        request.headers['User-Agent'] = self.user_agent
        return request


    def parse_item(self, response):
        yield{
            'Title': response.xpath("//div[@class='title_wrapper']/h1/text()").get(),
            'Genre': response.xpath("//div[@class='title_wrapper']/div[@class='subtext']/a[1]/text()").get(),
            'Released Date': response.xpath("//div[@class='title_wrapper']/div[@class='subtext']/a[2]/text()").get().strip(),
            'Runtime': response.xpath("//div[@class='title_wrapper']/div[@class='subtext']/time/text()").get().strip(),
            'Rating': response.xpath("//div[@class='ratingValue']/strong/span/text()").get(),
            }
        print("----------------------------------------------")