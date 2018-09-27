# 1
# https://programmers.co.kr/learn/courses/30/lessons/12907
# 위 링크의 문제를 풀어주세요.

# 풀이 1번
def solution(n, money):
  res = [0]*(n+1)
  res[0] = 1
  for i in money:
    for j in range(i, n+1):
      res[j] += res[j-i]
  return res[n]

# 풀이 2번
def solution(n, money): # 재귀함수 이용
  if len(money) == 1:
    if n%money[0] == 0:
      return 1
    else:
      return 0
  else:
    res = 0
    for i in range(n//money[0]+1):
      res += solution(n-i*money[0], money[1:])
    return res
  

# 2
# 짝수인 원소에 대응하는 인덱스의 합을 리턴하는 함수 f4()를 만들어주세요. 단, 제어문(for, while, if)을 사용하지 마세요!
# Hint : map, lambda, filter, enumerate

def f4(lst):
    return sum(map(lambda x: x[0], filter(lambda x:x[1]%2==1, enumerate(lst))))

# 3
# diamonds_data.csv 의 열을 뒤집은 파일을 생성하는 코드를 만들어주세요.
# (carat, depth, table, price, x, y, z) => (z, y, x, price, table, depth, carat)

import pandas as pd

try:
  data = pd.read_csv("diamonds_data.csv", engine='python')
except FileNotFoundError:
    print ("wrong file path")
    
reversed_data = data[data.columns[::-1]]
reversed_data.to_csv("diamonds_data_reversed.csv")
