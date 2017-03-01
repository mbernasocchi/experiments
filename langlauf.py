#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bottle import route, run, template

import re
import requests
from bs4 import BeautifulSoup as bs, ResultSet


@route('/')
def index():
    html = "<html><head><title>Langlauf bei Einsiedeln</title></head>\n<body>\n"

    sites = [
        {'name': 'Bolzberg/Trachslau',
         'url': 'http://www.loipe-bolzberg.ch/aktuell.html',
         'selector': "find(id='c100')"
         },
        {'name': 'Schwedentritt',
         'url': 'http://www.schwedentritt.ch/',
         'selector': "find(id='c778')"
         },
        {'name': 'Studen',
         'url': 'http://www.studen-sz.ch/',
         'selector': 'find_all(lambda t: t.name == "b" and "F5 drücken" in t.text)'
         },
        {'name': 'Rothenturm',
         'url': 'http://www.finnenloipe.ch/loipenzustand/',
         'selector': "find(id='content')"
         },
        {'name': 'Hoch-Ybrig',
         'url': 'http://www.infosnow.ch/~apgmontagne/?lang=de&id=75&tab=mob-wi2',
         'pattern': re.compile(r'Langlauf'),
         'selector': 'find("h1", text=site["pattern"]).parent'
         }
    ]

    for site in sites:
        request = requests.get(site['url'])
        soup = bs(request.text)
        selector = 'soup.%s' % site['selector']
        result = eval(selector)
        if result:
            html += '\n<h2>%s</h2>\n' % site['name']
            print(type(result))
            if isinstance(result, ResultSet):
                result = result[0]
            html += str(result.prettify())
            html += '<hr/>'

    html += "</body></html>"
    return html

run(host='localhost', port=8080)
