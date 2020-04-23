# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from bs4 import BeautifulSoup
import urllib.request
import re
import requests
from pathlib import Path

resp = urllib.request.urlopen("https://www.england.nhs.uk/statistics/statistical-work-areas/covid-19-daily-deaths/")
soup = BeautifulSoup(resp, from_encoding=resp.info().get_param('charset'))

for link in soup.find_all('a', attrs={'href': re.compile("^https:\/\/.*\.xlsx$")}):
    linkurl = link.get('href')
    filename = re.compile(".*/(.*)").search(linkurl).group(1)
    pathname = './Data/{0}'.format(filename)
    
    if not Path(pathname).is_file():
        print('Downloading file : {0}'.format(filename))
        r = requests.get(linkurl, allow_redirects=True)
        open(pathname, 'wb').write(r.content)
    