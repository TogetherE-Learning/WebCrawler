import requests
from bs4 import BeautifulSoup

url = 'https://www.ptt.cc/bbs/Food/index.html'
domain = 'https://www.ptt.cc'

for times in range(2):
    res = requests.get(url)
    #解析模式(html.parser)
    soup = BeautifulSoup(res.text,'html.parser')
    #爬取 class = 'title'下的 超連結
    articles = soup.select('.title a')

    for each_title in articles:
            href = each_title['href']
            print(each_title.text,f'{domain}{href}')

    #獲取上一頁連結
    paging = soup.select('.btn.wide')
    if len(paging) > 0:
        href = paging[1]['href']
        lastUrl = f'{domain}{href}'
        url = lastUrl
    else:
        break
