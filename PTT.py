import requests
import numpy as np
from bs4 import BeautifulSoup

keyword ='swift'
isShowNowUrl = False
#版名
name = 'Car'
domain = 'https://www.ptt.cc'
apiurl = f'/bbs/{name}/index.html'
over18Url = f'{domain}/ask/over18?from=%2Fbbs%2F{name}%2Findex.html'
url = f'{domain}{apiurl}'

#回傳 List 中 包含 text 的第一筆
def FirstByText(arr,text):
    for item in arr:
        if text in str(item):
            return item
   
#18禁 Button
def over18Chick(r):
    r.post(over18Url, payload)#取得頁面資訊   

def GetLastUrl(soup):
    u = soup.select(".btn.wide") #相關 a標籤
    tag = FirstByText(u,'上頁') #取得包含相關字串的 Tag
    
    lastUrl = tag.get("href")
    
    if lastUrl is None: #找不到按鈕跳出不執行
        return None
    
    return f'{domain}{lastUrl}'

r = requests.Session()
payload ={
    "from":apiurl,
    "yes":"yes"
}

for i in range(100): #往上爬3頁
    if isShowNowUrl:
        print(f"本頁的URL為 {url}")
    over18Chick(r)
    
    response = r.get(url)
    
    soup = BeautifulSoup(response.text,"html.parser")
    
    sel = soup.select("div.title a") #標題
    
    if keyword != '':
        sel = filter(lambda x: True if keyword.lower() in str(x).lower() else False ,sel)
        
    for s in sel: #印出網址跟標題
        print(f'{domain}{s["href"]}',s.text)
    
    if isShowNowUrl:
        print('')
    
    url = GetLastUrl(soup)#上一頁的網址
    
    if url is None: #沒有上一頁網址跳出迴圈
        print('-----------找不到上一頁的路徑或已經到第一頁-----------')
        break