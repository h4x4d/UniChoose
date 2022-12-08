import json
import time

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from parcer.list_of_links import vuz_links
data = []
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
for i in vuz_links:
    vuz_dict = {}
    url = i
    driver.get(i)
    time.sleep(1)
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    vuz_name = soup.find('h2', {'itemprop': 'name'}).text
    vuz_dict['name'] = vuz_name
    vuz_dict['description'] = 'Нет описания'
    try:
        vuz_dict['description'] = soup.select('html > body > div > div.maincontent > div.m270 > div.content > div.p40.pm40 > span.font2')[0].text
    except Exception:
        pass
    vuz_dict['region'] = soup.find('table', {'itemtype': 'https://schema.org/CollegeOrUniversity'}).find('table', {'style': 'width:auto; margin: 0 auto; margin-top:10px; text-align:center;'}).find('b', {'class': 'font1'}).text
    vuz_dict['rating'] = ('0.0', 'Нет оценок')
    try:
        rating_td = soup.find('td', {'class': 'ocenka'})
        vuz_dict['rating'] = (rating_td.find('b', {'class': 'font5'}).text, rating_td.find('span', {'class': 'font1'}).text.split(' ')[0])
    except Exception:
        pass
    # баллы
    url = i[:-5] + 'proxodnoi'
    driver.get(url)
    time.sleep(1)
    # .find_element(By.TAG_NAME, 'center')
    try:
        show_more_button = driver.find_element(By.CSS_SELECTOR, 'div.mobpadd20.morediv').click()
        time.sleep(1)
    except Exception:
        pass
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    headnaps = soup.find('div', {'id': 'rezspec'}).find_all('div', {'class': 'headnap'})
    napr_result = []
    for j in headnaps:
        napravlenie_class = j.find('div', {'class': 'napravlenienaz'})
        napravlenie = napravlenie_class.find('b', {'style': 'text-transform:uppercase;'}).text
        level = napravlenie_class.find('span', {'style': 'color:#8D8D8D;', 'class': 'font2'}).text.split(' ')[0]
        podrazd = j.find_all('table', {'class': 'vuzlist p20'})
        podrazd_result = []
        for k in podrazd:
            info = k.find('div', {'class': 'table-cell-2'}).find_all('span', {'class': 'font2'})
            podrazdelenie = info[0].text.split(': ')[1]
            profil = info[1].text.split(': ')[1]
            prohodnoy = k.find('table', {'class': 'circ2 circ2unique'}).find('span', {'class': 'font11'}).find('b').text
            subjects = k.find('div', {'class': 'napravlenietd1'}).find_all('table', {'class': 'cirfloat'})
            subj_list = []
            for subj_name in subjects:
                subj_list.append(subj_name.find_all('tr')[2].find('b').text.strip())
            print(podrazdelenie, profil, prohodnoy, level, subj_list)
            podrazd_result.append({'name': podrazdelenie, 'profile': profil, 'pass_mark': (prohodnoy if not prohodnoy.lower() == 'new' and not prohodnoy.lower() == 'нет' else 'Нет'), 'subjects': subj_list})
        napr_result.append({'name': napravlenie, 'level': level, 'podrazdelenie': podrazd_result})
    vuz_dict['napravlenie'] = napr_result
    data.append(vuz_dict)
file = open('data.json', 'w', encoding='utf-8')
json.dump(data, file, ensure_ascii=False, indent='    ')


# [
#     {
#         name: alsdfja
#         napr: [
#             {
#                 name: химия
#                 podrazd: [
#                     name: podrazdelenie
#                     profil: profil
#                     ...
#                 ]
#             }
#         ]
#     }
# ]
# vuzes[0]['name'] = sfdasdda
# vuzes[0]['napr'][0]['name'] = chemistry
# vuzes[0]['napr'][0]['podrazd']['name'] = podrazdelenie
