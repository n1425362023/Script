import requests

url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'

headers = {

    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15'

}

data = {
    'MIME类型': 'application/x-www-form-urlencoded; charset=UTF-8',
    'cname': '',
    'pid': '',
    'keyword': '秦皇岛',
    'pageIndex': '1',
    'pageSize': '3',
}

response = requests.post(url=url, headers=headers, data=data)
page_text = response.text
with open('KFC.txt', mode='a', encoding='utf-8') as f:
    f.write(page_text)
