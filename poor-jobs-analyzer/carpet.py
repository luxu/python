import csv
import os
import re
from concurrent import futures
from concurrent.futures import ThreadPoolExecutor
from html.parser import HTMLParser
from operator import itemgetter
from urllib import request
from urllib.error import HTTPError


def csv_to_list(filename: str) -> list:
    """Receive an csv filename and returns rows of file with an list"""
    with open(filename) as csv_file:
        reader = csv.DictReader(csv_file)
        csv_data = [line for line in reader]
    return csv_data


def get_files_in_directory(directory: str) -> list:
    """Receive an directory and returns an list of filenames in directory"""
    full_filenames = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            filename = os.path.join(root, file)
            full_filenames.append(filename)

    return full_filenames


def evaluate_job_file(filename: str, metrics: list) -> tuple:
    """
    Receive an filename and metrics (list of dicts containing metrics)
    and return an poor level and words with match
    Receber um nome de arquivo e métricas (lista de dicts contendo métricas)
    e retornar um nível fraco e palavras com correspondência
    """
    poor_level = 0
    words = []

    with open(filename, encoding="utf8") as file:
        content = file.read()

    for metric in metrics:
        lower_term = metric['Terms'].lower()
        pattern = r'\b{}\b'.format(lower_term)
        lower_content = content.lower()

        if re.search(pattern, lower_content):
            poor_level += int(metric['Poor level'])
            words.append(metric['Terms'])

    return poor_level, words


def order_by_key(results_list: list, order_key: str) -> list:
    """Receive an list of dicts and return ordered list by order_key"""
    reordered_results = sorted(results_list, key=itemgetter(order_key))
    return reordered_results


def get_pyjob_codes(url='http://www.pyjobs.com.br/', page=1) -> list:
    """Receive and url and page of pyjobs and return list of codes of jobs"""
    job_codes = []
    full_url = '{}?page={}'.format(url, page)

    try:
        response = request.urlopen(full_url)
    except HTTPError as exc:
        print('Error "{}" when get "{}"'.format(exc.msg, full_url))
        return job_codes

    pattern = r'href="/job/([0-9]+)/"'
    for line in response:
        decoded_line = line.decode('utf-8')
        match = re.search(pattern, decoded_line)
        if match:
            job_code = match.group(1)
            job_codes.append(job_code)

    return job_codes

class ParsePyjobsHTML(HTMLParser):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.parsed_content = ""
        self.capture_content = False

    def handle_starttag(self, tag, attrs):
        if tag == 'section':
            self.capture_content = True

    def handle_endtag(self, tag):
        if tag == 'section':
            self.capture_content = False

    def handle_data(self, data):
        if self.capture_content:
            self.parsed_content += data


def get_pyjob_content(pyjob_code: str) -> str:
    """Get an pyjob_code and return your description"""
    job_url = 'http://www.pyjobs.com.br/job/{}/'
    url = job_url.format(pyjob_code)

    try:
        response = request.urlopen(url)
    except HTTPError as exc:
        print('Error "{}" when get "{}"'.format(exc.msg, url))
        return (pyjob_code, None)

    response_content = response.read().decode('utf-8')

    parser = ParsePyjobsHTML()
    parser.feed(response_content)
    return (pyjob_code, parser.parsed_content)


def async_get_pyjob_codes(initial_page: int, final_page: int, max_workers=10) -> list:
    """Get initial_page and final_page of pyjobs and return a list pyjob_codes from pages"""
    print('Running async_get_pyjob_codes...')
    pyjob_codes = []
    pages = range(initial_page, final_page + 1)
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        to_do_map = {}
        for page in pages:
            future = executor.submit(get_pyjob_codes, page=page)
            to_do_map[future] = page

        done_iter = futures.as_completed(to_do_map)

        for future in done_iter:
            pyjob_codes += future.result()

    return pyjob_codes


def async_get_pyjob_content(pyjob_codes: list, max_workers=10) -> list:
    """Get pyjob_codes, get content of pyjob and return a list of contents"""
    print('Running async_get_pyjob_content...')
    contets = []
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        to_do_map = {}
        for pyjob_code in pyjob_codes:
            future = executor.submit(get_pyjob_content, pyjob_code=pyjob_code)
            to_do_map[future] = pyjob_code

        done_iter = futures.as_completed(to_do_map)

        for future in done_iter:
            pyjob_code, content = future.result()
            contets.append((pyjob_code, content))

    return contets
