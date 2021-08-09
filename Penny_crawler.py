import csv, requests
from bs4 import BeautifulSoup
from datetime import datetime

def crawler():
    headers = {
        'content-type': 'text/html; charset=UTF-8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
    page_url = 'https://asia.pennyskateboards.com/products/cactus-wanderlust-high-line-surfskate'
    page = requests.get(url=page_url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    name_tag = soup.find('span', attrs={'class': 'product__price'})
    name = name_tag.text.strip()
    return name

def lineNotifyMessage(token, msg):
    headers = {
        "Authorization": "Bearer " + token, 
        "Content-Type" : "application/x-www-form-urlencoded"
    }

    payload = {'message': msg }
    r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = payload)
    print(r)
    return r.status_code


if __name__ == "__main__":
  token = ''
  message = crawler()
  lineNotifyMessage(token, message)

  