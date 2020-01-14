from bs4 import BeautifulSoup
import requests


url = "https://music.naver.com/listen/top100.nhn?domain=DOMESTIC_V2"
str = requests.get(url)
print(str.text)

soup = BeautifulSoup(str.text, 'html.parser')

all_td__artist_artist = soup.find_all('td',{"class":"_artist artist"})
for tmp in all_td__artist_artist:
    print(tmp.find("a").text)