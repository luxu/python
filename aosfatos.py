from scrapy import Request, Spider

'''
para "aliviar" pros servidores usar:
```scrapy runspider <arquivo>.py -s HTTPCACHE_ENABLED=1 -o <nome-de-saida>.csv ```
```scrapy runspider <arquivo>.py -s HTTPCACHE_ENABLED=1 -s CLOSESPIDER ITEMCOUNT=500 -o <nome-de-saida>.csv ```

'''

class AosFatosSpider(Spider):
    name = 'aos_fatos'

    start_urls = [
        'https://aosfatos.org/'
    ]

    def parse(self, response):
        links = response.xpath(
            '//nav//ul//li/a[re:test(@href, "checamos")]/@href'
        ).getall()
        for link in links:
            yield Request(
                response.urljoin(link),
                callback=self.parse_category
            )

    def parse_category(self, response):
        news = response.css('.card::attr(href)').getall()
        for new_url in news:
            yield Request(
                response.urljoin(new_url),
                callback=self.parse_new
            )

        pages_url = response.css('.pagination a::attr(href)').getall()
        for page in pages_url:
            yield Request(
                response.urljoin(page),
                callback=self.parse_category,
            )

    def parse_new(self, response):
        title = response.css('article h1::text').get()
        date = ' '.join(response.css('p.publish_date::text').get().split())
        quotes = response.css('article blockquote p')
        for quote in quotes:
            quote_text = quote.css('::text').get()
            status = quote.xpath(
                './parent::blockquote/preceding-sibling::figure//figcaption/text()'
            ).get()
        yield {
            'title': title,
            'date': date,
            'quote_text' : quote_text,
            'status' : status,
            'url': response.url
        }
