# pip install bs4
# pip install requests
# pip install lxml
import requests
from bs4 import BeautifulSoup

url = "https://www.naver.com"
r = requests.get(url)

soup = BeautifulSoup(r.content, "lxml")
네이버등록된_뉴스언론사들 = soup.find_all("a", {"class": "thumb"})

횟수 = 0

for 언론사 in 네이버등록된_뉴스언론사들:
    횟수 += 1
    print(str(횟수) + ": " + 언론사.img.get("alt"))
# print(title.img.get("alt"))
