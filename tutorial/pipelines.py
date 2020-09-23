# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json
from scrapy.pipelines.images import ImagesPipeline,FilesPipeline
from scrapy.exceptions import DropItem
import scrapy
import pymysql
from urllib.parse import urlparse
import requests
import os
import hashlib
from scrapy.utils.python import to_bytes

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class TutorialPipeline(object):
    #保存数据到mysql

    def open_spider(self, spider):
        print('启动连接数据库')
        self.client=pymysql.Connect(host='localhost',user='opsuser',password='123!@#',database='spider',port=3306)
        self.cursor=self.client.cursor()

    def close_spider(self, spider):
        print('关闭数据库')
        self.cursor.close()
        self.client.close()


    def process_item(self, item, spider):
        sql = "INSERT INTO renren (`title`, `link`, `type`, `point`, `image_path`, `image_url`, `level`, `area`) " \
              "VALUES ('{title}', '{link}', '{type}', '{point}', '{image_path}', '{image_url}', '{level}','{area}')".format(**item)
        print(sql)
        self.cursor.execute(sql)
        self.client.commit()
        print('数据入库')
        return item


class MyImagePipline(ImagesPipeline):

    def get_media_requests(self, item, info):
        # print('准备下载图片 %s' % item['image_url'])
        # print("准备下载图片 \033[0;37;42m\t %s \033[0m" % ' %s' % item['image_url'])
        yield scrapy.Request(item['image_url'],meta={'item':item})

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        item['image_path'] = image_paths[0]
        return item


    def file_path(self, request, response=None, info=None):
        # image_guid = hashlib.sha1(to_bytes(request.url)).hexdigest()
        file_name = urlparse(request.url).path.split('/')[-1]
        # print('命名 '+"renren/%s" % file_name)
        return "renren/%s" % file_name