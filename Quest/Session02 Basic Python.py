# 1
# https://programmers.co.kr/learn/courses/30/lessons/12907
# 위 링크의 문제를 풀어주세요.

def Solution(n, money):
    a = [0]*100
    d = [0]*100001  
    
    for i in range(len(money)):
        a[i] = money[i]
        
    d[0] = 1
    for j in range(len(money)):
        for k in range(a[j],n+1):
            d[k] += d[k-a[j]]
            
    return d[k] % 1000000007


print(Solution(5,[1,2,5]))

# 2
# 짝수인 원소에 대응하는 인덱스의 합을 리턴하는 함수 f4()를 만들어주세요. 단, 제어문(for, while, if)을 사용하지 마세요!
# Hint : map, lambda, filter, enumerate


def f4(i):
    return(sum(map(lambda x:x[0],filter(lambda x:x[1] % 2 == 0, enumerate(i)))))

print(f4([1,2,3,4]))
print(f4([2,1,3,8,5]))

# 3
# diamonds_data.csv 의 열을 뒤집은 파일을 생성하는 코드를 만들어주세요.
# (carat, depth, table, price, x, y, z) => (z, y, x, price, table, depth, carat)

import pandas as pd

try:
    dia =  pd.read_csv('C:\\Users\\renz\\Desktop\\diamonds_data.csv')
except:
    print("wrong file path")


dia = dia.T.iloc[:: -1].T

dia.to_csv('C:\\Users\\renz\\Desktop\\diamonds_data_2.csv')
