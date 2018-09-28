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

# http://gomoveyongs.tistory.com/m/65 에 이해하기 쉽게 설명이 되어 있습니다.
# 풀이 1번은 dynamic programming을 이용하여 풀되, 2차원 행렬이 아닌 1차원 리스트에서 경우의 수를 업데이트 했습니다.


# 풀이 2번
def solution(n, money):     # 재귀함수 이용
  if len(money) == 1:       # base case : 동전의 종류가 하나일 때, n이 동전의 단위로 나누어 떨어지면 1, 아니면 0
    if n%money[0] == 0:
      return 1              
    else:
      return 0
  else:
    res = 0
    for i in range(n//money[0]+1):              # 이 for문에서 money[0]를 사용하는 경우는 모두 생각하고 남은 금액은 다른 동전들이 해결하도록 
                                                # solution()에게 넘겨 줄 것이다.
      res += solution(n-i*money[0], money[1:])  # money[0]를 i번 만 사용하고 남은 금액은 money[1:]이 해결하도록 하면, 
                                                # 언젠가 base case가 되어 리턴될 것이다.
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
