# Quest 제출 시 제목을 'Session03 이름'으로 해주세요. ex. Session03 김현세


# 1
# numpy, pandas를 활용하여, ‘sex ratio.csv’로부터 아래와 같은 형태를 가진 ‘new sex ratio.csv’를 반환하는 코드를 구현해주세요.

import pandas as pd
import pandas as pd
import numpy as np
df= pd.read_csv(r'C:\Users\EdwinPark\Dropbox\GrowthHackers\Session\session 3\sex ratio.csv', encoding= 'EUC-KR')
new_df=new_df1=pd.DataFrame({"지역":[df.iloc[0,0]]*(df.shape[1]-1),"연도":list(df.columns.values)[1:df.shape[0]],"성비":df.iloc[0,1:]})
for n in range(1,16):

    new_df = new_df.append(pd.DataFrame({"지역":[df.iloc[n,0]]*(df.shape[1]-1),"연도":list(df.columns.values)[1:df.shape[0]],"성비":df.iloc[n,1:]}))
new_df=new_df.reset_index()
new_df=new_df.drop(columns=['index'])
new_df.to_csv('new sex ratio.csv', encoding = 'EUC-KR')

# 2
# ‘province data.csv’로부터 지역별로 전 기간에 걸친 평균 gdp와 unemploymen를 구한 뒤, 이를 산포도로 표현하세요.
# 단, 평균 성비가 110 이상인 지역의 산포도는 파란색 X 모양의 점, 110 미만인 지역의 산포도는 빨간색 세모 모양의 점으로 표현하세요.

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
df=pd.read_csv(r'C:\Users\EdwinPark\province data.csv')
plt.scatter(df.groupby(['id']).mean()[df.groupby(['id']).mean().sexratio>=110]['gdp'],df.groupby(['id']).mean()[df.groupby(['id']).mean().sexratio>=110]['unemployment'],color='blue',marker='x')
plt.scatter(df.groupby(['id']).mean()[df.groupby(['id']).mean().sexratio<110]['gdp'],df.groupby(['id']).mean()[df.groupby(['id']).mean().sexratio<110]['unemployment'],color='red',marker='^')
plt.xlabel('GDP')
plt.ylabel('UNEMPLOYMENT')
plt.show()
