import requests
from bs4 import BeautifulSoup
import io
import pytesseract
from PIL import Image
from io import BytesIO

url = f'https://icinfo.immigration.gov.tw/NIL_WEB/NFCData.aspx'
r = requests.Session()
res = r.get(url)
soup = BeautifulSoup(res.text,'html.parser')

#TODO 取得驗證碼
validateCodeUrl = 'https://icinfo.immigration.gov.tw/NIL_WEB/ValidateCode.ashx'
response = r.get(validateCodeUrl)
image_bytes = io.BytesIO(response.content)
img = Image.open(image_bytes)
#img.show()
code = pytesseract.image_to_string(img)
print(code)


#print(img)
#取得隱藏的參數
VIEWSTATE = soup.find('input', {'name': '__VIEWSTATE'}).get('value')
VIEWSTATEGENERATOR = soup.find('input', {'name': '__VIEWSTATEGENERATOR'}).get('value')
EVENTVALIDATION = soup.find('input', {'name': '__EVENTVALIDATION'}).get('value')
formData = {
    "IDNO": "H123491963",
    "APPROVE_DATE": '20200101',
    "END_STAY_PERIOD": '1988/03/20',
    "BARCODE_NO": 'F160000001',
    "TextBox1": '36',
    "ReNext": "查詢",
    "__VIEWSTATE":VIEWSTATE,
    "__VIEWSTATEGENERATOR":VIEWSTATEGENERATOR,
    "__EVENTVALIDATION":EVENTVALIDATION,
}
res = r.post(url,data = formData)
soup = BeautifulSoup(res.text,'html.parser')
#print(soup)
result = soup.select('span',{'id':'lblResult'})
result
