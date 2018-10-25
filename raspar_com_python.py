''' External URL´s function'''

import urllib.request

def externalurls(url):
    '''List external urls on a given url'''
    t=urllib.request.urlopen(url).read().decode()
    t=t.replace("'",'"')
    t=t.split('href="')[1:]
    addr=url.replace('//','_BARRABARRA_').split('/')[0]
    addr=addr.replace('_BARRABARRA_','//')
    t=[i.split('"')[0] for i in t if i.startswith('http:') and not i.startswith(addr)]
    return t

if __name__ == '__main__':
    import sys
    print ('\n'.join(externalurls(sys.argv[1])))