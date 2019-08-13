import scrapy
from tutorial.items import TutorialItem




class ImageSpider(scrapy.Spider):

    name = 'imagespider'
    start_urls = [
        'http://www.itpub.net/category/yunwei/'
    ]

    def parse(self, response):
        for article in response.css('article.xin_hover'):
            item = TutorialItem()
            item['link'] = article.css('div.post__thumb a::attr("href")').get()
            item['image_url'] = article.css('div.post__thumb img::attr("data-src")').extract()
            item['title'] = article.css('h3.post__title a::text').get()
            item['author'] = article.css('a.entry-author__name::text').get()
            yield scrapy.Request(item['link'],meta={'item': item}, callback=self.context_parse)


    def context_parse(self,response):
        item = response.meta['item']
        # item['text'] = response.css('div.entry-content p::text').extract()
        item['text'] = response.xpath("//div[@class='entry-content typography-copy']//text()").extract()
        yield item
