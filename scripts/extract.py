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

response = requests.get('https://www.fitzmuseum.cam.ac.uk/gallery/shahnameh/vgallery/section5.html')
print('Visited URL: {}'.format(response.url))
print(response.status_code)
baseurl = 'https://www.fitzmuseum.cam.ac.uk/gallery/shahnameh/vgallery/'

soup = BeautifulSoup(response.text, 'html.parser')
type(soup)

soup = BeautifulSoup(response.text, parseOnlyThese=SoupStrainer("td"))
x = soup.findAll("a")
links = []
for tr in x:
    links.append(baseurl + tr.get('href'))
print(links)
for page in links:
    yoshi = requests.get(page)
    print(yoshi.status_code)
    toshi = BeautifulSoup(yoshi.text, 'html.parser')
    type(toshi)
    if yoshi.status_code != 404:
        h1 = toshi.find('div', id='content').h3
        if h1 is not None:
            title = h1.getText()
            body = toshi.find('div', id='content') or [0]
            # print(type(body))
            body = body.getText()
            body = body.replace('      ', '')
            body = body.replace("     " , " ")
            body = body.replace("  " , " ")
            body = body.replace("\r","\n")
            body = body.replace("\n\n\n\n\n\n\n\n","\n")
            body = body.replace("\n\n\n\n\n\n\n","\n")
            body = body.replace("\n\n\n\n\n","\n")
            body = body.replace("\n\n\n\n","\n")
            body = body.replace("\n\n\n","\n")
            body = body.replace("\n\n","\n")
            body = body.replace("Click for larger view [new window]" , "")
            body = body.replace("Click on each panel for larger view [new window]" , "")
            body = body.replace("Click on each panel to see it enlarged [new window]" , "")
            layout = 'default'
            permalink = ' /explore/objects/' + slugify(title[:75])
            mark = open('/Users/danielpett/Documents/GitHub/shahnameh/_explore/' + slugify(title[:75]) + '.md', "w")
            meta = '---\n'
            meta +=  'layout: ' + layout + '\n'
            meta += 'title: "' + title.rstrip() + '"\n'
            meta += 'permalink: ' + permalink + '\n'
            meta += '---\n'
            meta += body
            mark.write(meta)
            mark.close
