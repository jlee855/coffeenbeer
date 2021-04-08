import requests
from bs4 import BeautifulSoup


# Home Page Crawling
url = "http://fritz.co.kr/product/list.html?cate_no=24"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(url, headers = headers)
soup = BeautifulSoup(data.text, 'html.parser')


for i in soup.find_all('a'):
    if "/product/detail.html?product_no=" in str(i) and "상품명" in str(i):
        data = str(i)
        data = data.split("href=")[1]
        data = data.split('>')[0]
        url = 'http://fritz.co.kr' + str(data[1:len(data) - 1])
        data = requests.get(url, headers = headers)
        soup = BeautifulSoup(data.text, 'html.parser')
        for i in soup.select("#prdDscp > p"):
            if '국가' in i.text:
                countries = str(i.text)
            elif '품종' in i.text:
                type = str(i.text)
            elif '가공방식' in i.text:
                process = str(i.text)
        for i in soup.select("#prdSide > div > div > div.info-wrap > div.costArea > div.name"):
            print(i.text.split('[프릳츠] ')[1])
        countries = countries.split('\xa0')
        type = type.split('\xa0')
        if u'\xa0' in process:
            process = process.replace(u'\xa0', u' ')
        process_list = process.split(' ')
        print(process_list)
        print(countries)
        print(type)
        print("##############")
#prdSide > div > div > div.info-wrap > div.costArea > div.name






