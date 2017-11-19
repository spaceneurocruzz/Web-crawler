import urllib.request, csv
from bs4 import BeautifulSoup
from datetime import datetime

page_url = 'https://shop.lego.com/en-US/Millennium-Falcon-75192'
page = urllib.request.urlopen(page_url)
soup = BeautifulSoup(page, 'html.parser')
name_tag = soup.find('h1', attrs={'class': 'overview__name markup'})
name = name_tag.text.strip()
price_tag = soup.find('span', attrs={'class':'product-price__list-price'})
price = price_tag.text

with open('LEGO.csv', 'a', encoding = 'utf-8-sig') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow([name, price, datetime.now()])