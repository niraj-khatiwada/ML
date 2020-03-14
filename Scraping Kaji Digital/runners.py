import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrape_kaji_digital.scrape_kaji_digital.spiders.kaji import KajiSpider

process = CrawlerProcess(settings= get_project_settings())
process.create_crawler(KajiSpider)
process.start()