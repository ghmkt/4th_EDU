# Quest 제출 시 제목을 'Session03 이름'으로 해주세요. ex. Session03 김현세


# 1
# numpy, pandas를 활용하여, ‘sex ratio.csv’로부터 아래와 같은 형태를 가진 ‘new sex ratio.csv’를 반환하는 코드를 구현해주세요.

import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

a=pd.read_csv('c:\\GH\\sex ratio.csv')

a.columns=['dh','2006',
 '2007',
 '2008',
 '2009',
 '2010',
 '2011',
 '2012',
 '2013',
 '2014',
 '2015',
 '2016',
 '2017']

aa=a
bb=aa.drop('dh',axis=1)
for i in range(len(bb)):
    tp=pd.DataFrame(bb.iloc[i])
    tp['지역']=np.full((len(bb.iloc[i]),1),a.iloc[i,0])
    tp.columns=['성비','지역']
    tp['연도']=tp.index
    cp=cp.append(tp,ignore_index=True)
cp=cp[['지역','연도','성비']]
print(cp)
# 2
# ‘province data.csv’로부터 지역별로 전 기간에 걸친 평균 gdp와 unemploymen를 구한 뒤, 이를 산포도로 표현하세요.
# 단, 평균 성비가 110 이상인 지역의 산포도는 파란색 X 모양의 점, 110 미만인 지역의 산포도는 빨간색 세모 모양의 점으로 표현하세요.
df=pd.read_csv('c:\\GH\\province data.csv')
gdp_mean=df.groupby(['id'])['gdp'].mean()
unemployment_mean=df.groupby(['id'])['unemployment'].mean()
sexratio_mean=df.groupby(['id'])['sexratio'].mean()

idf=pd.DataFrame({'gdp':gdp_mean,'un':unemployment_mean,'sex':sexratio_mean})

a=idf[idf['sex']>=110]

b=idf[idf['sex']<110]

plt.scatter(a['gdp'],a['un'],color='b',marker='x')
plt.scatter(b['gdp'],b['un'],color='r',marker='^')
plt.xlabel('gdp')
plt.ylabel('unemployment')
plt.grid(True)
plt.show()
