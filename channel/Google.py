import pandas as pd
from pytrends.request import TrendReq
from datetime import datetime, timedelta

class GoogleTrend():
    def __init__(self) -> None:
        self.word_df = pd.DataFrame()
        self.pytrends = TrendReq(hl='ko-KR', tz=540) # hl(Host Language) : 구글 트랜드의 언어 설정, tz(TimeZone offset) : UTCF부터의 시차를 분 단위로 표히 

    def Search_TrendWord(self):
        try:
            self.word_df = self.pytrends.trending_searches(pn='south_korea') # pn : 국가설정
        except Exception as e:
            print(e)
            
        return self.word_df

    def Search_WordVolume(self, word):
        try:
            kw_list = '아이폰'
            self.pytrends.build_payload(kw_list, cat=0, timeframe='now 7-d', geo='KR', gprop='')

            data = self.pytrends.interest_over_time()
            df = data.reset_index()
            df.columns=[i for i in range(len(df.columns))]
            df = df[[0,2]]
            df.columns = ['date', word]   
            # startdate = datetime.strftime(datetime.now()-timedelta(days=7), '%Y-%m-%d')
            # enddate   = datetime.strftime(datetime.now(), '%Y-%m-%d')
            # self.pytrends.build_payload(
            #                         word,
            #                         cat=0, 
            #                         timeframe=f'{startdate} {enddate}', 
            #                         geo='KR', gprop=''
            #                     )
            # data = self.pytrends.interest_over_time()
        except Exception as e:
            print(e)

        return {word:round(df[word].mean(),2)}
            
