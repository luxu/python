import scrapy

class ABCDevSpider(scrapy.Spider):
    name = 'abcdev'

    def start_requests(self):
        urls = [
            'https://2018.abcdevelopers.org/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        speaker_names = response.css(
            'article h4::text').getall()
        yield {
            'speakers': speaker_names
        }
