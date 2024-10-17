import requests

if __name__ == '__main__':
    header = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'
    }
    k = input('输入搜索内容：')
    param = {
        'query': k
    }
    url = 'https://baidu.com/s?wd='+k
    response=requests.get(url=url,headers=header)
    print(response.status_code)
    r = response.text
    filename = "huohu" + '.html'
    with open(filename, 'w', encoding='utf-8') as fp:
        fp.write(r)
