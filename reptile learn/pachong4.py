import requests
from bs4 import BeautifulSoup
from multiprocessing.dummy import Pool
url = "https://www.shicimingju.com/book/sanguoyanyi.html"
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'
}
response = requests.get(url=url, headers=header)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
mulu = soup.select('.book-mulu > ul > li')
fp = open('./sanguoyanyi.txt', 'w', encoding='utf-8')
for i in mulu:
    title = i.a.text
    page_url = "https://www.shicimingju.com" + i.a['href']
    article = requests.get(url=page_url, headers=header)
    article.encoding = 'utf-8'
    page_soup = BeautifulSoup(article.text, 'lxml')
    content = page_soup.find('div', class_='chapter_content')
    fp.write(title + ':' + content.text.replace("\u00a0", " ")+'\n')
    print(title, "爬取成功")
