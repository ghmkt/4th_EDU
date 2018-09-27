# 1
# https://programmers.co.kr/learn/courses/30/lessons/12907
# 위 링크의 문제를 풀어주세요.
def solution(n, money):
    money.sort()
    money.reverse()
    def inner_function(n, money):
        max_unit_value = money[0]
        quotient = n // max_unit_value
        count = 0
        tmp = money[1:]
        if quotient == 0:
            if not tmp:
                return 0
            else:
                changes = n % max_unit_value
                count += inner_function(changes, tmp)
                return count
        else:
            for i in range(quotient,-1,-1):
                changes = n - i * max_unit_value
                if changes == 0:
                    count += 1
                else:
                    if not tmp:
                        return count
                    else:    
                        count += inner_function(changes, tmp)
        return count
    return inner_function(n, money)

# 풀었는데 효율성 문제 때문에 통과를 못하네요........흑흑

# 2
# 짝수인 원소에 대응하는 인덱스의 합을 리턴하는 함수 f4()를 만들어주세요. 단, 제어문(for, while, if)을 사용하지 마세요!
# Hint : map, lambda, filter, enumerate
def f4(list_):
    tmp = list(filter(lambda x: x[0]%2 == 0 , list(enumerate(list_))))
    return sum(list(map(lambda x : x[0], tmp)))
f4([1,2,3,4])
f4([1,2,3,4,5])

# 3
# diamonds_data.csv 의 열을 뒤집은 파일을 생성하는 코드를 만들어주세요.
# (carat, depth, table, price, x, y, z) => (z, y, x, price, table, depth, carat)

import pandas as pd
try:
    dataframe = pd.read_csv('/Users/daham/Desktop/GrowthHackers/quest1/diamonds_data.csv')
except:
    print('경로지정 잘못하셨습니다.')
result = dataframe[list(reversed(dataframe.columns))]
result.to_csv('/Users/daham/Desktop/GrowthHackers/quest1/result.csv')


