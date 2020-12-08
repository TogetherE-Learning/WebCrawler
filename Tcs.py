from selenium import webdriver as wd
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import datetime
import calendar
from datetime import timedelta
import csv

def add_months(sourcedate, months):
    month = sourcedate.month - 1 + months
    year = sourcedate.year + month // 12
    month = month % 12 + 1
    day = min(sourcedate.day, calendar.monthrange(year,month)[1])
    return datetime.date(year, month, day)

def getnowdate(sourcedate):
    month = sourcedate.month
    year = sourcedate.year
    day = sourcedate.day
    return datetime.date(year, month, day)

today = getnowdate(datetime.datetime.now())
startTime = '20201101'
endTime = '20201201'
dateFormatter = "%Y%m%d"

if(today.day < 16):
    today = add_months(today,-1)
    startTime = datetime.datetime.strftime(time,dateFormatter)
    time = add_months(today,1) - timedelta(today.day)
    endTime = datetime.datetime.strftime(time,dateFormatter)
else:
    time = today - timedelta(today.day-1)
    startTime = datetime.datetime.strftime(time,dateFormatter)
    time = add_months(today,1) - timedelta(today.day)
    endTime = datetime.datetime.strftime(time,dateFormatter)

driver = wd.Chrome()
driver.get('http://chap02/tcs/Forms/TCSReport.aspx?FORM_ID=100226&PRIV_ID=103&FORM_NME=%e5%b7%a5%e4%bd%9c%e6%97%a5%e8%aa%8c%e8%bc%b8%e5%85%a5')
driver.find_element_by_name("txtStartDate").send_keys(startTime)
driver.find_element_by_name("txtEndDate").send_keys(endTime)

driver.find_element_by_name("btnQuery").click()

soup = BeautifulSoup(driver.page_source, 'html.parser')

articles = soup.select('.tr_detail_1 td')

array = []
dic = {}

def foo(var):
    return {
    0: "專案名稱",
    1: "模組",
    2: "工作類別",
    3: "需求單號",
    4: "實際工時",
    5: "工作說明",
    6: "完成%"
    }.get(var,'error')

for i in range(0,len(articles)):
    td = articles[i]
    
    value = str(td).replace('<td>','').replace('</td>','').replace('<td align="right">','')
    
    key = foo(i%7)
    
    dic[key] = value
    
    if(i%7 == 5):
        array.append(dic)
        dic = {}

resultDic = {}

for item in array:
    projectName = item['專案名稱']
    singleNumber = item['需求單號']
    workingHours = float(item['實際工時'])
    if(projectName =='需求單'):
        if(singleNumber not in resultDic.keys()):
            resultDic[singleNumber] = float(0)
        resultDic[singleNumber] += workingHours
    else:
        if(projectName not in resultDic.keys()):
            resultDic[projectName] = float(0)
        resultDic[projectName] = resultDic[projectName] + workingHours
# 開啟輸出的 CSV 檔案
with open('output.csv', 'w', newline='') as csvfile: 
    # 建立 CSV 檔寫入器
    writer = csv.writer(csvfile)
    for item in resultDic:
        print(f'{item} {resultDic[item]}')
        # 寫入一列資料
        writer.writerow([f"'{item}", f"{resultDic[item]}"])

        
