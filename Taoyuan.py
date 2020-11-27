import requests
import json

api = 'https://www.taoyuan-airport.com/main_ch/airData.aspx'
formData = {
    "ft": "arrival",
    "s": '',
    "f": '',
    "c": '',
    "a": '',
    "dt": "06:00:00-07:59:59",
    "dd": "2020/11/27",
    "tm": 2,
    "uid": 154,
    "pid": 12
}
res = requests.post(api,data = formData)
data = json.loads(res.text)
data = json.loads(data)
clean = data['fd']
print('航空名稱','編號','  狀態')

for item in clean:
    aname = item['AName'].split('>')[3].split('<')[0]
    flightNo = item['FlightNo'].split('>')[1].split('<')[0]
    memo = item['memo'].split('>')[1].split('<')[0]
    print(aname,flightNo,memo)
