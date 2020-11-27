from selenium import webdriver as wd
import json
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup

startTime = '20201101'
endTime = '20201201'
#usr = '11415 劉昱揚'
usr = '13352 廖裕豪'
driver = wd.Chrome()
driver.get('http://chap02/tcs/Forms/TCSReport.aspx?FORM_ID=100226&PRIV_ID=103&FORM_NME=%e5%b7%a5%e4%bd%9c%e6%97%a5%e8%aa%8c%e8%bc%b8%e5%85%a5')
driver.find_element_by_name("txtStartDate").send_keys(startTime)
driver.find_element_by_name("txtEndDate").send_keys(endTime)

select = Select(driver.find_element_by_name('txtUSR_ID'))

for index in range(len(select.options)):
    if(select.options[index].text == usr):
        select.select_by_index(index)

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
        
for item in resultDic:
    print(f'{item} {resultDic[item]}')
