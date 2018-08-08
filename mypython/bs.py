#encoding:utf-8

import urllib2
from bs4 import BeautifulSoup


url = 'http://reeoo.com'
request = urllib2.request(url)
response = urllib2.urlopen(request,timeout = 20)
content = response.read()
soup = BeautifulSoup(content , 'html.parser')

