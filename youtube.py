from __future__ import unicode_literals
import youtube_dl
import os
import argparse


class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')

def pegarNomeArquivo(parser):
    parser.add_argument(
        "yt",
        default=
        '*************************************************\nCABEÇÃO...vc esqueceu de passar o arquivo de vídeo!!!!!\n*************************************************',
        help='Pegar o nome do Youtube.')
    arguments = parser.parse_args()
    url = "'" + arguments.yt + "'"
    return url


def baixar(ydl_opts, url):
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


def info_video(ydl_opts,url):
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        meta = ydl.extract_info(url, download=False)
        # meta = ydl.extract_info('https://www.youtube.com/watch?v=XWWPe4oXKtU', download=False)

    '''
    print('upload date : %s' % (meta['upload_date']))
    print('uploader    : %s' % (meta['uploader']))
    print('views       : %d' % (meta['view_count']))
    print('likes       : %d' % (meta['like_count']))
    print('dislikes    : %d' % (meta['dislike_count']))
    print('id          : %s' % (meta['id']))
    print('duration    : %s' %(meta['duration']))
    print('title       : %s' % (meta['title']))
    print('description : %s' % (meta['description']))
    print('format      : %s' % (meta['format']))
    '''
    return meta['title']

ydl_opts = {
    'outtmpl': '%(title)s-%(id)s.%(ext)s',  #how can i find
}
parser = argparse.ArgumentParser(description='Um programa de exemplo.')
first = pegarNomeArquivo(parser)
urlnv = first.split('&')
url = urlnv[0] + "'"
nome = ''
# print(url)
# url = "https://www.youtube.com/watch?v=BaW_jenozKcj"
# url = "https://www.youtube.com/watch?v=PeiOtp-Ldlw"
# url = "https://www.youtube.com/watch?v=R9hEzVc5HS4"
# url = 'https://www.youtube.com/watch?v=l36oFZnQO34' nery
# https://www.youtube.com/watch?v=WfzY35jGQLM&feature=em-uploademail chamada do molizane
url = 'https://www.youtube.com/watch?v=rEOlhIxoJSs'
# baixar(ydl_opts, url)
nome = '"'+info_video(ydl_opts,url)+'"'
print(nome)
# os.rename()
# shutil.move("path/to/current/file.foo", "path/to/new/destination/for/file.foo")
# shutil.move("", "")
# youtube-dl -o - "https://www.youtube.com/watch?v=BaW_jenozKcj" | vlc -