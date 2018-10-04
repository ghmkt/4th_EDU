# Quest 제출 시 제목을 'Session03 이름'으로 해주세요. ex. Session03 김현세


# 1
# numpy, pandas를 활용하여, ‘sex ratio.csv’로부터 아래와 같은 형태를 가진 ‘new sex ratio.csv’를 반환하는 코드를 구현해주세요.
import pandas as pd
import numpy as np

data = pd.read_csv('D:/Growth Hackers/Session03/sex ratio.csv', engine = 'python', index_col = 0)
columns = data.columns
print(data.head())

df = pd.DataFrame(columns = ["지역", "연도", "성비"])

for i in range(len(columns)):
    new_data = pd.DataFrame({"지역": [data.index[i] for j in range(len(columns))], 
                             "연도": columns, 
                             "성비": data.iloc[i]})
    df = df.append(new_data, ignore_index=True)

df = df[["지역", "연도", "성비"]]

print(df.head())
df.to_csv("D:/Growth Hackers/Session03/new sex ratio.csv", encoding = 'EUC-KR')

# 2
# ‘province data.csv’로부터 지역별로 전 기간에 걸친 평균 gdp와 unemploymen를 구한 뒤, 이를 산포도로 표현하세요.
# 단, 평균 성비가 110 이상인 지역의 산포도는 파란색 X 모양의 점, 110 미만인 지역의 산포도는 빨간색 세모 모양의 점으로 표현하세요.
from matplotlib import pyplot as plt

pro_data = pd.read_csv('D:/Growth Hackers/Session03/province data.csv', engine = 'python', index_col = 0)
print(pro_data.head())

df_id = pro_data.groupby("id")
df_average = df_id["gdp", "unemployment", "sexratio"].mean()

higher_ratio = df_average[df_average.sexratio>=110]
lower_ratio = df_average[df_average.sexratio<110]

plt.figure(figsize=(20,20))
plt.scatter(higher_ratio["gdp"], higher_ratio["unemployment"], color = "blue", marker = "x", label = "sexratio more or equal than 110")
for x, y, z in zip(higher_ratio["gdp"], higher_ratio["unemployment"], higher_ratio["sexratio"]):
    plt.annotate(z, xy=(x,y)) 
plt.scatter(lower_ratio["gdp"], lower_ratio["unemployment"], color = "red", marker = "^", label = "sexratio less than 110")
for x, y, z in zip(lower_ratio["gdp"], lower_ratio["unemployment"], lower_ratio["sexratio"]):
    plt.annotate(z, xy=(x,y))
             
plt.title('Average GDP & Unemployment') #
plt.xlabel('Average GDP') 
plt.ylabel('Average Unemployment') 
plt.grid(True) 
plt.legend() 

plt.show()
