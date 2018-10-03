# Quest 제출 시 제목을 'Session03 이름'으로 해주세요. ex. Session03 김현세


# 1
# numpy, pandas를 활용하여, ‘sex ratio.csv’로부터 아래와 같은 형태를 가진 ‘new sex ratio.csv’를 반환하는 코드를 구현해주세요.
import pandas as pd
import numpy as np
sex_ratio = pd.read_csv('/Users/daham/Desktop/GrowthHackers/Session03/sex ratio.csv', index_col=0)
columns = sex_ratio.columns
result_df = pd.DataFrame()
for i in range(len(sex_ratio)):
    tmp = pd.DataFrame(sex_ratio.iloc[i])
    tmp['지역'] = tmp.columns[0]
    tmp.columns = ['성비', '지역']
    tmp['연도'] = tmp.index
    result_df = result_df.append(tmp,ignore_index=True)

result_df = result_df[['지역', '연도', '성비']]
result_df.to_csv('/Users/daham/Desktop/GrowthHackers/Session03/new_sex ratio.csv')

# 2
# ‘province data.csv’로부터 지역별로 전 기간에 걸친 평균 gdp와 unemploymen를 구한 뒤, 이를 산포도로 표현하세요.
# 단, 평균 성비가 110 이상인 지역의 산포도는 파란색 X 모양의 점, 110 미만인 지역의 산포도는 빨간색 세모 모양의 점으로 표현하세요.

import matplotlib.pyplot as plt

province = pd.read_csv('/Users/daham/Desktop/GrowthHackers/Session03/province data.csv', index_col=0)
local_id = list(set(province.index))
result_df = pd.DataFrame()

for i in local_id:
    tmp = province.loc[i,['gdp', 'unemployment', 'sexratio']].mean()
    result = pd.DataFrame(tmp, columns=[i]).T
    result_df = result_df.append(result)

blue_x = result_df.loc[result_df['sexratio']>=110,:]
red_triangle = result_df.loc[result_df['sexratio']<110,:]

plt.scatter(blue_x['gdp'], blue_x['unemployment'], marker='x', color = 'b')
plt.scatter(red_triangle['gdp'], red_triangle['unemployment'], marker='^', color = 'r')
plt.xlabel('GDP')
plt.ylabel('UNEMPLOYMENT')
plt.show()
