import scrapy
from tutorial.items import TutorialItem
# from scrapy.contrib.loader import ItemLoader

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'http://quotes.toscrape.com/tag/humor/',
    ]

    def parse(self, response):
        item = TutorialItem()
        for quote in response.css('div.quote'):
                item['text'] = quote.css('span.text::text').get()
                item['author'] = quote.xpath('span/small/text()').get()
                item['link'] = quote.xpath('span//a//@href').get()
                yield item


        next_page = response.css('li.next a::attr("href")').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)