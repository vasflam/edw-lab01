import scrapy
from pprint import pprint
from ..items import ProductItem

PRODUCTS_LIMIT=20

class AtehnoSpider(scrapy.Spider):
    name = 'atehno'
    items = {}

    def start_requests(self):
        url = 'https://atehno.md'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        urls = response.css('article.product-item h3 a::attr(href)').getall()
        # Limit to X items
        for url in urls[0:PRODUCTS_LIMIT]:
            id = url.split("-")[-1]
            if id not in self.items:
                yield scrapy.Request(url, callback=self.parseItem, meta={'id': id})

    def parseItem(self, response):
        elem = response.css('.product-single')
        props = {}
        for row in elem.css('.item_properties-wr table tbody tr'):
            row = row.css('td::text').getall()
            props[row[0].strip()] = row[1].strip()

        images = []
        for img in elem.css('.product-carousel-pages a img::attr(src)').getall():
            images.append(img.strip())

        item = ProductItem(
            title =  elem.css(".product-title::text").get().strip(),
            price =  int(elem.css('.price .amount::text').get().strip()),
            currency =  elem.css('.price .amount .currency::text').get().strip(),
            images = images,
            properties = props,
            source = self.name,
            source_id = response.meta['id'],
        )
        yield item
