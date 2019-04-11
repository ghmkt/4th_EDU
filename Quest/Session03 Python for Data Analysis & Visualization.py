# 답안

import pandas as pd; import numpy as np

df = pd.read_csv('C:\\Users\\myeon\\Desktop\\Data Science\\교육팀\\sex ratio.csv', engine='python')
years = df.columns[1:]
idx = [i for i in df.iloc[:,0] for j in years]
years = list(years) * len(df)

new_df = pd.DataFrame()
new_df['지역'] = idx; new_df['연도'] = years; new_df['성비'] = np.array(df.iloc[:,1:]).reshape(len(idx))
new_df.to_csv('C:\\Users\\myeon\\Desktop\\Data Science\\교육팀\\new sex ratio.csv', encoding = 'euc-kr')

##

df = pd.read_csv('C:\\Users\\myeon\\Desktop\\Data Science\\교육팀\\province data.csv', engine='python')
gdp = df.groupby(['id'])['gdp'].mean()
unemployment = df.groupby(['id'])['unemployment'].mean()
sexratio = df.groupby(['id'])['sexratio'].mean()

from matplotlib import pyplot as plt

plt.scatter(gdp[sexratio >= 110], unemployment[sexratio >= 110], color='blue', marker='x')
plt.scatter(gdp[sexratio < 110], unemployment[sexratio < 110], color='red', marker='^')
plt.xlabel('GDP'); plt.ylabel('UNEMPLOYMENT')
plt.show()

# Quest 제출 시 제목을 'Session03 이름'으로 해주세요. ex. Session03 김현세


# 1
# numpy, pandas를 활용하여, ‘sex ratio.csv’로부터 아래와 같은 형태를 가진 ‘new sex ratio.csv’를 반환하는 코드를 구현해주세요.
import numpy as np
import pandas as pd
df = pd.read_csv('sex ratio.csv', engine = 'python', index_col = 0)

# 성비
dfv=df.values
# dfv.shape # 열 몇개? # [0] : 몇개의 행?
sexratio=dfv.reshape((192))

# 지역 설정
regionlist=[]
for i in range(dfv.shape[0]):
    region=df.index.values[i]
    for j in range(dfv.shape[1]-1):
        region=np.append(region,df.index.values[i])
    regionlist=np.append(regionlist,region)
# len(regionlist)    

# 연도 설정
yearlist=df.columns.values
for i in range(dfv.shape[0]-1):
    yearlist=np.append(yearlist,df.columns.values)
# len(yearlist)

# 새 데이터프레임 제작
new_df = pd.DataFrame({'지역':regionlist, '연도':yearlist, '성비':sexratio})
new_df.to_csv('new sex ratio.csv',encoding="euc-kr")


# 2
# ‘province data.csv’로부터 지역별로 전 기간에 걸친 평균 gdp와 unemploymen를 구한 뒤, 이를 산포도로 표현하세요.
# 단, 평균 성비가 110 이상인 지역의 산포도는 파란색 X 모양의 점, 110 미만인 지역의 산포도는 빨간색 세모 모양의 점으로 표현하세요.

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('province data.csv', engine = 'python', index_col = 0)
idlist = set(df.index.values)

# GDP,UNEMPLOYMENT 평균 구하고, SEX_RATIO에 따른 마커,색 얻기
gdp=[]
unemp=[]
colors=[]
markers=[]

for i in idlist:
    mean_gdp=np.mean(df.loc[i,'gdp'])
    mean_unemp=np.mean(df.loc[i,'unemployment'])
    mean_sexratio=np.mean(df.loc[i,'sexratio'])

    gdp.append(mean_gdp)
    unemp.append(mean_unemp)
    if mean_sexratio <=110:
        colors.append('red')
        markers.append('^')
    else:
        colors.append('blue')
        markers.append('x')

# SCATTER로 마커 모양 지정이 안되서 PLOT 사용
for i in range(len(gdp)):
    plt.scatter(gdp[i],unemp[i],color=colors[i],marker=markers[i])

plt.xlabel("GDP")
plt.ylabel("UNEMPLOYMENT")
plt.show()

