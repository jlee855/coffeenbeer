import requests
from bs4 import BeautifulSoup

url = "https://coffeelibre.kr/shop/listtotal.php?ca_id=10"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(url, headers = headers)
soup = BeautifulSoup(data.text, 'html.parser')

################################################################################

# Coffee Libre Single Origin
## Coffee List
"""#contents > section:nth-child(3) > ul > li:nth-child(1) > div > a > div.title > div > p:nth-child(1)"""

## Taste
"""#contents > section:nth-child(3) > ul > li.sct_li.sct_clear > div > a > div.copy > div > div.txt2"""


single_origin_coffee_list = soup.select("#contents > section:nth-child(3) > ul > li")

for i in single_origin_coffee_list:
    names = i.select_one("div > a > div.title > div > p:nth-child(1)")
    country = str(names).split('<p>')[1].split('<br/>')[0]
    coffee_name = str(names).split('<p>')[1].split('<br/>')[1].split('</p>')[0].strip()
    print(country)
    print(coffee_name)
    taste_info = i.select_one("div > a > div.copy > div > div.txt2").text
    roasting = taste_info.split('전')[0] + '전'
    tastes = taste_info.split('전')[1].lstrip()
    tastes = tastes.split(', ')
    print(roasting)
    print(tastes)


################################################################################
# Coffee Libre Goldmund

## Coffee List
"""#contents > section:nth-child(2) > ul > li.sct_li.sct_clear > div > a > div.title > div > p:nth-child(1)"""

## Taste
"""#contents > section:nth-child(2) > ul > li.sct_li.sct_clear > div > a > div.copy > div > div.txt2"""
#contents > section:nth-child(2) > ul > li:nth-child(2) > div > a > div.copy > div > div.txt2


goldmund_coffee_list = soup.select("#contents > section:nth-child(2) > ul > li")


for i in goldmund_coffee_list:
    names = i.select_one("div > a > div.title > div > p:nth-child(1)")
    country = str(names).split('<p>')[1].split('<br/>')[0]
    coffee_name = str(names).split('<p>')[1].split('<br/>')[1].split('</p>')[0].strip()
    tastes = i.select_one("div > a > div.copy > div > div.txt2").text
    roasting = taste_info.split('전')[0] + '전'
    tastes = taste_info.split('전')[1].lstrip()
    tastes = tastes.split(', ')
    print(country)
    print(coffee_name)
    print(tastes)
