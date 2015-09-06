import logging

import scrapy

from abandoniaScrapy.items import GameItem
from abandoniaScrapy.spiders.abandoniaspider import AbandoniaSpider

class AbandoniaImageSpider(AbandoniaSpider):
    """
    Abandonia.com all games crawler.
    Adds title image and screenshots downloading marker to choose pipeline
    """

    name = "abandonia_images"
    downloadimages = True