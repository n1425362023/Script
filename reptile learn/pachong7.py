import requests

url = 'https://www.huohutv.net/'
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0'
}
reponse = requests.post(url=url, headers=header)
text = reponse.text
filename = 'huohuotv.html'
with open(filename, 'w', encoding='utf-8') as fp:
    fp.write(text)
