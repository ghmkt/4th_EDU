# 1
# https://programmers.co.kr/learn/courses/30/lessons/12907
# 위 링크의 문제를 풀어주세요.

for n in range(1, 100001):
    for m in range(0, 101):
        def solution(s, m , n):
            if n == 0:
                return 1
            elif n < 0:
                return 0
            else:
                return (solution(s, m-1, n) + solution(s, m, n-s[m-1])) % 100000007
#recursion 방식을 찾아 다시 시도해 보았는데, 이번에는 recursionerror가 나와서 다시 해보겠습니다

# 2
# 짝수인 원소에 대응하는 인덱스의 합을 리턴하는 함수 f4()를 만들어주세요. 단, 제어문(for, while, if)을 사용하지 마세요!
# Hint : map, lambda, filter, enumerate

def f4(a):
  list1 = [0,1,2,3,4,5,6]
  a = dict(enumerate(filter(lambda x : x % 2 == 0, list1)))
  v = sum(a.values())
  return v
print(f4(a))

# 3
# diamonds_data.csv 의 열을 뒤집은 파일을 생성하는 코드를 만들어주세요.
# (carat, depth, table, price, x, y, z) => (z, y, x, price, table, depth, carat)

try:
    dm = pd.read_csv("C:\diamonds_data.csv")
except FileNotFoundError:
    print("Wrong File Path")
new_dm = list(dm.columns[0:8])
new_dm.reverse()
dm = dm[new_dm]
dm.to_csv('new_dm.csv')
