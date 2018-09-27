# 1
# https://programmers.co.kr/learn/courses/30/lessons/12907
# 위 링크의 문제를 풀어주세요.

def solution(n, money):
    big_return = money[len(money)-1]
    big_count = n // big_return
    if len(money) == 1:
        if n % big_return == 0 :
            return 1
        else:
            return 0
    else:
        answer = 0
        for i in range(big_count+1):
            answer += solution(n - big_return*i, money[:len(money)-1])
        return answer % 1000000007
    
print(solution(30, [1,2,3,5,7]))


# 2
# 짝수인 원소에 대응하는 인덱스의 합을 리턴하는 함수 f4()를 만들어주세요. 단, 제어문(for, while, if)을 사용하지 마세요!
# Hint : map, lambda, filter, enumerate

def f4(given_list):
    even_list = list(filter(lambda a: a%2 == 0, given_list))
    index_list = list(map(lambda a: given_list.index(a), even_list))
    sum_index = sum(index_list)
    return sum_index

test_1 = [3,7,8,1]
test_2 = [1,3,5,7]
test_3 = [2,4,6,8]
print(f4(test_1))
print(f4(test_2))
print(f4(test_3))
# 3
# diamonds_data.csv 의 열을 뒤집은 파일을 생성하는 코드를 만들어주세요.
# (carat, depth, table, price, x, y, z) => (z, y, x, price, table, depth, carat)

from pandas import DataFrame
import pandas as pd
try :
    dia_data = pd.read_csv('C:\\dev\\4th-EDU\\Session\\diamonds_data.csv', sep = ',')
    reversed_dia_data = DataFrame(dia_data, columns = ['z', 'y', 'x', 'price', 'table', 'depth', 'carat', '-'])
    reversed_dia_data.to_csv('C:\\dev\\4th-EDU\\Session\\reversed_dia_data.csv', sep = ',')
    print(reversed_dia_data)
except:
     print("wrong file path")
