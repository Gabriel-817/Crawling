from bs4 import BeautifulSoup
import requests


url = "https://book.naver.com/bestsell/bestseller_list.nhn"
str = requests.get(url)
print(str.text)

soup = BeautifulSoup(str.text, 'html.parser')

all_dt_book_title = soup.find_all('dt', id="book_title_0")
for tmp in all_dt_book_title:
    print(tmp.find("a").text)