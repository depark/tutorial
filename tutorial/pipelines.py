# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json
from scrapy.pipelines.images import ImagesPipeline,FilesPipeline
from scrapy.exceptions import DropItem
import scrapy
import requests
import os
import hashlib
from scrapy.utils.python import to_bytes

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class TutorialPipeline(object):

    def open_spider(self, spider):
        self.file = open('items.json', 'w',encoding='utf-8')

    def close_spider(self, spider):
        self.file.close()


    def process_item(self, item, spider):
        # res = requests.get(item['image_url'][0])
        # image_guid = hashlib.sha1(to_bytes(item['image_url'][0])).hexdigest()
        # item['image_paths'] = 'images/full/%s.jpg' % image_guid
        # if not os.path.exists('images/full/'):
        #     os.makedirs('images/full/')
        # with open(os.path.join(item['image_paths']),'wb') as f:
        #     f.write(res.content)
        line = json.dumps(dict(item))+'\n'
        self.file.write(line)
        return item


class MyImagePipline(ImagesPipeline):

    def get_media_requests(self, item, info):
        for image_url in item['image_url']:
            # print('>>>>>>>>>>>>>>>>>>>>>')
            # print('开始下载图片 '+image_url)
            # print(item)
            # item['image_paths'] = self.file_path(image_url)
            # with open('items_chinaunix.json', 'w',encoding='utf-8') as f:
            #     f.write(json.dumps(dict(item))+'\n')
            yield scrapy.Request(image_url,meta={'item': item})


    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        item['image_paths'] = image_paths
        return item
    #
    # def file_path(self, url, response=None, info=None):
    #     image_guid = hashlib.sha1(to_bytes(url)).hexdigest()
    #     return 'full/%s.jpg' % (image_guid)

    # def file_path(self, request, response=None, info=None):
    #     file_name = request.meta['item']['title'].replace('\r\n\t\t', r'') + ".jpg"
    #     file_name = file_name.replace('/', '_')
    #     return file_name