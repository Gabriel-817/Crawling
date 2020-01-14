from bs4 import BeautifulSoup
import requests


url = "https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=cur&date=20170714"
str = requests.get(url)
print(str.text)

soup = BeautifulSoup(str.text, 'html.parser')

all_div_tit5 = soup.find_all('div',{"class":"tit5"})
for tmp in all_div_tit5:
    print(tmp.find("a").text)