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

# csv파일 불러오기
import pandas as pd
df = pd.read_csv('C:\\Users\\renoi\\Session03\\sex ratio.csv', header = None)

# 지역 column 만들기
r_list = list(df.iloc[:,0])
r2_list = r_list[1:]
region_list = []
for i in r2_list:
    r = int(i)
    count = 1
    while count <= 12:
        region_list.append(r)
        count += 1
print(region_list)
len(region_list)

# 연도 column 만들기
y_list = list(df.iloc[0,:])
y2_list = y_list[1:] * 16
year_list = []
for i in y2_list:
    y = int(i)
    year_list.append(y)
print(year_list)
len(year_list)

# 성비 column 만들기
import numpy as np

df2 = df.iloc[1:17, 1:13]
df2_numpy = df2.as_matrix()
sexratio = df2_numpy.reshape((-1, 1))
sexratio_list = []
for [i] in sexratio:
    sexratio_list.append(i)
    
# new dataframe 만들기
temp = {"지역":region_list,
        "연도":year_list,
        "성비":sexratio_list}
df3 = pd.DataFrame(temp)
df3

# new csv파일 만들기
new_df.to_csv('new sex ratio.csv', encoding = 'EUC-KR')
    
    
    
    
    
    
# 2
# ‘province data.csv’로부터 지역별로 전 기간에 걸친 평균 gdp와 unemploymen를 구한 뒤, 이를 산포도로 표현하세요.
# 단, 평균 성비가 110 이상인 지역의 산포도는 파란색 X 모양의 점, 110 미만인 지역의 산포도는 빨간색 세모 모양의 점으로 표현하세요.
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv('province data.csv', engine='python', index_col=0)
df.head()
mean = df.groupby(['id']).mean()

mean1 = mean[mean['sexratio'] < 110]
mean2 = mean[mean['sexratio'] >= 110]

plt.scatter(mean1['gdp'], mean1['unemployment'], color = 'red', marker = '^')
plt.scatter(mean2['gdp'], mean2['unemployment'], color = 'blue', marker = 'x')
plt.xlabel('gdp')
plt.ylabel('unemployment')
plt.show()
