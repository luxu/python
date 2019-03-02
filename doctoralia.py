# coding=utf-8

from scrapy import Request, Spider

'''
para "aliviar" pros servidores usar:
```scrapy runspider doctoralia.py -s HTTPCACHE_ENABLED=1```
```scrapy runspider doctoralia.py -s HTTPCACHE_ENABLED=1 -o <nome-de-saida>.csv ```
```scrapy runspider doctoralia.py -s HTTPCACHE_ENABLED=1 -s CLOSESPIDER ITEMCOUNT=500 -o <nome-de-saida>.csv ```

'''
# Nome, descrição, imagem, endereço, foto, especialidade


class DoctoraliaSpider(Spider):
    name = 'doctoralia'

    start_urls = [
        'https://www.doctoralia.com.br/medico-clinico-geral/sao-paulo',
        # 'https://www.doctoralia.com.br/local/rio-de-janeiro-rj/medico-clinico-geral'
    ]

    def parse(self, response):
        links = response.css('a.rank-element-name__link::attr(href) ').extract()
        for link in links:
            yield Request(
                url=link,
                callback=self.parse_novo
            )
            break

    def parse_novo(self, response):
        # trago toda a caixa onde tem as infos
        boxes = response.css('#profile-info')
        # crio o laço para separar as coisas
        caixas = boxes.xpath('./div[contains(@data-id, "doctor-address-item")]')
        for caixa in caixas:
            self.endereco_details(caixa)

    def endereco_details(self, response):
        endereco = response.xpath(
            './/span[contains(@itemprop, "streetAddress")]//text()'
        ).extract()
        self.log(endereco[1].strip())

        especialidade = response.xpath(
            '//span[contains(@class, "text-muted")]//text()'
        ).extract_first()

        response.xpath(
            '//h5[contains(@class, "offset-0")]//following-sibling::span'
        )[-1].get()

        self.log(especialidade)

        '''
        for box in boxes:
            # pego todos os endereços da caixa
            enderecos = box.xpath('.//h5[contains(@class, "offset-0")]')
        # self.log(response.url)
        # caixas = response.xpath('//div[contains(@data-id, "doctor-address-item")]')
        nros = response.xpath(
            '//div[contains(@data-id, "doctor-address-item")]//@data-address-id'
            ).extract()
        for nro in set(nros):
            option = u'address-{}-services'.format(nro)
            self.log(option)
            espec = response.xpath(
                u'.//div[contains(@data-id, {})] \
                //p[contains(@class, "offset-top-1 offset-bottom-0")]//text()'.format(option)
            ).extract()
            for sep in espec:
                self.log(sep.strip())
            self.log('-'*66)
        caixas = response.xpath('//div[contains(@itemprop, "address")]')
        for caixa in caixas:
            novo = caixa.xpath(
                '//span[contains(@itemprop, "streetAddress")]//text()'
            ).extract()

            telefone = caixa.xpath(
                '//div[contains(@class, "well well-white")]//a/@href'
            ).extract()

            endereco = caixa.xpath(
                './/span[contains(@itemprop, "streetAddress")]//span//text()'
            ).extract()

            bairro = caixa.xpath(
                './/span[contains(@itemprop, "streetAddress")]//a//text()'
            ).extract()

            cidade = caixa.xpath(
                './/span[contains(@itemprop, "streetAddress")]//text()'
            ).extract()

            localidade = caixa.css('.text-muted::text')[1].extract()

            servicos = caixa.xpath(
                '//div[contains(@data-id, "address-217201-services")]//p//text()'
            ).extract()

            self.log(
                u'ENDEREÇO: {}{},{}{}\n{}'.format(
                    localidade,
                    endereco[0].strip(),
                    bairro[0].strip(),
                    telefone,
                    ' '.join(cidade[-1].split()),
                    '*'*100
                )
            )

            service = ''
            for servico in servicos:
                servico = u'{}{}'.format(servico.strip(),'\n')
                service += servico

            self.log(
                u'SERVIÇOS: {}\n{}'.format(
                    service,
                    '-'*100
                )
            )
        '''
