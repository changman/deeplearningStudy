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

fig1=model.plot(forecast)
fig2=model.plot_components(forecast)

forecast_1 = forecast['yhat'].values[len(forecast)-1]
print('The Prophet Predicted Value :', forecast_1)
# %%
