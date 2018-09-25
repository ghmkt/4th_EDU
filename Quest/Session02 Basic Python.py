# 1
# https://programmers.co.kr/learn/courses/30/lessons/12907
# 위 링크의 문제를 풀어주세요.

for n in range (1, 100001):
    for m in range (1, 101):
        def solution (S, m, n):
            if (n==0):
                return 1;
            if (n <0):
                return 0;
            if (m <=0 and n >=1):
                return 0
            return (solution (S, m-1, n) + solution (S, m, n-S[m-1])) #//100000007
        
CoinValue = [1, 2, 5]
m = len(CoinValue)
print(solution(CoinValue, m, 1000))


# 2
# 짝수인 원소에 대응하는 인덱스의 합을 리턴하는 함수 f4()를 만들어주세요. 단, 제어문(for, while, if)을 사용하지 마세요!
# Hint : map, lambda, filter, enumerate

def f4(x):
    return (sum(list(map(lambda x: x[0], filter(lambda x: x[0]%2==0, enumerate(x))))))

x = [1,2,3,4,5]
print(f4(x))


# 3
# diamonds_data.csv 의 열을 뒤집은 파일을 생성하는 코드를 만들어주세요.
# (carat, depth, table, price, x, y, z) => (z, y, x, price, table, depth, carat)

import pandas as pd

try: data = pd.read_csv("D:/Growth Hackers/diamonds_data.csv", engine='python')
except FileNotFoundError:
    print ("wrong file path")
    
data_re = data[data.columns[::-1]]
data_re.to_csv("D:/Growth Hackers/diamonds_data_2.csv")
print (data.head(), "/n", data_re.head())
