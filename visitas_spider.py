import scrapy

class SpiderSimples(scrapy.Spider):
    name = 'meuspider'
    start_urls = ['http://example.com']

    custom_settings = {
        'DOWNLOAD_DELAY': 1.5,
    }

    def parse(self, response):
        self.log('Visitei o site: %s' % response.url)
        yield {'url': response.url, 'tamanho': len(response.body)}

        proxima_url = 'http://www.google.com.br'
        self.log('Agora vou para: %s' % proxima_url)
        yield scrapy.Request(proxima_url, self.handle_google)

    def handle_google(self, response):
        self.log('Visitei o google via URL: %s' % response.url)
