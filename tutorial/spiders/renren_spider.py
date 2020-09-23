# encoding: utf-8
'''
#-------------------------------------------------------------------#
#                   CONFIDENTIAL --- CUSTOM STUDIOS                 #     
#-------------------------------------------------------------------#
#                                                                   #
#                   @Project Name : tutorial                 #
#                                                                   #
#                   @File Name    : renren_spider.py                      #
#                                                                   #
#                   @Programmer   : liuhua.yang                     #
#                                                                   #  
#                   @Start Date   : 2020/9/23 14:37                 #
#                                                                   #
#                   @Last Update  : 2020/9/23 14:37                 #
#                                                                   #
#-------------------------------------------------------------------#
# Classes:                                                          #
#                                                                   #
#-------------------------------------------------------------------#
'''

import scrapy
from tutorial.items import RenRenItem

class RenRenSpider(scrapy.Spider):

    name = 'renren'
    domain='http://www.rrys2020.com'
    start_urls = [
        'http://www.rrys2020.com/resourcelist'
    ]

    def start_requests(self):
        for i in range(1,3):
            print('开始采集第 %d 页' % i)
            url='http://www.rrys2020.com/resourcelist/?page='+str(i)
            yield scrapy.Request(url,self.parse)

    def parse(self, response, **kwargs):
        resource_list=response.xpath('/html/body/div[2]/div/div[2]/div/div[4]/ul/li')
        for resource in resource_list:
            # print('采集第 %d 条数据' % index)
            item=RenRenItem()
            item['link'] =self.domain+resource.xpath('div[1]/a/@href').get()
            p1=resource.xpath('div[1]/a/span/em/text()').get()
            p2=resource.xpath('div[1]/a/span/text()').get()
            item['point'] = p1+p2
            yield scrapy.Request(item['link'],meta={'item':item},callback=self.parse_details)

    def parse_details(self, response):
        item=response.meta['item']
        item['title'] = response.xpath('/html/body/div[2]/div/div[1]/div[1]/div[1]/h2/text()').get().replace('\n','').replace(' ','')
        item['image_url'] = response.xpath('/html/body/div[2]/div/div[1]/div[1]/div[2]/div[1]/div[1]/a/img/@src').get()
        item['type'] = response.xpath('/html/body/div[2]/div/div[1]/div[1]/div[2]/div[2]/ul/li[6]/strong/text()').get()
        item['area'] = response.xpath('/html/body/div[2]/div/div[1]/div[1]/div[2]/div[2]/ul/li[2]/strong/text()').get()
        item['level'] = self.Relevel(response.xpath('/html/body/div[2]/div/div[1]/div[1]/div[2]/div[2]/div/img/@src').get())
        yield item

    def Relevel(self,src):
        Level=''
        if src:
            img_name=src.split('/')[-1]
            if img_name=='a-big-1.png':
                Level='A'
            elif img_name=='b-big-1.png':
                Level='B'
            elif img_name=='c-big-1.png':
                Level='C'
            elif img_name=='d-big-1.png':
                Level='D'
            elif img_name=='e-big-1.png':
                Level='E'
        return Level