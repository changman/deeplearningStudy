#%%
import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt
from datetime import datetime


start=datetime(2003,1,1)
end=datetime(2017,6,30)

KIA=web.DataReader('000270.KS','yahoo',start,end)
KIA['Close'].plot(figsize=(12,6),grid=True);

#%%
import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt
from datetime import datetime
from fbprophet import Prophet

start=datetime(2003,1,1)
end=datetime(2017,6,30)

KIA=web.DataReader('000270.KS','yahoo',start,end)

KIA_trunc=KIA[:'2016-12-31']
df=pd.DataFrame({'ds':KIA_trunc.index, 'y':KIA_trunc['Close']})
df.reset_index(inplace=True)
del df['Date']

m=Prophet(daily_seasonality=True)
m.fit(df);

future=m.make_future_dataframe(periods=365)        # 예측하기
future.tail()
forecast=m.predict(future)

m.plot(forecast);           
# %%
