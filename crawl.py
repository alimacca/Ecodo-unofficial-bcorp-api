import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class BCorpItem(scrapy.Item):
    name = scrapy.Field()
    url = scrapy.Field()
    website = scrapy.Field()
    bscore = scrapy.Field()
    location = scrapy.Field()
    description = scrapy.Field()

class BCorpSpider(CrawlSpider):
    name = 'bcorp'
    allowed_domains = ['bcorporation.net']
    start_urls = ['https://www.bcorporation.net/en-us/find-a-b-corp']

    rules = (
        Rule(LinkExtractor(allow=('/en-us/find-a-b-corp/')), callback='parse_bcorp', follow=True),
        Rule(LinkExtractor(allow=('/en-us/find-a-b-corp/page/\d+')), follow=True)
    )

    def parse_bcorp(self, response):
        bcorp = BCorpItem()
