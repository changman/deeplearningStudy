#%%
from fbprophet import Prophet
import pandas as pd

lotto_df = pd.read_csv("lotto_940.csv")
lotto_df.head()

data_sum = lotto_df["Num1"]+lotto_df["Num2"]+lotto_df["Num3"]+lotto_df["Num4"]+lotto_df["Num5"]+lotto_df["Num6"]
values = data_sum.values

new_values=[]
new_values = pd.DataFrame(new_values)
new_values['ds'] = lotto_df['추첨일']
new_values['y'] = values
data = new_values[['ds','y']]

model=Prophet()
model.fit(data)

future = model.make_future_dataframe(periods=168, freq='H')

forecast = model.predict(future)

# 그래프 그리기
fig1=model.plot(forecast)
fig2=model.plot_components(forecast)

forecast_1 = forecast['yhat'].values[len(forecast)-1]
print('The Prophet Predicted Value :', forecast_1)
# %%

from fbprophet import Prophet
#https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.head.html
import pandas as pd

def is_same(expect, value):
    return 1 if expect ==value else 0

lotto_df = pd.read_csv("lotto_940.csv")
lotto_df.head()

print (lotto_df["Num1"].values)

found_list = []
#https://stackoverflow.com/questions/16476924/how-to-iterate-over-rows-in-a-dataframe-in-pandas
for index, row in lotto_df.iterrows():  
    sum_value = is_same(45,row["Num1"]) + is_same(45,row["Num2"])  + is_same(45,row["Num3"])  + is_same(45,row["Num4"])  + is_same(45,row["Num5"])  + is_same(45,row["Num6"])
    #https://stackoverflow.com/questions/42479988/how-to-append-rows-in-a-python-list
    found_list.append(sum_value)

new_values=[]
new_values = pd.DataFrame(new_values)
new_values['ds'] = lotto_df['추첨일']
new_values['y'] = found_list
data = new_values[['ds','y']]
print (data)

model=Prophet()
model.fit(data)

future = model.make_future_dataframe(periods=168, freq='H')

forecast = model.predict(future)

fig1=model.plot(forecast)
fig2=model.plot_components(forecast)

forecast_1 = forecast['yhat'].values[len(forecast)-1]

forecast_1 = forecast['yhat'].values[len(forecast)-1]
print('The Prophet Predicted Value :', forecast_1)
# %%
