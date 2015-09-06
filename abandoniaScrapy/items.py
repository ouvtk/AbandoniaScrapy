# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GameItem(scrapy.Item):

    name = scrapy.Field()
    year = scrapy.Field()
    tags = scrapy.Field()
    rating = scrapy.Field()
    gamepage_link = scrapy.Field()
    download_link = scrapy.Field()
    titleimage_path = scrapy.Field()
    screenshots_path = scrapy.Field()
