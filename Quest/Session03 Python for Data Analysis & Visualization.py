# Quest 제출 시 제목을 'Session03 이름'으로 해주세요. ex. Session03 김현세


# 1
# numpy, pandas를 활용하여, ‘sex ratio.csv’로부터 아래와 같은 형태를 가진 ‘new sex ratio.csv’를 반환하는 코드를 구현해주세요.

import numpy as np
import pandas as pd

df = pd.read_csv('c:\\project\\sex ratio.csv')
df.columns
df=df.rename(columns={'Unnamed: 0':'지역'})

pr,yr,sr=[],[],[]
for i in range(16):
    for k in range(0,12):
        pr.append(df.iloc[i,0])
        yr.append(k+2006)
        sr.append(df.iloc[i,k+1])
        df_new={'지역':pr,'연도':yr,'성비':sr}
        
new=pd.DataFrame(data=df_new)
new.to_csv('c:\\project\\new sex ratio.csv',sep=',',encoding='Utf-8')

# 2
# ‘province data.csv’로부터 지역별로 전 기간에 걸친 평균 gdp와 unemploymen를 구한 뒤, 이를 산포도로 표현하세요.
# 단, 평균 성비가 110 이상인 지역의 산포도는 파란색 X 모양의 점, 110 미만인 지역의 산포도는 빨간색 세모 모양의 점으로 표현하세요.

import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('c:\\project\\province data.csv')
df.head()

df['gdp_mean'] = df.groupby(['id'])['gdp'].mean()
df['unemployment_mean'] = df.groupby(['id'])['unemployment'].mean()

df['high'] = df.groupby(['id'])['sexratio'].mean() >= 110
high_sr = df.query('high == True')
low_sr = df.query('high == False')

plt.scatter(high_sr['gdp_mean'], high_sr['unemployment_mean'], color='blue', marker='x')
plt.scatter(low_sr['gdp_mean'], low_sr['unemployment_mean'], color='red', marker='^')
plt.xlabel('GDP')
plt.ylabel('UNEMPLOYMENT')
