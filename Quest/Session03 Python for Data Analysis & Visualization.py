Session03 오동건

### 1. numpy, pandas를 활용하여, ‘sex ratio.csv’로부터 아래와 같은 형태를 가진 ‘new sex ratio.csv’를 반환하는 코드를 구현해주세요.

#### 모듈 불러오기
import pandas as pd
import numpy as np

#### 데이터 불러오기
df = pd.read_csv("sex ratio.csv")

#### 비어있는 컬럼명을 "지역"으로 바꾼다. 
df.rename(columns = {"Unnamed: 0"  : "지역"}, inplace = True)

####  melt로 wide 행태의 자료형을 long 형태로 바꾼다.  
#### 지역이 기준이 되기 때문에 id_vars 전달인자에 "지역"을 넣는다.
#### 변화된 자료에 "연도"와 "성비"라는 열 이름을 할당한다. 
df2 = pd.melt(df,id_vars = ["지역"], var_name ="연도", value_name = "성비" )

#### 데이터를 지역과 연도를 기준으로 다시 정렬한다. 
df2 = df2.sort_values(["지역","연도"])

#### 기존의 인덱스는 필요없기 때문에 새로운 인덱스로 갱신한다. 
df2 = df2.reset_index(drop = True)

#### 새로운 자료형태를 확인한다. 
df2.head()

#### 변경된 자료로 새로운 csv 파일을 만든다. 
df2.to_csv("new sex ratio.csv", encoding= "EUC - KR")

### 2.‘province data.csv’로부터 지역별로 전 기간에 걸친 평균 gdp와 unemploymen를 구한 뒤, 이를 산포도로 표현하세요.
### 단, 평균 성비가 110 이상인 지역의 산포도는 파란색 X 모양의 점, 110 미만인 지역의 산포도는 빨간색 세모 모양의 점으로 표현하세요.

#### 모듈 및 자료 불러오기
from matplotlib import pyplot as plt
pro = pd.read_csv("province data.csv")
pro.head()

#### 지역을 기준으로 값을 평균낸다. 
pro2 = pro.groupby(["id"]).mean()

#### 평균 성비가 110이상인 지역과 미만인 지역을 나눈다. 
high = pro2.loc[pro2["sexratio"] >= 110, :]
low = pro2.loc[pro2["sexratio"] < 110, :]

#### 각각의 점들을 문제의 조건에 맞춰 그린다. 
plt.scatter(high['gdp'], high['unemployment'], c = "b", marker= "x") 
plt.scatter(low['gdp'], low['unemployment'], c = "r", marker= "^") 
plt.xlabel("GDP")
plt.ylabel("UNEMPLOYMENT")
plt.show()
