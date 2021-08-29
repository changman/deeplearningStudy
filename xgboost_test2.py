from pandas import DataFrame
from pandas import concat
from xgboost import XGBRegressor
from pandas_datareader import data as pdr

days_in=30
day_out=1

event = pdr.get_data_yahoo('055550.KS')
event_close = event["Close"]
values = event_close.values
#print(values)

df = DataFrame(values)
raw = []
for i in range(days_in, 0,-1):
    raw.append(df.shift(i))

for i in range(0, day_out):
    raw.append(df.shift(-i))

sum = concat(raw,axis=1)
sum.dropna(inplace=True)

train = sum.values
#print(train)

trainX,trainY= train[:,:-1], train[:,-1]

model = XGBRegressor(objective='reg:squarederror', n_estimators=80)
model.fit(trainX,trainY)

data_in = values[-(days_in):]
result = model.predict([data_in])

print('input: %s, Predicted: %.3f' %(data_in,result[0]))
