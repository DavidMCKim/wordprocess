import requests
import pandas as pd
from bs4 import BeautifulSoup as bs
from datetime import datetime, timedelta

class KMA(): #KMC(Korea Meteorological Administration):기상청
    def __init__(self) -> None:
        self.url = 'https://www.weather.go.kr/w/weather/forecast/mid-term.do'
        self.headers = {
            'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Referer':'https://www.weather.go.kr/w/index.do',
            'Host':'www.weather.go.kr'
        }
        self.res = requests.get(self.url, headers=self.headers)
        self.soup = bs(self.res.text,'html.parser')

    def Parsing_Weather(self):
        try:
            weather = pd.read_html(self.res.text ,header = 0,encoding='euc-kr')[0]
            
        except Exception as e:
            print(e)
            
        return 

    def Parsing_Temparature(self, word):
        try:
           temparature = pd.read_html(self.res.text ,header = 0,encoding='euc-kr')[1]
        except Exception as e:
            print(e)

        return 
            
