from pandas import DataFrame
from pandas import concat

days_in = 1
day_out = 1

df = DataFrame( x for x in range(10))
#print(df.values)
raw = []
#print(df.shift(1))
for i in range(days_in , 0, -1):
    raw.append(df.shift(i))


for i in range(0, day_out):
    raw.append(df.shift(-i))

sum = concat(raw, axis=1)
#print(sum)

sum.dropna(inplace=True)
print(sum.values)