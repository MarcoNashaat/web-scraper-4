#enabling https
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

#importing libraries
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re


def get_links(url):
    html = urlopen('http://en.wikipedia.org{}'.format(url))
    bs = BeautifulSoup(html,'html.parser')
    for link in bs.find('div',{'id':'bodyContent'}).find_all('a',href=re.compile('^(/wiki/)((?!:).)*$')):
        if 'href' in link.attrs:
            print(link['href'])






