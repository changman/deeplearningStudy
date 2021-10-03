# 참고 https://wendys.tistory.com/174?category=769564
#  판다스 문서 https://pydata.github.io/pandas-datareader/readers/index.html
#%%

#종목 코드 가져오기
import pandas as pd

df = pd.read_html('http://kind.krx.co.kr/corpgeneral/corpList.do?method=download', header=0)[0]

df = df[['회사명', '종목코드']]
df = df.sort_values(['종목코드'], ascending=[True])
df.head(10)
#df.to_csv("stock_code.csv",index=False)
# %%

# 주식 종가 가져오기
import pandas_datareader as pdr
import matplotlib.pyplot as plt
from datetime import datetime

start=datetime(2021,1,1)
end=datetime(2021,10,3)
# 코스피 :  .KS, 코스닥 .KQ
stock_code = '005930.KS'

# 1번 방법
# DataReader API를 통해서 yahoo finance의 주식 종목 데이터를 가져온다.
df = pdr.DataReader(stock_code, 'yahoo',start,end)

# 2번 방법
# get_data_yahoo API를 통해서 yahho finance의 주식 종목 데이터를 가져온다.
#df = pdr.get_data_yahoo(stock_code,start,end)

df['Close'].plot(figsize=(12,6),grid=True);
df.to_csv("samsung_close.csv",index=True)
# %%
