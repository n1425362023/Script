import json
import requests

url = 'https://fanyi.baidu.com/sug'
word = input('要搜索的单词:')
data = {
    'kw': word
}
header = {
    'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'
}
response = requests.post(url=url, data=data, headers=header)
dic = response.json()
print(dic)
filename = word + '.json'
fp = open(filename, 'w', encoding='utf-8')
json.dump(dic, fp=fp, ensure_ascii=False)
