import urllib.request, csv
from bs4 import BeautifulSoup
from datetime import datetime

page_urls = ['https://shop.lego.com/en-US/Women-of-NASA-21312?icmp=SHM_NA_21312', 'https://shop.lego.com/en-US/Millennium-Falcon-75192']

data = []
for pg in page_urls:
    page = urllib.request.urlopen(pg)
    soup = BeautifulSoup(page, 'html.parser')
    name_tag = soup.find('h1', attrs={'class': 'overview__name markup'})
    name = name_tag.text.strip()
    price_tag = soup.find('span', attrs={'class':'product-price__list-price'})
    price = price_tag.text
    data.append((name, price))

with open('LEGOs.csv', 'a', encoding = 'utf-8-sig') as csv_file:
    writer = csv.writer(csv_file)
    for name, price in data:
        writer.writerow([name, price, datetime.now()])