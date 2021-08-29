##############################
## Lotto 6개 번호 합 예측
##############################

from pandas import DataFrame
from pandas import concat
from pandas import read_csv
from xgboost import XGBRegressor
from sklearn.model_selection import KFold, GridSearchCV
from xgboost import XGBClassifier
import pandas as pd
import requests 
from tqdm import tqdm
import json
import os

def getLottoWinInfo(minDrwNo, maxDrwNo):
    drwtNo1 = []
    drwtNo2 = []
    drwtNo3 = []
    drwtNo4 = []
    drwtNo5 = []
    drwtNo6 = []
    bnusNo = []
    totSellamnt = []
    drwNoDate = []
    firstAccumamnt = []
    firstPrzwnerCo = []
    firstWinamnt = []

    for i in tqdm(range(minDrwNo, maxDrwNo+1, 1)):
        req_url = "http://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=" + str(i)
        req_lotto = requests.get(req_url)
        lottoNo = req_lotto.json()

        drwtNo1.append(lottoNo["drwtNo1"])
        drwtNo2.append(lottoNo["drwtNo2"])
        drwtNo3.append(lottoNo["drwtNo3"])
        drwtNo4.append(lottoNo["drwtNo4"])
        drwtNo5.append(lottoNo["drwtNo5"])
        drwtNo6.append(lottoNo["drwtNo6"])
        bnusNo.append(lottoNo["bnusNo"])
        totSellamnt.append(lottoNo["totSellamnt"])
        drwNoDate.append(lottoNo["drwNoDate"])
        firstAccumamnt.append(lottoNo["firstAccumamnt"])
        firstPrzwnerCo.append(lottoNo["firstPrzwnerCo"])
        firstWinamnt.append(lottoNo["firstWinamnt"])

        lotto_dict = {"추첨일":drwNoDate, 
                      "Num1":drwtNo1,"Num2":drwtNo2,"Num3":drwtNo3,"Num4":drwtNo4,"Num5":drwtNo5,"Num6":drwtNo6,"bnsNum":bnusNo,
                      "총판매금액":totSellamnt,
                      "총1등당첨금":firstAccumamnt,
                      "1등당첨인원":firstPrzwnerCo,
                      "1등수령액": firstWinamnt}
        
    df_lotto= pd.DataFrame(lotto_dict)
    return df_lotto
if not os.path.isfile("lotto_940.csv"):
    lotto_df = getLottoWinInfo(939,940)
    lotto_df.to_csv("lotto_940.csv",index=False)

data = pd.read_csv("lotto_940.csv")
data.head()
data_sum = data["Num1"]+data["Num2"]+data["Num3"]+data["Num4"]+data["Num5"]+data["Num6"]
# print(data_sum.values)

#####################################################################################
# 로또 숫자 합 예측
#####################################################################################

days_in=600
day_out=1


df = DataFrame(data_sum)
raw = []
for i in range(days_in, 0,-1):
    raw.append(df.shift(i))

for i in range(0, day_out):
    raw.append(df.shift(-i))

sum = concat(raw,axis=1)
sum.dropna(inplace=True)

train = sum.values
#print(train)

#split into input and output columns
trainX,trainY= train[:,:-1], train[:,-1]

# fit model
model = XGBRegressor(objective='reg:squarederror', nthread=4)
model.fit(trainX,trainY)

grid = {'max_depth':[5,6,8], 'learning_rate':[0.05,0.1,0.15], 'n_estimators': range(50,100,10)}
gs = GridSearchCV(model, grid, cv=5, return_train_score=True)
gs.fit(trainX,trainY)
para = gs.best_params_
model_best = XGBRegressor(max_depth = para['max_depth'],learning_rate = para['learning_rate'],n_estimators = para['n_estimators'], objectov = 'reg:squarederror')
model_best.fit(trainX,trainY)

# construct an input for a new preduction
data_in = data_sum[-(days_in):]

# make a one-step prediction
result = model_best.predict([data_in])

print('input: %s, Predicted: %.3f' %(data_in,result[0]))
