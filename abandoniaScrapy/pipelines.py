# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import re
import scrapy

from scrapy.pipelines.files import FilesPipeline


class AbandoniaPipeline(object):

    def process_item(self, item, spider):
        return item


class AbandoniaImagesPipeline(FilesPipeline):

    def file_path(self, request, response=None, info=None):
        name = re.match(".+/(?P<name>.+)$", request.url)
        return '%s' % name.groups("name")

    def get_media_requests(self, item, info):
        if hasattr(info.spider, 'downloadimages') and info.spider.downloadimages:
            for image_url in item['screenshots_path']:
                yield scrapy.Request(image_url)
            for image_url in item['titleimage_path']:
                yield scrapy.Request(image_url)

    def item_completed(self, results, item, info):
        return item