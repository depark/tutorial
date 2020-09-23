# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    link = scrapy.Field()
    title = scrapy.Field()
    text = scrapy.Field()
    image_url = scrapy.Field()
    author = scrapy.Field()
    image_paths = scrapy.Field()

class ChinaUniuxItem(scrapy.Item):

    title = scrapy.Field()
    image_path = scrapy.Field()
    desc = scrapy.Field()


class RenRenItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    type = scrapy.Field()
    point = scrapy.Field()
    image_path = scrapy.Field()
    image_url = scrapy.Field()
    level = scrapy.Field()
    area = scrapy.Field()