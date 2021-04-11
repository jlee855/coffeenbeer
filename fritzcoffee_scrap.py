import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient


# Home Page Crawling
url = "http://fritz.co.kr/product/list.html?cate_no=24"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(url, headers = headers)
soup = BeautifulSoup(data.text, 'html.parser')

client = MongoClient('localhost', 27017)
db = client.coffeenbeer



for i in soup.find_all('a'):
    if "/product/detail.html?product_no=" in str(i) and "상품명" in str(i):
        data = str(i)
        data = data.split("href=")[1]
        data = data.split('>')[0]
        url = 'http://fritz.co.kr' + str(data[1:len(data) - 1])
        data = requests.get(url, headers = headers)
        soup = BeautifulSoup(data.text, 'html.parser')
        ## Getting the coffee name
        for i in soup.select("#prdSide > div > div > div.info-wrap > div.costArea > div.name"):
            name = i.text.split('[프릳츠] ')[1]
        ## Getting country, type, and process
        for i in soup.select("#prdDscp > p"):
            if '국가' in i.text:
                country = str(i.text)
            elif '품종' in i.text:
                type = str(i.text)
            elif '가공방식' in i.text:
                process = str(i.text)
        ## Getting the flavors
        # prdSide > div > div > div.info-wrap > div.xans-element-.xans-product.xans-product-detail.boxArea > div.description2
        for i in soup.select("#prdSide > div > div > div.info-wrap > div.xans-element-.xans-product.xans-product-detail.boxArea > div.description2"):
            description = str(i).split('<br/>')[0]
            print(description.split('>'))
        # ## Tidying the Scraped Data
        # if u'\xa0' in process:
        #     process = process.replace(u'\xa0', u' ')
        # if u'\xa0' in country:
        #     country = country.replace(u'\xa0', u' ')
        # if u'\xa0' in type:
        #     type = type.replace(u'\xa0', u' ')
        # print(process)
        # print(country)
        # print(type)
        # db.coffee_info.insert_one({
        #     'brand': 'fritz_coffee',
        #     'lineup': 'Single Origin',
        #     'name': name.rstrip(),
        #     'country': country.split(': ')[1].rstrip(),
        #     'type': type.split(': ')[1].rstrip(),
        #     'process': process.split(': ')[1].rstrip()
        # })




