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
    link = scrapy.Field()
    desc = scrapy.Field()