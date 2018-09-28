### 1. numpy, pandas를 활용하여, ‘sex ratio.csv’로부터 아래와 같은 형태를 가진 ‘new sex ratio.csv’를 반환하는 코드를 구현해주세요.

import pandas as pd 
df = pd.read_csv("sex ratio.csv")

df.rename(columns = {"Unnamed: 0"  : "지역"}, inplace = True) # 빈 컬럼명을 "지역"으로 할당
df2 = pd.melt(df,id_vars = ["지역"], var_name ="연도", value_name = "성비" ) # wide 데이터를 long 데이터로 변환
df2 = df2.sort_values(["지역","연도"]) # 지역과 연도로 재정렬
df2 = df2.reset_index(drop = True) # 새로운 인덱스로 갱신
df2.to_csv("new sex ratio.csv", encoding= "EUC - KR") # 변화된 파일 저장

### 2.‘province data.csv’로부터 지역별로 전 기간에 걸친 평균 gdp와 unemploymen를 구한 뒤, 이를 산포도로 표현하세요.
### 단, 평균 성비가 110 이상인 지역의 산포도는 파란색 X 모양의 점, 110 미만인 지역의 산포도는 빨간색 세모 모양의 점으로 표현하세요.


from matplotlib import pyplot as plt
pro = pd.read_csv("province data.csv")

pro2 = pro.groupby(["id"]).mean() # 지역을 기준으로 변수들을 평균
high = pro2.loc[pro2["sexratio"] >= 110, :] # 평균 성비가 110이상인 행만 인덱싱해서 high 변수에 할당.
low = pro2.loc[pro2["sexratio"] < 110, :] # 평균 성비가 100미만인 행만 인덱싱해서 low 변수에 할당.

plt.scatter(high['gdp'], high['unemployment'], c = "b", marker= "x") # high 그룹을 산점도로 표현
plt.scatter(low['gdp'], low['unemployment'], c = "r", marker= "^")  # low 그룹을 산점도로 표현 
plt.xlabel("GDP") ; plt.ylabel("UNEMPLOYMENT") # 라벨 추가
plt.show()
