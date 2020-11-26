import requests
import json

for page in range(1,61,20):
    url = f'https://ecapi.pchome.com.tw/cdn/ecshop/prodapi/v2/region/DJAD/salesrank/0/prod&offset={page}&limit=20&fields=Id,Nick,Pic,Price,Discount,isSpec,Name,isCarrier,isSnapUp,isBigCart&_callback=jsonp_prodlist&1606409364796?_callback=jsonp_prodlist'
    res = requests.get(url)
    jsonStr = res.text.replace('try{jsonp_prodlist(','').replace(');}catch(e){if(window.console){console.log(e);}}','')
    jsonData = json.loads(jsonStr)
    for item in jsonData:
        print(item['Nick'],item['Price']['P'])
