# 1
# https://programmers.co.kr/learn/courses/30/lessons/12907
# 위 링크의 문제를 풀어주세요.
def solution(n, money):
    count = 0
    for i in range(len(money)):
        if n >= money[i]:
            if n % money[i] == 0:
                count += 1
            for j in range(n // money[i]):
                count += solution(n-(j+1)*money[i], money[i+1:])
    answer= count % 1000000007          
    return answer

solution(5,[1,2,5])


# 2
# 짝수인 원소에 대응하는 인덱스의 합을 리턴하는 함수 f4()를 만들어주세요. 단, 제어문(for, while, if)을 사용하지 마세요!
# Hint : map, lambda, filter, enumerate
def f4(alist):
    index_list = list(map(lambda x : x[0] , enumerate(alist)))
    even_index = list(filter(lambda y : y % 2 == 0, index_list))
    return sum(even_index)

f4([1,2,3,4])
f4([1,2,3,4,5])


# 3
# diamonds_data.csv 의 열을 뒤집은 파일을 생성하는 코드를 만들어주세요.
# (carat, depth, table, price, x, y, z) => (z, y, x, price, table, depth, carat)
import pandas as pd

data = pd.read_csv('c:\project\diamonds_data.csv',index_col=0)

try:
    data2 = data[data.columns[::-1]]
    data2.to_csv('diamonds_data2.csv')    

except FileNotFoundError:
    print('wrong file path')
