import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.coffeenbeer

###################################################################################################

# Goldmund Coffee List

url = "https://coffeelibre.kr/shop/list.php?ca_id=1020"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(url, headers = headers)
soup = BeautifulSoup(data.text, 'html.parser')

for link in soup.find_all('a'):
    if '/shop/item.php' in str(link.get('href')):
        url = link.get('href')
        data = requests.get(url, headers = headers)
        soup = BeautifulSoup(data.text, 'html.parser')
        for i in soup.select_one("#sit > form > div > div > div.h_list > p.copy2"):
            roasting_flavor = str(i).split('<br/>')
            if '전' in str(roasting_flavor[0]):
                roasting = str(roasting_flavor[0])
            elif str(roasting_flavor[0]) != '':
                flavor = str(roasting_flavor[0].lstrip())
                flavor = flavor.split(', ')
        for i in soup.find_all('p'):
            if '품종 /' in i.text:
                type = i.text
                type = str(type.split('품종 /')[1].lstrip())
        for i in soup.find_all('h3'):
            if i.text != '선택된 옵션':
                name = i.text
                country = str(i).split('<br/>')[0]
                country = country.split('>')[1].rstrip()
        db.coffee_info.insert_one({'brand': '커피 리브레',
                                   'lineup': 'Goldmund',
                                   'name': name,
                                   'country': country,
                                   'roasting': roasting,
                                   'flavor': flavor,
                                   'type': type})

# ################################################################################

# # Coffee Libre Single Origin

url = "https://coffeelibre.kr/shop/list.php?ca_id=1030"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(url, headers = headers)
soup = BeautifulSoup(data.text, 'html.parser')

for link in soup.find_all('a'):
    if '/shop/item.php' in str(link.get('href')):
        url = link.get('href')
        data = requests.get(url, headers = headers)
        soup = BeautifulSoup(data.text, 'html.parser')
        for i in soup.select_one("#sit > form > div > div > div.h_list > p.copy2"):
            roasting_flavor = str(i).split('<br/>')
            if '전' in str(roasting_flavor[0]):
                roasting = str(roasting_flavor[0])
            elif str(roasting_flavor[0]) != '':
                flavor = str(roasting_flavor[0].lstrip())
                flavor = flavor.split(', ')
        for i in soup.find_all('p'):
            if '품종 /' in i.text:
                type = i.text
                type = str(type.split('품종 /')[1].lstrip())
        for i in soup.find_all('h3'):
            if i.text != '선택된 옵션':
                name = i.text
                country = str(i).split('<br/>')[0]
                country = country.split('>')[1].rstrip()
        db.coffee_info.insert_one({'brand': '커피 리브레',
                                   'lineup': 'Goldmund',
                                   'name': name,
                                   'country': country,
                                   'roasting': roasting,
                                   'flavor': flavor,
                                   'type': type})
################################################################################