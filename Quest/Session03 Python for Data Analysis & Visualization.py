# Quest 제출 시 제목을 'Session03 이름'으로 해주세요. ex. Session03 임정빈
# 1
# numpy, pandas를 활용하여, ‘sex ratio.csv’로부터 아래와 같은 형태를 가진 ‘new sex ratio.csv’를 반환하는 코드를 구현해주세요.

import numpy as np
import pandas as pd

data = pd.read_csv('./sex ratio.csv')
data.columns = ["code", 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017]
sex_rate = []
year_list = []
place = []

for year in range(2006, 2018):
    sex_rate += list(data[year])
    for code in data["code"]:
        year_list.append(year)
        place.append(code)
        
new_data = pd.DataFrame()
temp = {"province": place, 
       "year": year_list,
       "sex_rate": sex_rate}
df = pd.DataFrame(temp)
new_data = df.sort_values(["province","year"], ascending=True).reset_index()
del new_data['index']
new_data.head()
new_data.to_csv("new sex ratio.csv", encoding = "utf-8")

# 2
# ‘province data.csv’로부터 지역별로 전 기간에 걸친 평균 gdp와 unemploymen를 구한 뒤, 이를 산포도로 표현하세요.
# 단, 평균 성비가 110 이상인 지역의 산포도는 파란색 X 모양의 점, 110 미만인 지역의 산포도는 빨간색 세모 모양의 점으로 표현하세요.
import matplotlib.pyplot as plt
province_data = pd.read_csv('./province data.csv')
province_data.head()
#평균 sexratio가 110이상, 미만으로 나누어서 지역 목록 up,down에 저장.
id_sexratio = province_data.groupby(['id'])['sexratio'].mean()
sr_list = dict(id_sexratio)
up = []
down = []
for i in list(sr_list.keys()):
    if sr_list[i] >= 110:
        up.append(i)
    else:
        down.append(i)
# 성비 110 넘는 그룹, 안넘는 그룹에서 각각 지역별 전기간에 걸친 평균 gdp. unemployment 구하기
up_gdp = []
up_unemployment = []
down_gdp = []
down_unemployment = []
for place in up:
    up_gdp.append(province_data[province_data.id == place]['gdp'].mean())
    up_unemployment.append(province_data[province_data.id == place]['unemployment'].mean())
for place in down:
    down_gdp.append(province_data[province_data.id == place]['gdp'].mean())
    down_unemployment.append(province_data[province_data.id == place]['unemployment'].mean())

# 그래프 그리기. 짜자잔!
plt.scatter(up_gdp, up_unemployment, marker="x", color="blue")
plt.scatter(down_gdp, down_unemployment, marker="^", color="red")
plt.show()
