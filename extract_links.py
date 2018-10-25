# coding: utf-8

import locale

import requests
import rows

# Get the HTML
# url = 'http://wnpp.debian.net/'
url = 'https://www.sindasp.org.br/site/index.php'
html = requests.get(url).content

# Import into rows
# locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
locale.setlocale(locale.LC_ALL, '')
t = rows.import_from_html(html, encoding='utf-8')

# Export it using '.' as thousands separator
# locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
locale.setlocale(locale.LC_ALL, '')
t.export_to_text('sindasp.txt')