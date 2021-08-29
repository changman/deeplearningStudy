#ref https://rfriend.tistory.com/256
import pandas as pd
from pandas import DataFrame

df_1 = pd.DataFrame({'A': ['A0', 'A1', 'A2',],
                     'B': ['B0', 'B1', 'B2'],
                     'C': ['C0', 'C1', 'C2'],
                     'D': ['D0', 'D1', 'D2']},index=[0, 1, 2])

df_2 = pd.DataFrame({'A': ['A3', 'A4', 'A5'],
                     'B': ['B3', 'B4', 'B5'],
                     'C': ['C3', 'C4', 'C5'],
                     'D': ['D3', 'D4', 'D5']},index=[0, 1, 2])

#print('##### df_1 ####')
#print (df_1)
#
#print('\n##### df_2 ####')
#print (df_2)
#
#df_12_axis0 = pd.concat([df_1, df_2])
#print('\n##### df_12_axis0 ####')
#print (df_12_axis0)

df_3 = pd.DataFrame({'E': ['A6', 'A7', 'A8'],
                     'F': ['B6', 'B7', 'B8'],
                     'G': ['C6', 'C7', 'C8'],
                     'H': ['D6', 'D7', 'D8']},index=[3, 4, 5])

print('##### df_3 ####')
print(df_3)

df_13_axis1 = pd.concat([df_1, df_3], axis=1) # column bind
print('##### df_13_axis1 ####')
print (df_13_axis1)