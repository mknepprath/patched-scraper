import scrapy


class patchedSpider(scrapy.Spider):
    name = 'Patched'
    start_urls = ['https://www.rottentomatoes.com/']

    def parse(self, response):
        print(response.css('#homepage-opening-this-week > h2::text').extract())
