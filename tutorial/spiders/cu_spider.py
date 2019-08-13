import scrapy
from tutorial.items import ChinaUniuxItem


class CuSpider(scrapy.Spider):

    name = 'chinaunix'
    start_urls = [
        'http://blog.chinaunix.net/uid/30261776.html'
    ]

    def parse(self, response):
        item = ChinaUniuxItem()
        for cu in response.css('div.Blog_right1_2'):
            item['title'] = cu.css('div.Blog_tit4 a::text').get()
            item['link'] = cu.css('div.Blog_tit4 a::attr("href")').get()
            item['desc'] = cu.css('p.Blog_p10::text').get()
            yield item

        next_url = response.css('li.next a::attr("href")').get()
        if next_url:
            yield response.follow(next_url,self.parse)