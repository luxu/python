# coding: utf-8

from requests import get
from bs4 import BeautifulSoup as bs


def carregar(url):
    return bs(get(url).text, 'lxml')


def parse(soup):
    for caixa in soup.find_all('div', class_='Box-row'):
        base = caixa.find('a')
        texto = caixa.find('a').text
        if '#0' in texto:
            link = base.get('href')
            # print(texto)
            # print(link)
            new_url = 'https://github.com%s' % link
            new_soup = carregar(new_url)
            new_soup.find_all('h3', class_="timeline-comment-header-text")[0]
            author = new_soup.find_all('a', class_="author")[0].text
            hour_comment = new_soup.find_all(
                'h3', class_="timeline-comment-header-text")[0] \
                .find('relative-time').get('datetime')
            for value in new_soup.findAll('td', class_='comment-body'):
                print(value.text)
                print(author,' - ',hour_comment)
                print('*'*66)

if __name__ == '__main__':
    url = 'https://github.com/CollabCodeTech/forum-do-front-ao-end/issues'
    soup = carregar(url)
    parse(soup)
