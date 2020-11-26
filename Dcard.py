import requests,json
import matplotlib.pyplot as plt

api = 'https://www.dcard.tw/service/api/v2/forums/money/posts?popular=true'

res = requests.get(api)
jArray = json.loads(res.text)

genderCount = {'F':0,'M':0,'D':0}

for item in jArray:
    gender = item['gender']
    genderCount[gender] = genderCount[gender] + 1

sex = ['女性','男性']

total = [genderCount['F'],genderCount['M']]

#由於 plt 會出現亂碼，故透過 font.sans-serif 設定能夠支援的中文字形
# 若 DFKai-SB 還是亂碼 可改成 SimHei 嘗試
plt.rcParams['font.sans-serif'] = ['DFKai-SB']
plt.bar(sex,total)
