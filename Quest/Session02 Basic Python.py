# 1
# https://programmers.co.kr/learn/courses/30/lessons/12907
# 위 링크의 문제를 풀어주세요.


# 2
# 짝수인 원소에 대응하는 인덱스의 합을 리턴하는 함수 f4()를 만들어주세요. 단, 제어문(for, while, if)을 사용하지 마세요!
# Hint : map, lambda, filter, enumerate
def f4(li):
    mylist=list(filter(lambda x: x[1]%2== 0, list(enumerate(li))))
    return sum(list(map(lambda x: x[0], mylist)))

# 3
# diamonds_data.csv 의 열을 뒤집은 파일을 생성하는 코드를 만들어주세요.
# (carat, depth, table, price, x, y, z) => (z, y, x, price, table, depth, carat)

import pandas as pd
try:
    data = pd.read_csv("C:\\Users\\Yang\\Downloads\\diamonds_data.csv")
except FileNotFoundError:
    print('wrong file path')
    
new_data = data.sort_index(axis=1, ascending=False)
new_data.to_csv("C:\\Users\\Yang\\Downloads\\new_data.csv")
