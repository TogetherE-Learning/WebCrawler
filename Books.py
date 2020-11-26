import requests
from bs4 import BeautifulSoup
import shutil
import os 

def SaveFile(folderName,fName,stream):
    # wb => 寫入 byte
    pics = open(f'{folderName}/{fName}','wb')
    shutil.copyfileobj(stream.raw,pics)
    pics.close()
    
for page in range(1,3):
    folderName = f'page{str(page).zfill(3)}'
    if os.path.exists(folderName) == False:
        os.mkdir(folderName)
    url = f'https://www.books.com.tw/web/sys_bbotm/books/020806/?o=1&v=1&page={page}'
    res = requests.get(url)
    #解析模式(html.parser)
    soup = BeautifulSoup(res.text,'html.parser')
    #爬取 class = 'title'下的 超連結
    for item in soup.select('.cover'):
        #圖片路徑
        src = item['src']
        # 切割後取得最後一筆資料
        p = src.split('/')[-1]
        # 取得檔案名稱
        fName = p.split('&')[0]
        # 取得圖片網址
        imgUrl = src.split('i=')[1].split('&')[0]
        imgStream = requests.get(imgUrl,stream = True)
        # 將取得的圖片檔案寫入電腦資料夾
        SaveFile(folderName,fName,imgStream)
