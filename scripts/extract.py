#!/usr/bin/env python3

# Interviewing Leather e-book creation script
#
# * https://banter-latte.com/portfolio/interviewing-leather/
# * https://nullprogram.com/blog/2017/05/15/

import requests
from bs4 import BeautifulSoup,SoupStrainer
from slugify import slugify
import pandas as pd
import html2markdown
import re

response = requests.get('https://www.fitzmuseum.cam.ac.uk/gallery/lagrandeguerre/')
print('Visited URL: {}'.format(response.url))
print(response.status_code)
baseurl = 'https://www.fitzmuseum.cam.ac.uk/gallery/lagrandeguerre/'

soup = BeautifulSoup(response.text, 'html.parser')
type(soup)
data = souP.find("div", {"id": "content"})
links = []
for b in data.findAll('a'):
    link = b.get('href')
    print(link)
    if link != None:
        links.append(baseurl + b.get('href'))
print(links)
for page in links:
    yoshi = requests.get(page)
    print(yoshi.status_code)
    toshi = BeautifulSoup(yoshi.text, 'html.parser')
    type(toshi)
    if yoshi.status_code != 404:
        h1 = toshi.find('div', id='content')
        if h1 is not None:
            body = toshi.find('div', id='content') or [0]
            # print(type(body))
            body = str(body.prettify())
            layout = 'default'
            mark = open('/Users/danielpett/Documents/GitHub/la-grande-guerre/_explore/' + slugify(page) + '.md', "w")
            meta = '---\n'
            meta +=  'layout: ' + layout + '\n'
            meta += '---\n'
            meta += body
            mark.write(meta)
            mark.close
