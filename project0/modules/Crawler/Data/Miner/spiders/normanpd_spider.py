import scrapy


class NormanPDSpider(scrapy.Spider):
    name = "normanpd"

    def start_requests(self):
        urls = [
            'http://normanpd.normanok.gov/content/daily-activity'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        print(response)