from html.parser import HTMLParser
from urllib.request import urlopen
from urllib import parse
import sys
import os
from pprint import pprint

# We are going to create a class called LinkParser that inherits some
# methods from HTMLParser which is why it is passed into the definition
# Nós vamos criar um class chamada LinkParser que herda alguns
# métodos de HTMLParser é por isso que é passado para a definição
class LinkParser(HTMLParser):

    # This is a function that HTMLParser normally has
    # but we are adding some functionality to it
    # Esta é uma função que HTMLParser normalmente tem
    # mas estamos adicionando algumas funcionalidades para isso
    def handle_starttag(self, tag, attrs):
        # We are looking for the begining of a link. Links normally look
        # like <a href="www.someurl.com"></a>
        # Estamos procurando o começo de um link. Links normalmente parecem
        # like <a href="www.someurl.com"></a>
        if tag == 'a':
            for (key, value) in attrs:
                if key == 'href':
                    # We are grabbing the new URL. We are also adding the
                    # base URL to it. For example:
                    # www.netinstructions.com is the base and
                    # somepage.html is the new URL (a relative URL)
                    #
                    # We combine a relative URL with the base URL to create
                    # an absolute URL like:
                    # www.netinstructions.com/somepage.html
                    # Estamos pegando a URL nova. Nós também estamos adicionando a
                    # URL base para isso. Por exemplo:
                    # www.netinstructions.com é a base e
                    # somepage.html é a nova URL (URL relativa)
                    #
                    # Nós combinamos uma URL relativa com a URL base para criar
                    # uma URL absoluta
                    # www.netinstructions.com/somepage.html
                    newUrl = parse.urljoin(self.baseUrl, value)
                    # And add it to our colection of links:
                    # E adicioná-la à nossa coleção de links
                    self.links = self.links + [newUrl]

    # This is a new function that we are creating to get links
    # that our spider() function will call
    # Esta é uma nova função que estamos criando para obter links
    # que nossa function spider() chamará
    def getLinks(self, url):
        self.links = []
        # Remember the base URL which will be important when creating
        # absolute URLs
        # Lembre-se da URL base que será importante ao criar
        # URLs absoluta
        self.baseUrl = url
        # Use the urlopen function from the standard Python 3 library
        # Use a function urlopen da biblioteca padrão do Python 3
        response = urlopen(url)
        # print(response.getheader('Content-Type'))
        # import pdb; pdb.set_trace()
        # Make sure that we are looking at HTML and not other things that
        # are floating around on the internet (such as
        # JavaScript files, CSS, or .PDFs for example)
        # Certifique-se de que estamos olhando para HTML e não outras coisas que
        # estão flutuando na internet (como
        # JavaScript files, CSS, or .PDFs por exemplo)
        if response.getheader('Content-Type').startswith('text/html'):
            htmlBytes = response.read()
            # Note that feed() handles Strings well, but not bytes
            # (A change from Python 2.x to Python 3.x)
            # Observe que feed() handles Strings bem, mas não bytes
            # (Uma mudança do Python 2.x to Python 3.x)
            htmlString = htmlBytes.decode("utf-8")
            self.feed(htmlString)
            return htmlString, self.links
        else:
            return "",[]

# And finally here is our spider. It takes in an URL, a word to find,
# and the number of pages to search through before giving up
# E finalmente aqui está nossa spider. Pega em uma URL, uma palavra para encontrar,
# e o número de páginas para procurar antes de desistir
def spider(url, word, maxPages) -> str:
    pagesToVisit = [url]
    # pagesToVisit = url
    numberVisited = 0
    foundWord = False
    # The main loop. Create a LinkParser and get all the links on the page.
    # Also search the page for the word or string
    # In our getLinks function we return the web page
    # (this is useful for searching for the word)
    # and we return a set of links from that web page
    # (this is useful for where to go next)
    # TRADUÇÃO PARA O PORTUGUÊS
    # O loop principal. Crie um LinkParser e obtenha todos os links na página.
    # Também procure na página a palavra ou string
    # Na nossa function getLinks nós retornamos a página web
    # e nós retornamos um conjunto de links dessa página da web
    # (isso é útil para onde ir em seguida)
    while numberVisited < int(maxPages) and pagesToVisit != [] and not foundWord:
        numberVisited = numberVisited +1
        # Start from the beginning of our collection of pages to visit:
        # Comece do início de nossa coleção de páginas para visitar:
        url = pagesToVisit[0]
        # url = pagesToVisit
        pagesToVisit = pagesToVisit[1:]
        try:
            print(numberVisited, "Visiting:", url)
            parser = LinkParser()
            data, links = parser.getLinks(url)
            if data.find(word)>-1:
                foundWord = True
                # Add the pages that we visited to the end of our collection
                # of pages to visit:
                # Adicione as páginas que visitamos ao final de nossa coleção
                # de páginas para visitar
                pagesToVisit = pagesToVisit + links
                sucesso = " **Success!**"
                print(u'{}\nA palavra {} foi encontrado na URL.: {}'.format(sucesso,word,url))
                foundWord = False
        except:
            # print(" **Failed!**")
            continue
        # if foundWord:
        #     return "A palavra", word, "foi encontrado em ", url
        #     foundWord = False
        # else:
        #     return "Nenhuma palavra encontrada"
    return ""


def spider2(url, word, maxPages):
    numberVisited = 0
    parser = LinkParser()
    searchWord = []
    data, links = parser.getLinks(url)
    qtd_links_url = len(links)
    print(u'Quantidade de links encontrados na {}: {}'.format(url,qtd_links_url))
    qtd_pages = int(maxPages)
    numberVisited = 0
    if qtd_links_url < qtd_pages:
        qtd_pages = qtd_links_url
    for i in range(qtd_pages):
        try:
            if links[i].startswith('http'):
                numberVisited = numberVisited +1
                print(numberVisited, "Visiting:", links[i])
                parser = LinkParser()
                data, linkss = parser.getLinks(links[i])
                if word in data:
                    searchWord.append(links[i])
        except:
            continue

    return searchWord

if __name__ == '__main__':
    os.system('cls')
    if len(sys.argv) < 2:
        print('-'*66)
        print('Tem que passar um site para poder pegar os links dele')
        print('ex.: WebSpider.py "http://www.uol.com.br","carnaval", 200')
        print('-'*66)
        sys.exit()
    else:
        url = u'{}'.format(sys.argv[1])
        word = u'{}'.format(sys.argv[2])
        maxPages = sys.argv[3]
        resultSite = spider2(url, word, maxPages)
        print(u'{}\nQuantidade de links que tem a palavra: {} é: {}'
            .format('-'*66,word,len(resultSite)))
        pprint(resultSite)
        # print(url, word, maxPages)
        # spider(url, word, maxPages)
        # url_s = u'https://{}'.format(sys.argv[1])
        # print(url_s, word, maxPages)
        # spider(url_s, word, maxPages)
