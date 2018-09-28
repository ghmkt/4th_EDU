# Quest 제출 시 제목을 'Session03 이름'으로 해주세요. ex. Session03 김현세


# 1
# numpy, pandas를 활용하여, ‘sex ratio.csv’로부터 아래와 같은 형태를 가진 ‘new sex ratio.csv’를 반환하는 코드를 구현해주세요.
import pandas as pd

data = pd.read_csv('C:\\Users\\승우\\Desktop\\sex ratio.csv', engine='python')
# 이상하게도 raw data에서는 빈칸으로 되어있던 변수명이, data로 받아오면 이상한 문자로 변형이 되어 나타납니다.
new_col = data.columns.values
new_col[0] = ''
data.columns = new_col
# 그래서 이상한 문자를 그냥 공백으로 바꾸어버렸습니다.
data_tr = pd.DataFrame.transpose(data)
data_vari = data_tr.iloc[0, :]

new_col2 = data_tr.columns.values
new_col2 = data_vari
data_tr.columns = new_col2

data_tr2 = data_tr.drop('', axis=0)


def listing(x, y, z):
    result_data = []
    for i in range(0, len(x)):
        for j in range(0, len(y)):
            result_data.append([x[i], y[j], z[j, i]])

    return result_data


result = listing(data_tr2.columns, data_tr2.index, data_tr2.iloc)
result2 = pd.DataFrame(result)

result2_col = result2.columns.values
result2_col = ['지역', '연도', '성비']
result2.columns = result2_col

result2.to_csv('C:\\Users\\승우\\Desktop\\new sex ratio.csv', encoding='EUC-KR')


# 2
# ‘province data.csv’로부터 지역별로 전 기간에 걸친 평균 gdp와 unemploymen를 구한 뒤, 이를 산포도로 표현하세요.
# 단, 평균 성비가 110 이상인 지역의 산포도는 파란색 X 모양의 점, 110 미만인 지역의 산포도는 빨간색 세모 모양의 점으로 표현하세요.
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('C:\\Users\\승우\\Desktop\\province data.csv', engine='python')

gdp_mean=pd.DataFrame(data.groupby('id')['gdp'].mean())
unim_mean=pd.DataFrame(data.groupby('id')['unemployment'].mean())
sex_mean=pd.DataFrame(data.groupby('id')['sexratio'].mean())


data2=pd.DataFrame({'gdp':gdp_mean.get('gdp'),'unemployment':unim_mean.get('unemployment'),'sexratio':sex_mean.get('sexratio')})


big_110=data2[data2['sexratio']>=110][['gdp','unemployment']]
b_gdp=big_110['gdp']
b_une=big_110['unemployment']
sma_110=data2[data2['sexratio']<110][['gdp','unemployment']]
s_gdp=sma_110['gdp']
s_une=sma_110['unemployment']


plt.scatter(b_gdp, b_une, color='blue', marker='x')
plt.scatter(s_gdp, s_une, color='red', marker='^')
plt.xlabel('GDP')
plt.ylabel('UNEMPLOYMENT')
