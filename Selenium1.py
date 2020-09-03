from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import bs4 as bs
import urllib.request

driver = webdriver.Chrome(executable_path=r"C:\Users\brind\PycharmProjects\chromedriver.exe")
driver.get("https://pythonprogramming.net/parsememcparseface/")
print(driver.title) #title of page
#close browser

source = urllib.request.urlopen('https://netflix.com').read()
soup = bs.BeautifulSoup(source, 'lxml')

print(soup.title)



print('entered the file')
