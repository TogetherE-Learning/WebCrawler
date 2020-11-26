import requests
import json

api = 'https://www.thsrc.com.tw/TimeTable/Search'
formData = {
    "SearchType": "S",
    "Lang": "TW",
    "StartStation": "NanGang",
    "EndStation": "ZuoYing",
    "OutWardSearchDate": "2020/11/27",
    "OutWardSearchTime": "07:30",
    "ReturnSearchDate": "2020/11/27",
    "ReturnSearchTime": "07:30"

}
res = requests.post(api,data =formData)
result = json.loads(res.text)
clean = result['data']['DepartureTable']['TrainItem']
print('車次','出發','抵達','耗時','自由座')
for item in clean:
    print(item['TrainNumber'],item['DepartureTime'],item['DestinationTime'],item['Duration'],item['NonReservedCar'])
