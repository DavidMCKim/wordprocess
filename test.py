# import plotly.express as px
# import matplotlib.pyplot as plt
# from pytrends.request import TrendReq

# pytrends = TrendReq(hl='ko', tz=540)
# kw_list = '아이폰'
# pytrends.build_payload(kw_list, cat=0, timeframe='now 1-H', geo='KR', gprop='')

# data = pytrends.interest_over_time()
# df = data.reset_index()
# df.columns=[i for i in range(len(df.columns))]
# df = df[[0,2]]
# df.columns = ['date', kw_list]

# df.plot(kind='line',x='date', y=' 아이폰', color='red')

# figure = px.line(df, x = 'date', y=kw_list, title='google trend')
# figure.show()
# plt.savefig('googletrend.png')
# print()



# import requests

# url = 'http://apis.data.go.kr/1360000/RoadWthrInfoService/getCctvStnRoadWthr'
# params ={'serviceKey' : 'Dtfs8G7sjUuYfC8Wm2Uef8o1L6uAqHfTOVnaiXqH2gnfm0LI0%2B1Qv0vp6MBc2AJmB%2FQVYgEjI3dVRp384EmClQ%3D%3D', 'pageNo' : '1', 'numOfRows' : '10', 'dataType' : 'XML', 'eqmtId' : '0500C00001', 'hhCode' : '00' }

# response = requests.get(url, params=params)
# print(response.content)

import json
import requests
from bs4 import BeautifulSoup

# url = 'https://www.weather.go.kr/w/rest/zone/dong.do?type=WIDE&wideCode=&cityCode=&keyword=&keywordStart=&keywordEnd='
url = 'https://www.weather.go.kr/w/weather/forecast/mid-term.do'
headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Referer':'https://www.weather.go.kr/w/index.do',
    'Host':'www.weather.go.kr'
}
res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text,'html.parser')

print()