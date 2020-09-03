from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import bs4 as bs
import urllib.request


source = urllib.request.urlopen('https://netflix.com').read()
soup = bs.BeautifulSoup(source, 'lxml')

print(soup.title)



print('entered the file')
