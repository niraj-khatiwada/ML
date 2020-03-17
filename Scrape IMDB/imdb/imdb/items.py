# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ImdbItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    Title = scrapy.Field()
    Genre = scrapy.Field()
    Released_Date = scrapy.Field()
    Runtime = scrapy.Field()
    Rating = scrapy.Field()
    pass