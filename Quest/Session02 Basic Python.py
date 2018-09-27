# 1
# https://programmers.co.kr/learn/courses/30/lessons/12907
# 위 링크의 문제를 풀어주세요.
def solution(money,coins):
    answer=0
    if(money==0):
        return 1
    if(len(coins)==1):
        if(money%coins[0]==0):
            return 1
        else:
            return 0
    else:
        k=coins.pop()
        t=int(money/k)
        for i in range(0,t+1):
            answer=answer+solution(money-k*i,coins)
        return answer

mon=int(input(''))
coin_list=list(map(int, input().split()))
coin_list.sort()
print(solution(mon,coin_list))

# 2
# 짝수인 원소에 대응하는 인덱스의 합을 리턴하는 함수 f4()를 만들어주세요. 단, 제어문(for, while, if)을 사용하지 마세요!
# Hint : map, lambda, filter, enumerate
def f4(listt):
    hello = list(filter(lambda x: x[0]%2==0, list(enumerate(listt))))
    ans = sum(list(map(lambda x: x[0], hello)))
    return ans

# 3
# diamonds_data.csv 의 열을 뒤집은 파일을 생성하는 코드를 만들어주세요.
# (carat, depth, table, price, x, y, z) => (z, y, x, price, table, depth, carat)
import pandas as pd

try:
    data = pd.read_csv('C:/Users/lg01/Desktop/diamonds_data.csv')
except FileNotFoundError:
    print('wrong file path')
    
new = data[list(reversed(data.columns))]
new.to_csv('C:/Users/lg01/Desktop/new.csv')
