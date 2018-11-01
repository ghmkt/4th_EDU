# Quest 제출 시 제목을 'Session04 이름'으로 해주세요. ex. Session04 이재경


# Crawling Quest
# http://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=100&sid2=269
# 위의 주소는 네이버 정치 일반 기사 페이지의 주소입니다. 한 페이지에는 20개의 기사가 있습니다. 
# 최신 5페이지에 걸쳐 100개의 제목과 기사를 가져올 수 있는 코드를 작성해주세요.


# Machine Learning Quest는 아래 1, 2 중 택1입니다.

# Machine Learning Quest 1
# 'caschool.csv' 데이터에서 str과 avginc변수를 통해 read_scr을 예측할 수 있는 y=a*x1+b*x2+c 모형으로 Cost function을 minimize해보세요.
import pandas as pd
df = pd.read_csv("C:/users/lg01/desktop/caschool.csv", engine = 'python', index_col = 0)

x1 = df["str"]
x2 = df["avginc"]
y = df["read_scr"]
print(len(x1), len(x2), len(y))

import scipy
from scipy import optimize as op
def f(a):
    for i in range(1,421):
        cost_function = 0
        cost_function += (a[0]*x1[i] + a[1]*x2[i] + a[2] -y[i])**2
    return cost_function
result = op.minimize(f,(1,1,1))
print(result)
# Machine Learning Quest 2
# 앤드류 강의 week1과 week2에서 필요한 강의 듣고 중요 내용 요약해서 올리기
# https://www.coursera.org/learn/machine-learning
