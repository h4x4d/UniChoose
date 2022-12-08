import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
url = "https://tabiturient.ru/"
driver = webdriver.Chrome('./chromedriver')
driver.get(url)
time.sleep(3)
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
results = soup.find_all('table', {'class': 'dopvuzlist open'})
links = []
for i in results:
    links.append(i.find('td', {'colspan': '10', 'class': None}).find('a')['href'])
print(links)